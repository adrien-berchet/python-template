"""Utilities for updating the docs cookiecutter content."""

import os
import pathlib
import re
import distutils.dir_util
import tempfile

import click
import sphinx.cmd.quickstart


# addtional configuration to be appended to the conf.py
ADDITIONAL_CONF = """

html_theme_options = {
    'metadata_distribution': '{{ cookiecutter.package_name }}',
}

html_title = u'{{ cookiecutter.project_name }}'

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
"""

DEFAULT_THEME = "alabaster"


def _do_replacements(content):
    """Replace portions of the conf.py"""
    # replace version placeholders
    content = content.replace(
        "'VERSION-PLACEHOLDER'",
        "get_distribution('{{ cookiecutter.package_name }}').version",
        1,
    )
    content = content.replace("'VERSION-PLACEHOLDER'", "version")

    # replace the html_theme variable
    if DEFAULT_THEME not in content:
        raise ValueError("Expected default theme was not found: %s" % DEFAULT_THEME)
    content = content.replace(DEFAULT_THEME, "sphinx-bluebrain-theme")

    # comment out the static path
    static_re = re.compile(r"^html_static_path.*", flags=re.MULTILINE)
    if static_re.search(content) is None:
        raise ValueError("Expected 'html_static_path' config variable not found")
    content = static_re.sub("# \g<0>", content)

    # comment out the template path
    templates_re = re.compile(r"^templates_path.*", flags=re.MULTILINE)
    if templates_re.search(content) is None:
        raise ValueError("Expected 'templates_path' config variable not found")
    content = templates_re.sub("# \g<0>", content)

    # remove the copyright which is injected by the theme
    copyright_re = re.compile(r"^copyright.*\n", flags=re.MULTILINE)
    if copyright_re.search(content) is None:
        raise ValueError("Expected 'copyright' config variable not found")
    content = copyright_re.sub("", content)

    # remove the author which is not required
    author_re = re.compile(r"^author.*\n", flags=re.MULTILINE)
    if author_re.search(content) is None:
        raise ValueError("Expected 'author' config variable not found")
    content = author_re.sub("", content)

    # add the get_distribution import
    import_re = re.compile(r"(import sys.*?\n)(\n)", flags=re.DOTALL)
    if import_re.search(content) is None:
        raise ValueError("Expected 'import sys' in conf.py not found")
    content = import_re.sub(
        "\g<1>\nfrom pkg_resources import get_distribution\n\n", content
    )

    return content


@click.command()
@click.option(
    "--output-path", required=True, type=click.Path(file_okay=False, exists=True)
)
def main(output_path):
    """Generate quickstart content, modify, and update the cookiecutter."""
    with tempfile.TemporaryDirectory(prefix="sphinx-quickstart") as tempdir:
        quickstart_args = [
            "--quiet",
            "--project",
            "{{ cookiecutter.project_name }}",
            "--author",
            "NSE",
            "-v",
            "VERSION-PLACEHOLDER",
            "--no-batchfile",
            "--sep",
            "-d",
            "path=" + tempdir,
        ]

        # create the default folder structure for sphinx
        sphinx.cmd.quickstart.main(quickstart_args)

        temp_path = pathlib.Path(tempdir)

        # get the path to the conf.py
        conf_path = temp_path / "source" / "conf.py"

        with open(conf_path, "r+", encoding="utf8") as conf_file:
            content = conf_file.read()
            content = _do_replacements(content)
            conf_file.seek(0)
            conf_file.write(content)
            conf_file.write(ADDITIONAL_CONF)
            conf_file.truncate()

        # we don't want to overwrite our custom index.rst
        index_path = temp_path / "source" / "index.rst"
        os.remove(index_path)

        distutils.dir_util.copy_tree(tempdir, output_path)


if __name__ == "__main__":
    main()
