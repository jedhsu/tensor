"""

    *Index*

  A fixed cell label expressing the one-to-one correspondence to the tensor.

"""

from __future__ import annotations
from dataclasses import dataclass

from typing import Sequence

from ..coordinate import Coordinate
from ..shape import Shape
from .movement import CellMovement

__all__ = ["CellIndex"]


# this should be have a layer that is Point, because technically nto a coordinate


@dataclass
class CellIndex:
    coordinate: Coordinate

    def __init__(
        self,
        *coordinate: int,
    ):
        self.coordinate = Coordinate.create(*coordinate)

    def __getitem__(
        self,
        index: int,
    ):
        assert 0 <= index <= len(self.coordinate)
        return self.coordinate[index]

    def add(
        self,
        change: CellMovement,
        *,
        shape: Shape,
    ):
        position = self.bound([a + b for a, b in zip(self.coordinate, change)], shape)
        return CellIndex(*position)

    def bound(
        self,
        indices: Sequence[int],
        shape: Shape,
    ) -> Sequence[int]:
        """
        Make sure labels stay within bounds.

        """
        bounded = []
        for i, index in enumerate(indices):
            index = max(0, index)
            index = min(index, shape[i])
            bounded.append(index)
        return tuple(bounded)

    def __hash__(self) -> int:
        return int("".join([str(el) for el in self]))


class Test:
    middle = CellIndex(1, 1, 1)
