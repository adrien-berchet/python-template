# Update an Existing Generated Project

Projects generated from Copier can be updated from a newer template revision.

## 1. Start from a clean working tree

Before updating, commit or stash any local work you do not want mixed into the
template update.

## 2. Run Copier update

From the generated project directory:

```bash
copier update --UNSAFE
```

If you want to revisit some answers while updating, omit `--defaults` and
respond to the prompts.

## 3. Review the result

Pay particular attention to:

- repository metadata and URL changes
- newly added workflows or optional files
- docs or CI changes caused by new questionnaire options

## 4. Re-run the project validation

After updating, run the generated project checks again:

```bash
tox
```
