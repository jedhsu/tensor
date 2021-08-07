"""

    *examples*

  Run examples with xdoctest.

"""

from nox_poetry import Session
from nox_poetry import session


@session(
    python=python_versions,
)
def examples(
    session: Session,
) -> None:
    args = session.posargs or ["all"]
    session.install(".")
    session.install("xdoctest[colors]")
    session.run(
        "python",
        "-m",
        "xdoctest",
        package,
        *args,
    )
