"""{{ cookiecutter.project_name }} package."""
import pkg_resources

__version__ = pkg_resources.get_distribution("{{ cookiecutter.project_name }}").version
