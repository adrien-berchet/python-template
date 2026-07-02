# Feature Matrix

## Core options

- `docs_type=sphinx`: generate the Sphinx/MyST/Furo docs tree and docs tox env
- `docs_type=README`: keep the project lightweight and omit docs-specific files
- `type_checker=pyright`: generate Pyright config, with optional strict mode
- `type_checker=pyrefly`: generate Pyrefly config and tox wiring
- `use_uv_lock`: commit `uv.lock` and run generated automation in locked mode

## GitHub-only options

- `setup_renovate`: add Renovate configuration
- `setup_github_pages_docs`: add GitHub Pages docs publishing while keeping Read the Docs support
- `setup_container`: add container build/publish automation and container files

## Always-on GitHub behavior

GitHub-hosted projects also receive:

- issue and pull-request templates
- the main CI workflow
- release automation on version tags
- optional CodeQL when enabled in the questionnaire
