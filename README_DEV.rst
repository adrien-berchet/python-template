Developer Readme
================

The cookiecutter template should be updated whenever the standard project
configuration is modified, for example when new tools are adopted as
part of the developer workflow.

New versions of Sphinx
----------------------

In new versions of Sphinx, the ``sphinx-quickstart`` templates may be
updated. For example, many of the default settings were removed in
Sphinx version 2.x.x, which reduced the clutter in the ``conf.py``
and the ``Makefile`` a lot.

In order to make the upgrade process simpler, a utility has been
written which may be run with ``tox`` to make these changes.

A developer wishing to see the latest changes in the Sphinx default
templates should take the following steps:

#. Run ``tox -r -e update-docs`` to update the Sphinx files in the
   cookiecutter.
#. Run ``git diff`` to see changes and confirm that we want to
   include them in the cookiecutter.
#. Commit the changes and submit them for review.
