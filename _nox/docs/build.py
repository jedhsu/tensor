"""

    *docs-build*

  Build the docs.

"""

import shutil
from pathlib import Path

from nox_poetry import Session
from nox_poetry import session


@session(
    name="docs-build",
    python="3.9",
)
def docs_build(
    session: Session,
) -> None:
    """Build the documentation."""
    args = session.posargs or [
        "docs",
        "docs/_build",
    ]
    session.install(".")
    session.install(
        "sphinx",
        "sphinx-click",
        "sphinx-rtd-theme",
    )

    build_dir = Path(
        "docs",
        "_build",
    )
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run(
        "sphinx-build",
        *args,
    )
