"""

Abstract base types for Array, annotated for dtype and dimensions.

"""

from typing import Sequence

from . import typed
from .dtype import Dtype
from .sized import AbstractSizedArray
from .typed import AbstractTypedArray

__all__ = ["AbstractArray"]


class _From_:
    @staticmethod
    def from_abstract_typed(arr: AbstractTypedArray, dim: Sequence[int]):
        return AbstractArray(arr.dtype, dim)


class AbstractArray(
    AbstractTypedArray,
    AbstractSizedArray,
    _From_,
):
    def __init__(self, dtype: Dtype, dim: Sequence[int], *args, **kwargs):
        super(AbstractArray, self).__init__(dtype, dim, *args, **kwargs)

    # TODO: cooperatove class mechanism could be better here

    def __repr__(self) -> str:
        return f"AbstractArray[{self._repr_dtype()}][{self._repr_dim()}]"


typed._Build_.__getitem__ = _From_.from_abstract_typed
