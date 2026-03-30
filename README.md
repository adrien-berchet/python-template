# Python repository template

This Copier template generates a modern Python library skeleton with optional
Sphinx documentation, selectable type-checking, GitHub/GitLab-aware repository
files, and a stronger default tooling baseline.

## Highlights

* Generic repository metadata instead of organization-specific defaults.
* Optional `docs_type` to generate either a Sphinx docs tree or a README-only project.
* Optional `type_checker` selection between `pyright` and `pyrefly`.
* Optional strict Pyright mode.
* Optional GitHub Renovate configuration.
* Optional GitHub Pages and container-publishing automation for GitHub-hosted projects.
* A `uv`-centric developer workflow for generated projects without requiring a committed `uv.lock`.
* Generated project validation with linting, packaging, tests, docs, and min-version checks.

## Documentation

Long-form template documentation lives under `docs/`:

* [Overview](docs/index.md)
* [Tutorials](docs/tutorials.md)
* [How-to Guides](docs/how-to.md)
* [Explanations](docs/explanations.md)

## Usage

### Dependencies

Before you can use this template you need to install `copier` and `jinja2-time`:
```bash
pip install copier copier-templates-extensions jinja2-time
```

### Running

This template can be used using the following commands:

```bash
copier copy --UNSAFE <template_repository> <new_project_directory>
```

Then you just have to answer to the prompted questions and the new package directory will be
automatically created afterwards.

The `--UNSAFE` flag is required because the template uses Jinja extensions and
post-generation tasks.

### Generated project options

During generation, the most important choices are:

1. `repository_provider`: `github` or `gitlab`
2. `docs_type`: `sphinx` or `README`
3. `type_checker`: `pyright` or `pyrefly`
4. `strict_typing`: enabled only when `type_checker=pyright`
5. `setup_renovate`: optional GitHub-only Renovate support


### Post generation steps

After generating a new repository, you still have a few manual steps to perform:

1. Search for `TODO` strings in the repository and replace them by what you need.
2. Review the generated metadata, URLs, and CI defaults.
3. Commit the generated project once it matches your needs.

## Template validation

The template repository includes its own validation suite. Run it with:

```bash
tox
```

The canonical render answers used by the tests live in `example-answers.yml`.

# Updating a project to a newer template version

A repository created with `Copier` can be easily updated according to the template using the
following command:
```bash
copier update
```
If you want to change one or several answers, you can remove the `--force` argument and then answer
the questions as usual. After that, you can check how your files were updated and then commit
these changes.


### Switching repository platforms

The `Copier` template can also help migrate a repository between the supported git platforms. From
the project directory, run the following command:

```bash
copier update
```

Then answer the questions and change the repository platform to the new value. The template should
create the missing files and overwrite the existing ones. Note that it may not remove files that
are no longer present in the template, so review the changes carefully before committing them.
