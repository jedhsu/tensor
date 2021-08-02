"""

    *Tensor,   [Bindings]*

"""

from ._tensor import Tensor as _Tensor

from .initialize import Initialize

__all__ = ["Tensor"]


class Tensor(
    Initialize,
    _Tensor,
):
    pass
