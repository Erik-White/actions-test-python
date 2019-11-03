import io
import re
from pathlib import Path
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        Path.joinpath(Path(__file__).parent, *names),
        encoding = kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


setup(
    python_requires = ">3.7",
    name = "actions_test_python",
    version = "0.0.1",
    description = "Testing out GitHub actions with a minimal Python package",
    long_description = "%s\n%s" % (
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", read("README.md")),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.md"))
    ),
    long_description_content_type = "text/markdown",
    url = "https://github.com/Erik-White/actions-test-python/",
    author = "Erik White",
    author_email = "",
    license = "GPL-3.0",
    packages = find_packages(where = "src", exclude = ["tests", "tests.*"]),
    package_dir = {"": "src"},
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
            'actions-test-python = actions_test_python.main:main',
        ],
    },
)