"""

    *Position*

  Mutates when coordinate system is refixed.

"""

from dataclasses import dataclass
from typing import MutableSequence

from .._coordinate import CoordinateSystem

__all__ = ["Position"]


@dataclass
class Position(
    MutableSequence[int],
):
    # contains a reference to the coordinate system
    _coordinate_system: CoordinateSystem

    def __init__(
        self,
        system: CoordinateSystem,
    ):
        self._coordinate_system = system

    def __getitem__(
        self,
        ordinal: int,
    ):
        assert 0 <= ordinal < len(self._coordinate_system.axes), ValueError

        self._coordinate_system.axes[i]
