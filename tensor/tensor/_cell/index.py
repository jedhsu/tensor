"""

    *Index*

  A fixed cell label expressing the one-to-one correspondence to the tensor.

"""

from __future__ import annotations
from dataclasses import dataclass

from ..coordinate import Coordinate
from ..shape import Shape


__all__ = ["Index"]


# this should be have a layer that is Point, because technically nto a coordinate


@dataclass
class Index(
    Coordinate,
):
    _shape: Shape

    def __init__(
        self,
        index: tuple[int, ...],
        shape: Shape,
    ):
        self._shape = shape
        super(Index, self).__init__(
            index,
        )

    def __add__(
        self,
        change: Index,
    ):
        position = self.bound([a + b for a, b in zip(self, change)])
        return Index(tuple(position), self._shape)

    def bound(
        self,
        indices: list[int],
    ) -> list[int]:
        """
        Make sure labels stay within bounds.

        """
        indices = []
        for i, index in enumerate(indices):
            index = max(0, index)
            index = min(index, self._shape[i])
            indices.append(index)
        return indices
