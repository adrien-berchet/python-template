"""Validation tests for the Copier template itself."""

from __future__ import annotations

import json
import tomllib
from pathlib import Path

import pytest
import yaml

from tests.helpers import configure_git_identity
from tests.helpers import copy_project
from tests.helpers import run_cmd
from tests.helpers import snapshot_template


def test_template_defaults(tmp_path: Path) -> None:
    """Render the default project and run its main validation environments."""
    project_path = copy_project(tmp_path / "generated")
    pyproject_toml = project_path / "pyproject.toml"

    assert (project_path / "docs").exists()
    assert (project_path / ".github").exists()
    assert not (project_path / "Dockerfile").exists()
    assert not (project_path / "renovate.json").exists()
    assert not (project_path / ".github" / "workflows" / "publish-docs.yml").exists()
    assert not (project_path / ".github" / "workflows" / "publish-container.yml").exists()
    assert 'typeCheckingMode = "strict"' in pyproject_toml.read_text(encoding="utf-8")

    run_cmd(
        [
            "tox",
            "-e",
            "lint,type-checking,check-packaging,docs,py312,min_versions",
        ],
        cwd=project_path,
    )


def test_template_gitlab_excludes_github_files(tmp_path: Path) -> None:
    """GitLab renders should omit GitHub-only files."""
    project_path = copy_project(tmp_path / "generated", repository_provider="gitlab")

    assert not (project_path / ".github").exists()
    assert not (project_path / "AUTHORS.md").exists()
    assert not (project_path / "CONTRIBUTING.md").exists()
    assert not (project_path / "codecov.yml").exists()
    assert not (project_path / ".readthedocs.yml").exists()


def test_template_readme_docs_mode(tmp_path: Path) -> None:
    """README-only mode should omit docs-specific files and environments."""
    project_path = copy_project(
        tmp_path / "generated",
        docs_type="README",
        project_url="https://example.com/project",
    )
    pyproject_toml = (project_path / "pyproject.toml").read_text(encoding="utf-8")
    tox_ini = (project_path / "tox.ini").read_text(encoding="utf-8")

    assert not (project_path / "docs").exists()
    assert not (project_path / ".readthedocs.yml").exists()
    assert "sphinx>=" not in pyproject_toml
    assert "[testenv:docs]" not in tox_ini

    run_cmd(
        ["tox", "-e", "lint,type-checking,check-packaging,py312,min_versions"],
        cwd=project_path,
    )


def test_github_pages_docs_workflow_renders_when_enabled(tmp_path: Path) -> None:
    """GitHub Pages docs automation should be optional and coexist with RTD config."""
    project_path = copy_project(
        tmp_path / "generated",
        setup_github_pages_docs=True,
    )

    assert (project_path / ".github" / "workflows" / "publish-docs.yml").exists()
    assert (project_path / ".readthedocs.yml").exists()


def test_container_files_render_when_enabled(tmp_path: Path) -> None:
    """Container automation should render the expected files when enabled."""
    project_path = copy_project(
        tmp_path / "generated",
        setup_container=True,
    )

    assert (project_path / "Dockerfile").exists()
    assert (project_path / ".dockerignore").exists()
    assert (project_path / ".github" / "workflows" / "publish-container.yml").exists()


def test_pyright_standard_typing_mode(tmp_path: Path) -> None:
    """Pyright standard mode should render and run correctly."""
    project_path = copy_project(
        tmp_path / "generated",
        type_checker="pyright",
        strict_typing=False,
    )
    pyproject_toml = (project_path / "pyproject.toml").read_text(encoding="utf-8")

    assert 'typeCheckingMode = "standard"' in pyproject_toml
    assert "[tool.pyrefly]" not in pyproject_toml

    run_cmd(["tox", "-e", "type-checking"], cwd=project_path)


def test_pyrefly_type_checking(tmp_path: Path) -> None:
    """Pyrefly should be rendered as a first-class type-checking option."""
    project_path = copy_project(tmp_path / "generated", type_checker="pyrefly")
    pyproject_toml = (project_path / "pyproject.toml").read_text(encoding="utf-8")

    assert "[tool.pyrefly]" in pyproject_toml
    assert "[tool.pyright]" not in pyproject_toml
    assert "typeCheckingMode" not in pyproject_toml

    run_cmd(["tox", "-e", "type-checking"], cwd=project_path)


def test_invalid_repository_name(tmp_path: Path) -> None:
    """Invalid repository names should be rejected by Copier."""
    answers = tmp_path / "invalid-repo.yml"
    template_path = snapshot_template(tmp_path / "template-source")
    answers.write_text(
        yaml.safe_dump(
            {
                "project_name": "Broken Repo",
                "project_description": "Broken repo description",
                "repository_provider": "github",
                "author_name": "Example Author",
                "author_email": "author@example.com",
                "repository_namespace": "example",
                "repository_name": "bad:thing",
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    result = run_cmd(
        [
            "copier",
            "copy",
            "--UNSAFE",
            "--overwrite",
            "--defaults",
            "--data-file",
            str(answers),
            str(template_path),
            str(tmp_path / "generated"),
        ],
        check=False,
    )
    assert result.returncode != 0
    assert "is not a valid repository name" in result.stdout


def test_invalid_package_name(tmp_path: Path) -> None:
    """Invalid package names should be rejected by Copier."""
    template_path = snapshot_template(tmp_path / "template-source")
    result = run_cmd(
        [
            "copier",
            "copy",
            "--UNSAFE",
            "--overwrite",
            "--defaults",
            "-d",
            "package_name=bad-package",
            str(template_path),
            str(tmp_path / "generated"),
        ],
        check=False,
    )
    assert result.returncode != 0
    assert "is not a valid Python package name" in result.stdout


def test_empty_project_description_is_rejected(tmp_path: Path) -> None:
    """Project descriptions should not be allowed to be empty."""
    template_path = snapshot_template(tmp_path / "template-source")
    result = run_cmd(
        [
            "copier",
            "copy",
            "--UNSAFE",
            "--overwrite",
            "--defaults",
            "-d",
            "project_description=",
            str(template_path),
            str(tmp_path / "generated"),
        ],
        check=False,
    )
    assert result.returncode != 0
    assert "Please provide a short project description." in result.stdout


def test_copier_update_roundtrip(tmp_path: Path) -> None:
    """A freshly generated project should be updatable from the local template."""
    project_path = copy_project(tmp_path / "generated")

    configure_git_identity(project_path)
    run_cmd(["git", "commit", "-m", "Initial commit"], cwd=project_path)
    run_cmd(["copier", "update", "--UNSAFE", "--defaults", "--conflict", "inline"], cwd=project_path)


def test_renovate_actions_match_workflows(tmp_path: Path) -> None:
    """The optional Renovate config should ignore the shipped GitHub Actions."""
    project_path = copy_project(
        tmp_path / "generated",
        setup_renovate=True,
        setup_github_pages_docs=True,
        setup_container=True,
    )

    assert (project_path / "renovate.json").exists()
    assert not (project_path / ".github" / "dependabot.yml").exists()

    renovate_config = json.loads((project_path / "renovate.json").read_text(encoding="utf-8"))
    config_actions = set(renovate_config["packageRules"][0]["matchPackageNames"])

    used_actions: set[str] = set()
    for workflow_file in (project_path / ".github" / "workflows").glob("*.yml"):
        workflow = yaml.safe_load(workflow_file.read_text(encoding="utf-8"))
        for job in workflow.get("jobs", {}).values():
            for step in job.get("steps", []):
                action = step.get("uses")
                if action:
                    used_actions.add(action.split("@")[0])

    assert used_actions == config_actions


def test_python_versions_match_across_configs(tmp_path: Path) -> None:
    """The generated metadata and CI matrix should agree on supported versions."""
    project_path = copy_project(tmp_path / "generated")
    workflow = yaml.safe_load(
        (project_path / ".github" / "workflows" / "run-tox.yml").read_text(encoding="utf-8")
    )
    pyproject_toml = tomllib.loads((project_path / "pyproject.toml").read_text(encoding="utf-8"))

    python_versions = workflow["jobs"]["build"]["strategy"]["matrix"]["python-version"]
    assert python_versions == ["3.12", "3.13", "3.14"]
    assert pyproject_toml["project"]["requires-python"] == ">=3.12"
    assert "Programming Language :: Python :: 3.12" in pyproject_toml["project"]["classifiers"]
    assert "Programming Language :: Python :: 3.14" in pyproject_toml["project"]["classifiers"]
