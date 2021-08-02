"""

    *Cell,   [Bindings]*

"""

from ._cell import Cell as _Cell

from .move import Move

__all__ = ["Cell"]


class Cell(
    Move,
    _Cell,
):
    pass
