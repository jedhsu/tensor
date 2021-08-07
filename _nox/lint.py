"""

    *lint*

  Lint using pre-commit.

"""


from nox_poetry import Session
from nox_poetry import session

from .activate import activate


@session(
    name="pre-commit",
    python="3.9",
)
def lint(
    session: Session,
):
    args = session.posargs or [
        "run",
        "--all-files",
        "--show-diff-on-failure",
    ]
    session.install(
        "black",
        "darglint",
        "flake8",
        "flake8-bandit",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-rst-docstrings",
        "pep8-naming",
        "pre-commit",
        "pre-commit-hooks",
        "reorder-python-imports",
    )
    session.run("pre-commit", *args)
    if args and args[0] == "install":
        activate(session)
