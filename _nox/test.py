"""

    *test*

  Runs the test suite with _pytest_.

"""


from nox_poetry import Session
from nox_poetry import session


@session(
    python=[
        "3.9",
        "3.8",
        "3.7",
    ]
)
def test(
    session: Session,
) -> None:
    session.install(".")
    session.install(
        "coverage[toml]",
        "pytest",
        "pygments",
    )
    try:
        session.run(
            "coverage",
            "run",
            "--parallel",
            "-m",
            "pytest",
            *session.posargs,
        )
    finally:
        if session.interactive:
            session.notify(
                "coverage",
                posargs=[],
            )
