"""

    *build-with-view*

  Build and serve the documentation with live reloading on changes.

"""

import shutil
from pathlib import Path

from nox_poetry import Session
from nox_poetry import session


@session(
    python="3.9",
)
def docs(
    session: Session,
) -> None:
    args = session.posargs or [
        "--open-browser",
        "docs",
        "docs/_build",
    ]

    session.install(".")
    session.install(
        "sphinx",
        "sphinx-autobuild",
        "sphinx-click",
        "sphinx-rtd-theme",
    )

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run(
        "sphinx-autobuild",
        *args,
    )
