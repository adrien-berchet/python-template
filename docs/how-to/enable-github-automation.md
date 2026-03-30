# Enable GitHub Automation Features

The template can optionally generate several GitHub-specific automations.

## GitHub Pages docs

Set `setup_github_pages_docs=yes` together with `docs_type=sphinx` to generate
the Pages deployment workflow. This is additive: `.readthedocs.yml` is still
generated, so the same project can also be published with Read the Docs.

## Renovate

Set `setup_renovate=yes` to generate `renovate.json`. The template keeps the
workflow-managed GitHub Actions pinned in Renovate so the template remains the
single source of truth for those actions.

## Container publishing

Set `setup_container=yes` to generate a `Dockerfile`, `.dockerignore`, and a
workflow that builds the image on pull requests and publishes tagged releases
to `ghcr.io/<owner>/<repo>`.

## Release automation

GitHub-hosted projects always receive the release workflow. Tagged releases:

- build the source and wheel artifacts
- publish them to PyPI
- create a GitHub release with the built artifacts attached
- optionally include a documentation zip when Sphinx docs are enabled
