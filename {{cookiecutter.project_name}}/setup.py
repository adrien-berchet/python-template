"""Setup for the {{ cookiecutter.project_name }} package."""
import importlib.util
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

spec = importlib.util.spec_from_file_location(
    "{{ cookiecutter.package_name }}.version",
    "{{ cookiecutter.package_name }}/version.py",
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
VERSION = module.VERSION

setup(
    name="{{ cookiecutter.project_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    version=VERSION,
    description="{{ cookiecutter.description }}",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="{{ cookiecutter.project_url }}",
    project_urls={
        "Tracker": "{{ cookiecutter.tracker_url }}",
        "Source": "{{ cookiecutter.download_url }}",
    },
    license="BBP-internal-confidential",
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.7",
    extras_require={
        "docs": ["m2r2", "sphinx", "sphinx-bluebrain-theme"],
        "test": [
            "mock",
            "pytest",
            "pytest-cov",
            "pytest-html",
        ]
    },
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
