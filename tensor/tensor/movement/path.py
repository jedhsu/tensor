"""

    *Movement Path*

  An exact movement.

"""

from dataclasses import dataclass
from typing import Sequence

__all__ = ["MovementPath"]


@dataclass
class MovementPath(
    tuple[int],
):
    def __init__(
        self,
        values: Sequence[int],
    ):
        super(MovementPath, self).__new__(
            tuple,
            values,
        )

    @classmethod
    def create(
        cls,
        *value: int,
    ):
        return cls([*value])
