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

### Post cookiecutting steps

After cookie-cutting a new repository, you have manual steps to perform:

1. complete Spack recipe in `extra/spack` and add it to BlueBrain Spack repo:
   https://github.com/BlueBrain/spack#the-bluebrain-spack-deployment
2. the `extra` folder can now be removed
3. search for `TODO` strings in the repository and replace them by what you need
