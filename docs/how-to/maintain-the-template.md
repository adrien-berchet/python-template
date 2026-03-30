# Maintain the Template Repository

## Run the validation suite

The template repository validates rendered projects instead of only linting the
template source itself.

```bash
tox
```

## Update the canonical render answers

The file `example-answers.yml` represents the reference render used by the
tests. Update it when:

- a new questionnaire option should be part of the default validation path
- a default changes in a way that should be reflected in the canonical project

## Add a new optional feature

When extending the template:

1. add the questionnaire option in `copier.yml`
2. gate the generated files or content on that option
3. add at least one render test for the enabled path
4. keep the default path in `example-answers.yml` explicit when it matters

## Keep generated-project docs and CI aligned

Changes to `pyproject.toml.jinja`, `tox.ini.jinja`, or workflow templates often
need matching updates in:

- generated README or contributing docs
- generated Sphinx pages
- Renovate action allowlists
- template self-tests
