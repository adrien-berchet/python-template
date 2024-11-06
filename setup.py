"""Setup for the python-template."""
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

def my_version():
    from setuptools_scm.version import guess_next_version

    def clean_local_scheme(version):
        return "" if not version.dirty else "+dirty"

    def clean_scheme(version):
        return guess_next_version(version)

    return {"version_scheme": clean_scheme, "local_scheme": clean_local_scheme}


setup(
    name="python-template",
    author="bbp-ou-cells",
    author_email="bbp-ou-cells@groupes.epfl.ch",
    description="Template for Python packages",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    use_scm_version=my_version,
    setup_requires=[
        "setuptools_scm",
    ],
    python_requires=">=3.9",
    include_package_data=True,
)
