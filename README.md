# actions-test-python
Testing out GitHub actions with a minimal Python package

Currently implements two actions:
* On any PUSH:

   Run flake8 linting and then any available tests with Pytest
* On new RELEASE:

   Build the package and upload to PyPi test
