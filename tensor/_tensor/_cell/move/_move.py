"""

    *Cell,   [Move Interface]*

  movement can later be generalized to other spaces!

"""

from dataclasses import dataclass

from typing import Sequence

from ._cell import Cell

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
