"""

    *Cell,   [Move Interface]*

  Modify the index of the array under a fixed coordinate system.

"""

from ._cell import Cell
from .movement import CellMovement

__all__ = ["Move"]


class Move(
    Cell,
):
    def move(
        self,
        *value: int,
    ) -> Cell:
        index = self.index + CellMovement.create(*value)
        return self.index.tensor[index]
