"""

    *security*

  Scans dependencies for insecure packages through _safety_.

"""

from nox_poetry import Session
from nox_poetry import session


@session(python="3.9")
def security(
    session: Session,
) -> None:
    requirements = session.poetry.export_requirements()
    session.install("safety")
    session.run(
        "safety",
        "check",
        "--full-report",
        f"--file={requirements}",
    )
