from __future__ import annotations
from typing import Callable, Optional, Sequence

import jax.numpy as jnp

from .base import AbstractArray, AbstractTypedArray, Dtype, i16

# from .fn import Fn


__all__ = ["Array"]


class _Array(AbstractArray):
    _arr: jnp.ndarray


#     def __init__(self, *args, **kwargs):
#         super(_Array, self).__init__(*args, **kwargs)


class _Display_:
    """Move to abstract, and give symbols."""

    def _build_display(self, cellwidth=2):
        ...

    def _build_row(self, row_index: int, cell_width=2):
        """
        Row index is the index of the matrix arity.
        """

    def _build_cell(self, cell_index):
        ...

    def display(self):
        ...


class _Default_:
    @staticmethod
    def i16_square():
        return Array(dtype=i16, dim=(3, 3), constructor=jnp.zeros)


class _Build_:
    # TODO: need to do some hacky shit for BOTH the constructor to work AND the typing hinting!
    @classmethod
    def __class_getitem__(cls, dtype: Dtype):
        return AbstractTypedArray(dtype)

    def __getitem__(self, dtype: Dtype):
        return AbstractTypedArray(dtype)


class Array(
    _Build_,
    _Default_,
    _Display_,
    _Array,
):
    _class_getitem__: classmethod

    def __init__(
        self,
        dtype: Dtype,
        dim: Sequence[int],
        constructor: Callable,
        populator: Optional[Sequence] = None,
    ):
        self._arr = constructor(shape=dim, dtype=dtype.value)

        if populator:
            self._arr[:] = populator

        super(Array, self).__init__(dtype, dim)


# Array.__class_getitem__ = classmethod(AbstractTypedArray)
# Array.__getitem__ =
# AbstractTypedArray.__class_getitem = classmethod(AbstractArray)


# #     def __init__(self):
# #         jnp.zeros(self.dim, self.dtype)
# # super(Array, self).__new__(self, builder)
