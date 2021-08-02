"""

    *Test Cell Index*

"""

from tensor.tensor.cell.index import Test
from tensor.tensor.cell.index import CellMovement
from tensor.tensor.cell.index import Shape
from tensor.tensor.cell.index import CellIndex


class TestCellIndex:
    def test_getitem(self):
        a = Test.middle
        assert a[1] == 1

    def test_add(self):
        a = Test.middle
        assert a.add(
            CellMovement.create(0, 3, 0), shape=Shape.create(2, 2, 2)
        ) == CellIndex(1, 2, 1)

        assert a.add(
            CellMovement.create(-1, 3, -3), shape=Shape.create(2, 2, 2)
        ) == CellIndex(0, 2, 0)

        # assert a + CellMovement.create(-1, 3, -3) == CellIndex.create(
        #     (0, 2, 0),
        #     (2, 2, 2),
        # )

    def test_bound(self):
        a = Test.middle
        assert a.bound((1, -2, 3), Shape.create(2, 2, 2)) == (1, 0, 2)

    def test_hash(self):
        a = CellIndex(0, 0, 0)
        b = CellIndex(0, 0, 0)
        assert a == b
