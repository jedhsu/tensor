"""

    *Coordinate System,   [Fix Interface]*

  Fixes the system's frame of reference.

  This constructs a new coordinate system.

"""

from .._coordinate import Coordinate
from ._system import CoordinateSystem

__all__ = ["Fix"]


class Fix(
    CoordinateSystem,
):
    def fix(
        self,
        origin: Coordinate,
    ):
        # [TODO] feels like easy reference issues here
        for ordinal in range(len(origin)):
            self.axes[ordinal].origin = origin[ordinal]
