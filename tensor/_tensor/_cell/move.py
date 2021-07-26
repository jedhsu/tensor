"""

    *Cell,   [Move Interface]*

  movement can later be generalized to other spaces!

"""

from dataclasses import dataclass

from typing import Sequence

from ._cell import Cell

__all__ = ["Move"]


@dataclass
class Movement(
    tuple[int],
):
    def __init__(
        self,
        values: Sequence[int],
    ):
        super(Movement, self).__new__(
            tuple,
            values,
        )

    @classmethod
    def create(
        cls,
        *value: int,
    ):
        return cls([*value])


class Move(
    Cell,
):
    def move(
        self,
        *value: int,
    ) -> Cell:
        index = self.index + Movement.create(*value)
        return self.index.tensor[index]
