# Neuromath Python repository template

## Usage

### Dependencies

Before you can use this template you need to install `copier` and `jinja2-time`:
```bash
pip install copier copier-templates-extensions jinja2-time
```

### Running

This template can be used using the following commands:

```bash
copier copy --trust git@...:python-template.git <new_project_directory>
```

Then you just have to answer to the prompted questions and the new package directory will be
automatically created afterwards.

Note that the `--UNSAFE` parameter is only needed for `copier>=8`.


### Post generation steps

After generating a new repository, you have manual steps to perform:

1. complete Spack recipe in `extra/spack` and add it to BlueBrain Spack repo:
   https://github.com/BlueBrain/spack#the-bluebrain-spack-deployment
2. the `extra` folder can now be removed
3. search for `TODO` strings in the repository and replace them by what you need


# Updating a project to a newer template version

A repository created with `Copier` can be easily updated according to the template using the
following command:
```bash
copier update
```
If you want to change one or several answers, you can remove the `--force` argument and then answer
the questions as usual. After that, you can check how your files were updated and then commit
these changes.


### Open sourcing an existing package

The `Copier` template can be used to help migrating a repository from Gitlab to Github. From the
project directory, run the following command:

```bash
copier update
```

Then answer the questions and change the repository destination platform to the new value. Then the
new template should create the missing files and overwrite the existing ones. Note that it may not
remove the ones that are not present in the new template. After that, review the changes and commit
the new migrated project.
