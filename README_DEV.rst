Developer Readme
================

The template should be updated whenever the default project structure or the
generated tooling changes.

Validation
----------

The repository-level test suite renders example projects from the local working
tree and validates that the generated projects can lint, type-check, package,
and build documentation.

Run the full suite with::

    tox

The canonical answers used by the tests live in ``example-answers.yml``.
Long-form repository documentation lives in ``docs/``.
