"""

    *Cell*

  A tensor cell at a coordinate.

"""

from typing import Any

from ..coordinate import CoordinateSystem
from .position import Position
from .index import Index

__all__ = ["Cell"]


class Cell(
    Position,
):
    index: Index
    content: Any

    def __init__(
        self,
        index: Index,
        coordinate_system: CoordinateSystem,
    ):
        self.index = index
        super(Cell, self).__init__(
            coordinate_system,
        )
