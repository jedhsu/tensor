from __future__ import annotations
from typing import Callable, GenericAlias, Optional, Sequence

import jax.numpy as jnp

from .base import AbstractArray, AbstractTypedArray, Dtype, i16

# from .fn import Fn


__all__ = ["Array"]


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


class DeviceArray(AbstractArray):
    def __init__(
        self,
        dtype: Dtype,
        dim: Sequence[int],
        constructor: Callable,
        populator: Optional[Sequence] = None,
    ):
        self._arr = constructor(shape=dim, dtype=dtype.value)
        if populator:
            self._arr = populator
        super(DeviceArray, self).__init__(dtype, dim)


class Array(
    DeviceArray,
    _Default_,
    _Display_,
):
    def __init__(
        self,
        dtype: Dtype,
        dim: Sequence[int],
        constructor: Callable,
        populator: Optional[Sequence] = None,
    ):
        super(Array, self).__init__(dtype, dim, constructor, populator)

    __class_getitem__ = classmethod(AbstractTypedArray)


#     def __init__(self):
#         jnp.zeros(self.dim, self.dtype)
# super(Array, self).__new__(self, builder)
