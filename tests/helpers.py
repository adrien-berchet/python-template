"""Helpers for validating the Copier template."""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
from pathlib import Path
from typing import Any

import yaml

TOP = Path(__file__).resolve().parent.parent


def run_cmd(
    cmd: str | list[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    """Run a subprocess command and return the completed process."""
    args = shlex.split(cmd) if isinstance(cmd, str) else cmd
    clean_env = {key: value for key, value in os.environ.items() if not key.startswith("TOX_")}
    if env:
        clean_env.update(env)
    completed = subprocess.run(
        args,
        check=False,
        cwd=cwd,
        env=clean_env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if check and completed.returncode != 0:
        raise AssertionError(completed.stdout)
    return completed


def load_answers(**overrides: Any) -> dict[str, Any]:
    """Load the canonical example answers and apply overrides."""
    with (TOP / "example-answers.yml").open(encoding="utf-8") as stream:
        answers = yaml.safe_load(stream)
    answers.update(overrides)
    return answers


def snapshot_template(snapshot_path: Path) -> Path:
    """Create a clean filesystem snapshot of the working tree for Copier."""
    if snapshot_path.exists():
        shutil.rmtree(snapshot_path)
    shutil.copytree(
        TOP,
        snapshot_path,
        ignore=shutil.ignore_patterns(
            ".git",
            ".pytest_cache",
            ".tox",
            "__pycache__",
            "*.pyc",
        ),
    )
    run_cmd(["git", "init"], cwd=snapshot_path)
    run_cmd(["git", "config", "user.name", "Template Snapshot"], cwd=snapshot_path)
    run_cmd(["git", "config", "user.email", "template.snapshot@example.com"], cwd=snapshot_path)
    run_cmd(["git", "add", "-A"], cwd=snapshot_path)
    run_cmd(["git", "commit", "-m", "Snapshot"], cwd=snapshot_path)
    return snapshot_path


def copy_project(project_path: Path, **overrides: Any) -> Path:
    """Render the local Copier template into a temporary project directory."""
    answers = load_answers(**overrides)
    answers_path = project_path.parent / f"{project_path.name}-answers.yml"
    template_path = snapshot_template(project_path.parent / f"{project_path.name}-template")
    with answers_path.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(answers, stream, sort_keys=False)
    run_cmd(
        [
            "copier",
            "copy",
            "--UNSAFE",
            "--overwrite",
            "--defaults",
            "--data-file",
            str(answers_path),
            str(template_path),
            str(project_path),
        ]
    )
    return project_path


def configure_git_identity(project_path: Path) -> None:
    """Configure a local git identity for tests that need to create commits."""
    run_cmd(["git", "config", "user.name", "Template Tester"], cwd=project_path)
    run_cmd(["git", "config", "user.email", "template.tester@example.com"], cwd=project_path)
