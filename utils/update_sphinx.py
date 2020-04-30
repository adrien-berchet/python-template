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


def _do_replacements(content):
    """Replace portions of the conf.py"""
    # first replace the quotes around the version numbers
    content = content.replace(
        "'{{ cookiecutter.package_name }}.__version__'",
        "{{ cookiecutter.package_name }}.__version__",
    )

    # replace the html_theme variable
    content = content.replace(
        "html_theme = 'alabaster'", "html_theme = 'sphinx-bluebrain-theme'"
    )

    # comment out the static path
    static_re = re.compile(r"^html_static_path.*", flags=re.MULTILINE)
    content = static_re.sub("# \g<0>", content)

    # comment out the template path
    templates_re = re.compile(r"^templates_path.*", flags=re.MULTILINE)
    content = templates_re.sub("# \g<0>", content)

    # remove the copyright which is injected by the theme
    copyright_re = re.compile(r"^copyright.*\n", flags=re.MULTILINE)
    content = copyright_re.sub("", content)

    # remove the author which is not required
    author_re = re.compile(r"^author.*\n", flags=re.MULTILINE)
    content = author_re.sub("", content)

    # add the self import
    import_re = re.compile(r"(import sys.*?\n)(\n)", flags=re.DOTALL)
    content = import_re.sub(
        "\g<1>\nimport {{ cookiecutter.package_name }}\n\n", content
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
            "{{ cookiecutter.package_name }}.__version__",
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
