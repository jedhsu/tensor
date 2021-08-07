"""

    *coverage*

  Analyzes code coverage with _coverage_.

"""

from pathlib import Path

from nox_poetry import Session
from nox_poetry import session


@session
def coverage(
    session: Session,
) -> None:
    args = session.posargs or ["report"]

    session.install("coverage[toml]")

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)
