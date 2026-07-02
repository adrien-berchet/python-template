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

## `uv` without forcing lockfiles

The generated projects now prefer `uv` for developer workflows and GitHub
automation, while keeping committed `uv.lock` files optional. The default fits
library projects that need to validate their declared dependency ranges, and
applications can opt into locked CI when reproducible deployments matter more.
