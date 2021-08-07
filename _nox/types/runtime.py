"""

    *runtime-types*

  Checks for type safety at runtime with _typeguard_.

"""

from nox_poetry import Session
from nox_poetry import session

from .._nox import python_versions
from .._nox import package


@session(
    python=python_versions,
)
def typeguard(
    session: Session,
):
    session.install(".")
    session.install(
        "pytest",
        "typeguard",
        "pygments",
    )
    session.run(
        "pytest",
        f"--typeguard-packages={package}",
        *session.posargs,
    )
