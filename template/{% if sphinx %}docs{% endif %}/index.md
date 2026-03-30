---
html_theme.sidebar_secondary.remove: true
---

```{include} ../README.md
:end-before: <!-- README only content
```

## How the documentation is structured

Documentation is split into four categories inspired by
[Diataxis](https://diataxis.fr).

::::{grid} 2
:gutter: 4

:::{grid-item-card} Tutorials
```{toctree}
:maxdepth: 2
tutorials
```
+++
Step-by-step guides for getting started and following common workflows.
:::

:::{grid-item-card} How-to Guides
```{toctree}
:maxdepth: 2
how-to
```
+++
Practical recipes for specific tasks once you know the basics.
:::

:::{grid-item-card} Explanations
```{toctree}
:maxdepth: 2
explanations
```
+++
Background material about the project structure and why it is organized that way.
:::

:::{grid-item-card} Reference
```{toctree}
:maxdepth: 2
reference
```
+++
API, CLI, and release information for day-to-day reference.
:::

::::
