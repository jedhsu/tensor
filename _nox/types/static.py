"""

    *static-types*

  Check for well-typedness through _mypy_.

"""

from nox_poetry import Session
from nox_poetry import session

from .._nox import python_versions


@session(
    python=python_versions,
)
def mypy(
    session: Session,
) -> None:
    args = session.posargs or [
        "src",
        "tests",
        "docs/conf.py",
    ]
    session.install(".")
    session.install(
        "mypy",
        "pytest",
    )
    session.run(
        "mypy",
        *args,
    )
    if not session.posargs:
        session.run(
            "mypy",
            f"--python-executable={sys.executable}",
            "noxfile.py",
        )
