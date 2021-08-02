"""

    *Index Tensor,   [Unit Tests]*

"""

from tensor.tensor.index import IndexTensor
from tensor.tensor.index import CellIndex
from tensor.tensor.index import Test


class TestIndexTensor:
    def test_init_and_create(self):
        tensor = Test.square
        assert isinstance(tensor, IndexTensor)
        assert len(tensor.cells) == 9
        assert tensor.focus.index == CellIndex(0, 0)

    def test_getitem(self):
        tensor = Test.square
        assert tensor[0, 0].index == CellIndex(0, 0)
