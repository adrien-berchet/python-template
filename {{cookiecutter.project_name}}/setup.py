#!/usr/bin/env python

import imp
import sys

from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    sys.exit("Sorry, Python < 3.6 is not supported")

# read the contents of the README file
with open("README.rst", encoding="utf-8") as f:
    README = f.read()

VERSION = imp.load_source("", "{{ cookiecutter.package_name }}/version.py").__version__

setup(
    name="{{ cookiecutter.project_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    version=VERSION,
    description="{{ cookiecutter.description }}",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="{{ cookiecutter.project_url }}",
    project_urls={
        "Tracker": "{{ cookiecutter.tracker_url }}",
        "Source": "{{ cookiecutter.download_url }}",
    },
    license="BBP-internal-confidential",
    install_requires=[],
    packages=find_packages(),
    python_requires=">=3.6",
    extras_require={"docs": ["sphinx", "sphinx-bluebrain-theme"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
