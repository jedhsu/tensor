"""

    *Coordinate System*

"""

from typing import Sequence

from .._coordinate import Coordinate
from ._axis import Axis

__all__ = ["CoordinateSystem"]


class CoordinateSystem:
    axes: Sequence[Axis]

    def __init__(
        self,
        *size: int,
    ):
        self.axes = [Axis.create(size) for size in range(len([*size]))]

    def origins(self) -> Coordinate:
        return Coordinate([axis.origin for axis in self.axes])
