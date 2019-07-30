#!/usr/bin/env python

import imp
import sys

from setuptools import setup, find_packages

if sys.version_info < (2, 7):
    sys.exit("Sorry, Python < 2.7 is not supported")

VERSION = imp.load_source("", "{{ cookiecutter.package_name }}/version.py").__version__

setup(
    name="{{ cookiecutter.project_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    version=VERSION,
    description="{{ cookiecutter.description }}",
    url="{{ cookiecutter.project_url }}",
    project_urls={
        "Tracker": "{{ cookiecutter.tracker_url }}",
        "Source": "{{ cookiecutter.download_url }}",
    },
    license="BBP-internal-confidential",
    install_requires=[
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
