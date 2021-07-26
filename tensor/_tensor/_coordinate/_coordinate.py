"""

    *Coordinate*

"""

from dataclasses import dataclass

from typing import Sequence


__all__ = ["Coordinate"]


@dataclass
class Coordinate(
    tuple[int],
):
    def __init__(
        self,
        values: Sequence[int],
    ):
        return super(Coordinate, self).__new__(
            tuple,
            values,
        )
