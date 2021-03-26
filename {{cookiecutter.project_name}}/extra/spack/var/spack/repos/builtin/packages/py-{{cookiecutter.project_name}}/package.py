# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


# replace all 'x-y' with 'xY' (e.g. 'Py-morph-tool' -> 'PyMorphTool')
class Py-{{ cookiecutter.project_name }}(PythonPackage):
    """{{ cookiecutter.description }}"""

    homepage = "{{ cookiecutter.project_url }}"
    git      = "{{ cookiecutter.download_url }}"

    version('develop', branch='master')
    version('{{ cookiecutter.version }}', tag='{{ cookiecutter.project_name }}-v{{ cookiecutter.version }}')

    depends_on('py-setuptools', type='build')  # type=('build', 'run') if specifying entry points in 'setup.py'

    # for all 'foo>=X' in 'install_requires' and 'extra_requires':
    # depends_on('py-foo@<min>:')
