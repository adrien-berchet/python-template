import os
import shutil
import sys


REMOVE_PATHS = [
    "{% if cookiecutter.repository_destination != 'github' %} .github {% endif %}",
    "{% if cookiecutter.repository_destination != 'gitlab' %} .gitlab-ci.yml {% endif %}",
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
