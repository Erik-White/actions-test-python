[![GitHub](https://img.shields.io/github/license/erik-white/actions-test-python?color=blue)](https://github.com/Erik-White/actions-test-python/blob/master/LICENSE)

# actions-test-python
Testing out GitHub actions with a minimal Python package

Currently implements two actions:
* On any PUSH:

   Run flake8 linting and then any available tests with Pytest
* On new RELEASE:

   Build the package and upload to PyPi test
* On any PUSH to the `docs` directory on `master`:

   Build the mkdocs static site and publish to the `gh-pages` branch

   Build the package and upload to PyPi test
