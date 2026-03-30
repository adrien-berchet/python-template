"""Regression tests for the generated gitleaks + pre-commit configuration."""

from __future__ import annotations

import base64
import hashlib
from pathlib import Path

import pytest

from tests.helpers import copy_project
from tests.helpers import run_cmd

STABLE_LEAK_CASES = [
    ("github_token.txt", "ghp_" + "1234567890abcdefghijklmnopqrstuvwx12AB"),
    (
        "slack_webhook.txt",
        "https://hooks.slack.com/services/" + "T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
    ),
    ("stripe_secret.txt", "sk_test_" + "4eC39HqLyjWDarjtT1zdp7dcFAKE"),
]


@pytest.mark.parametrize("fname,content", STABLE_LEAK_CASES)
def test_gitleaks_stable_patterns_fail(tmp_path: Path, fname: str, content: str) -> None:
    """Known secret patterns should fail the generated lint configuration."""
    project_path = copy_project(tmp_path / "generated")

    (project_path / fname).write_text(content, encoding="utf-8")
    run_cmd(["git", "add", "-A"], cwd=project_path)
    result = run_cmd(["tox", "-e", "lint"], cwd=project_path, check=False)

    assert result.returncode != 0
    assert any(word in result.stdout.lower() for word in ["gitleaks", "leak", "secret"])


def _fake_sealed_secret_blob(n: int = 800, seed: str = "sealed-secrets-test") -> str:
    """Create deterministic base64-like ciphertext for sealed-secret tests."""
    chunk = hashlib.sha256(seed.encode("utf-8")).digest()
    raw = (chunk * ((n // len(chunk)) + 4))[: n + 64]
    body = base64.b64encode(raw).decode("ascii").replace("=", "")
    value = "Ag" + body[:n]
    remainder = len(value) % 4
    if remainder:
        value += "=" * (4 - remainder)
    return value


def test_gitleaks_yaml_allowlist_for_sealed_secrets_yaml(tmp_path: Path) -> None:
    """Generated YAML files that resemble SealedSecrets should pass linting."""
    blob = _fake_sealed_secret_blob()
    sealed_yaml = f"""\
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: demo
  namespace: default
spec:
  encryptedData:
    token: "{blob}"
"""
    project_path = copy_project(tmp_path / "generated")

    (project_path / "secret.yaml").write_text(sealed_yaml, encoding="utf-8")
    run_cmd(["git", "add", "-A"], cwd=project_path)
    run_cmd(["tox", "-e", "lint"], cwd=project_path)


def test_gitleaks_yaml_allowlist_for_sealed_secrets_yml(tmp_path: Path) -> None:
    """Generated YML files that resemble SealedSecrets should pass linting."""
    blob = _fake_sealed_secret_blob()
    sealed_yaml = f"""\
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: demo
  namespace: default
spec:
  encryptedData:
    token: "{blob}"
"""
    project_path = copy_project(tmp_path / "generated")

    (project_path / "secret.yml").write_text(sealed_yaml, encoding="utf-8")
    run_cmd(["git", "add", "-A"], cwd=project_path)
    run_cmd(["tox", "-e", "lint"], cwd=project_path)


def test_leaky_code_fails_gitleaks(tmp_path: Path) -> None:
    """Non-YAML files containing secret-like blobs should fail linting."""
    blob = _fake_sealed_secret_blob()
    project_path = copy_project(tmp_path / "generated")

    (project_path / "leaky.py").write_text(f'api_key = "{blob}"\n', encoding="utf-8")
    run_cmd(["git", "add", "-A"], cwd=project_path)
    result = run_cmd(["tox", "-e", "lint"], cwd=project_path, check=False)

    assert result.returncode != 0
    assert any(word in result.stdout.lower() for word in ["gitleaks", "leak", "secret"])
