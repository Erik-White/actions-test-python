from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    python_requires = ">3.7",
    name = "actions-test-python",
    version = "0.0.1",
    description = "Testing out GitHub actions with a minimal Python package",
    long_description = long_description,
    url = "https://github.com/Erik-White/actions-test-python/",
    author = "Erik White",
    author_email = "",
    license = "GPL-3.0",
    packages = find_packages(),
    zip_safe = False,
    install_requires = [
        "numpy"
    ],
    extras_require = {
        "dev": [
            "check-manifest"
            "pytest",
            "pytest-cov"
        ],
        "test": [
            "pytest",
            "pytest-cov"
        ],
    },
    entry_points={
        'console_scripts': [
            'actions-test-python = src.main:main',
        ],
    },
)