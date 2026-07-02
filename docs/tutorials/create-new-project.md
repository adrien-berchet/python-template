# Create a New Project

This tutorial walks through the common path for creating a new repository from
the template.

## 1. Install Copier and the template extensions

```bash
python3 -m pip install copier copier-templates-extensions jinja2-time
```

## 2. Generate a new project

```bash
copier copy --UNSAFE <template_repository> <new_project_directory>
```

## 3. Answer the key questions

The most important decisions are usually:

- `repository_provider`: GitHub or GitLab
- `docs_type`: Sphinx or README-only
- `type_checker`: Pyright or Pyrefly
- `strict_typing`: only shown for Pyright
- `use_uv_lock`: whether to commit and enforce `uv.lock`
- `setup_renovate`, `setup_github_pages_docs`, and `setup_container`: optional GitHub extras

## 4. Review the generated project

Before the first commit:

- replace any remaining `TODO` markers
- review the generated URLs and CI defaults
- decide whether the default badges and issue templates fit the repository

## 5. Validate the generated project

The generated project includes `tox` environments for linting, packaging,
tests, type-checking, docs, and min-version validation:

```bash
tox
```
