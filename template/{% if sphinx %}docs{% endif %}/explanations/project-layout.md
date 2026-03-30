# Why the project uses a `src` layout

The generated project keeps importable code under `src/` instead of at the
repository root. This helps tests and local development behave more like an
installed package, which reduces surprises caused by accidentally importing the
working tree directly.

It also keeps packaging metadata, tests, documentation, and source code clearly
separated, which makes the repository easier to navigate as the project grows.
