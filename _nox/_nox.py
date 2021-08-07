"""

    *nox*

  Parameters for nox.

"""

import nox

__all__ = [
    "nox",
    "python_versions",
]


package = "{{cookiecutter.package_name}}"
python_versions = [
    "3.9",
    "3.8",
    "3.7",
]
nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "pre-commit",
    "safety",
    "mypy",
    "tests",
    "typeguard",
    "xdoctest",
    "docs-build",
)
