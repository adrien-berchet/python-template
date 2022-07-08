# Neuromath cookiecutter template

## Usage

### Dependencies

Before you can use this template you need to install cookiecutter:
```bash
pip install cookiecutter
```

### Running

This template can be used in two ways:

1. remotely:
   ```bash
   cookiecutter git@bbpgitlab.epfl.ch:neuromath/cookiecutter-python.git
   ```

2. locally:
   1. clone this template in a directory:
      ```bash
      git clone git@bbpgitlab.epfl.ch:neuromath/cookiecutter-python.git
      ```
   2. then run cookiecutter:
      ```bash
      cookiecutter <path-to-the-template-directory>
      ```

Then in the two cases you just have to answer to the prompted questions and the new package
directory will be automatically created afterwards.

Note: You can also use [cruft](https://cruft.github.io/cruft) to create the new project so it will
be easier to update it according to template change in the future.

### Post cookiecutting steps

After cookie-cutting a new repository, you have manual steps to perform:

1. complete Spack recipe in `extra/spack` and add it to BlueBrain Spack repo:
   https://github.com/BlueBrain/spack#the-bluebrain-spack-deployment
2. the `extra` folder can now be removed
3. search for `TODO` strings in the repository and replace them by what you need

### Using cruft to open source an existing package

Whether you did or did not use [cruft](https://cruft.github.io/cruft) to create your project, you
have to (re)link it to the template first (even if you used it to create the project you should
re-link in order to regenerate all the variables). This can be achieved using the following command:
```bash
cruft link git@bbpgitlab.epfl.ch:neuromath/cookiecutter-python.git
```
or
```bash
cruft link <path-to-the-template-directory>
```
if you have the template locally.
In the prompts, select `Github` as repository destination.

After that, it is possible to check what should be changed in the repository to make it (almost)
ready for open sourcing.
Then you can run the command:
```bash
cruft diff
```
to see what should be changed.
