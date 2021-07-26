"""

    *Cell*

  A tensor cell at a coordinate.

"""

from typing import Optional
from typing import Any

from .._coordinate import CoordinateSystem
from ._position import Position
from ._index import Index


class Cell(
    Position,
):
    index: Index
    value: Optional[Any] = None

    def __init__(
        self,
        index: Index,
        coordinate_system: CoordinateSystem,
    ):
        self.index = index
        super(Cell, self).__init__(
            coordinate_system,
        )

    def bind(
        self,
        value: Any,
    ):
        """
        Binds a value to the coordinate.

        """
        self.value = value
