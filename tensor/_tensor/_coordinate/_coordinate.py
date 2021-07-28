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
        coordinates: Sequence[int],
    ):
        super(Coordinate, self).__new__(
            tuple,
            coordinates,
        )

    @classmethod
    def create(
        cls,
        *coordinate: int,
    ):
        return cls([*coordinate])
