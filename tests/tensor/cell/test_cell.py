"""

    *Cell,   [Unit Tests]*

"""

from tensor.tensor.index import Test
from tensor.tensor.cell._cell import Cell
from tensor.tensor.cell._cell import Tensor
from tensor.tensor.cell._cell import CellIndex


class TestCell:
    def test_init(self):
        cell = Test.square[0, 0]
        assert isinstance(cell, Cell)
        assert isinstance(cell.tensor, Tensor)
        assert cell.index == CellIndex(0, 0)
