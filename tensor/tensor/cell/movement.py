"""

    *Movement*

  movement can later be generalized to other spaces!

"""

from dataclasses import dataclass
from typing import Sequence

__all__ = ["CellMovement"]


@dataclass
class CellMovement(
    tuple[int],
):
    def __init__(
        self,
        values: Sequence[int],
    ):
        super(CellMovement, self).__new__(
            tuple,
            values,
        )

    @classmethod
    def create(
        cls,
        *value: int,
    ):
        return cls([*value])
