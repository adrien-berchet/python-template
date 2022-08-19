"""{{ cookiecutter.project_name }} package."""
{% if cookiecutter.support_py37 == 'yes' %}import pkg_resources

__version__ = pkg_resources.get_distribution("{{ cookiecutter.project_name }}").version{% else %}import importlib.metadata

__version__ = importlib.metadata.version("{{ cookiecutter.project_name }}"){% endif %}
