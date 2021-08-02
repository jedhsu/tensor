"""

    *Cell,   [Move Interface]*

  Modify the index of the array under a fixed coordinate system.

"""

from dataclasses import dataclass

from .._cell import Cell
from .movement import Movement

__all__ = ["Move"]


class Move(
    Cell,
):
    def move(
        self,
        *value: int,
    ) -> Cell:
        index = self.index + Movement.create(*value)
        return self.index.tensor[index]
