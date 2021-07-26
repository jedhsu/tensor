"""

    *Coordinate System,   [Bindings]*

"""

from ._system import CoordinateSystem as _CoordinateSystem
from .fix import Fix

__all__ = ["CoordinateSystem"]


class CoordinateSystem(
    _CoordinateSystem,
    Fix,
):
    pass