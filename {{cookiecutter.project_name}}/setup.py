#!/usr/bin/env python
import importlib.util

from setuptools import setup, find_packages

# read the contents of the README file
with open("README.rst", "r", encoding="utf-8") as f:
    README = f.read()

spec = importlib.util.spec_from_file_location(
    "{{ cookiecutter.package_name }}.version",
    "{{ cookiecutter.package_name }}/version.py",
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
VERSION = module.__version__

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
    python_requires=">=3.7",
    extras_require={"docs": ["sphinx", "sphinx-bluebrain-theme"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
