# Design Principles

## Generic first

The template avoids organization-specific defaults and instead asks for the
minimum repository metadata needed to generate a good starting point for a new
project.

## Optional complexity

Features such as Sphinx docs, GitHub Pages deployment, Renovate, and container
publishing are available as options instead of being forced into every
generated project.

## Strong defaults with room to relax

Generated projects still get a modern baseline:

- strict linting and packaging checks
- explicit type-checker selection
- min-version compatibility validation
- documentation tooling that can be disabled for simpler libraries

## `uv` as workflow, not lockfile policy

The generated projects now prefer `uv` for developer workflows and GitHub
automation, while still remaining lockfile-free by default. That keeps the
template fast and modern without forcing a committed `uv.lock` into every
library repository.
