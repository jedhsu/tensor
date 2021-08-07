"""

    *Tensor,   [Bindings]*

"""

from .index import IndexTensor
from .move import Move

from .initialize import Test as InitializeTest

__all__ = ["Tensor"]


class Tensor(
    Move,
    IndexTensor,
):
    pass


class Test:
    square = Tensor.create(InitializeTest.square)
    square_5x5 = Tensor.create(InitializeTest.square_5x5)
