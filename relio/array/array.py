from __future__ import annotations
from typing import Callable, GenericAlias, Sequence

import jax.numpy as jnp

from .dtype import *
from .fn import Fn

# TODO: AbstractSizedArray and AbstractTypedArray can be generalized to Sized and ContainerTyped
class AbstractSizedArray:
    dim: Sequence[int]

    def __init__(self, dim: Sequence[int], *args, **kwargs):
        self.dim = dim
        super(AbstractSizedArray, self).__init__(*args, **kwargs)


class AbstractTypedArray:
    dtype: Dtype

    def __init__(self, dtype: Dtype, *args, **kwargs):
        self.dtype = dtype
        super(AbstractTypedArray, self).__init__(*args, **kwargs)

    __class_getitem__: classmethod


class AbstractArray(AbstractTypedArray, AbstractSizedArray):
    def __init__(self, dtype: Dtype, dim: Sequence[int], *args, **kwargs):
        super(AbstractArray, self).__init__(dtype, dim, *args, **kwargs)


def declare_size(cls, size):
    return AbstractArray


AbstractTypedArray.__class_getitem__ = classmethod(declare_size)


class DeviceArray:
    def __init__(
        self,
        dtype: Dtype,
        dim: Sequence[int],
        constructor: Callable,
    ):
        self._arr = constructor(shape=dim, dtype=dtype.value)
        super(DeviceArray, self).__init__()


class Array(AbstractArray, DeviceArray):
    def __init__(
        self,
        dtype: Dtype,
        dim: Sequence[int],
        builder: Callable,
    ):
        super(Array, self).__init__(dtype, dim, jnp.zeros)

    __class_getitem__ = classmethod(AbstractTypedArray)


#     def __init__(self):
#         jnp.zeros(self.dim, self.dtype)
# super(Array, self).__new__(self, builder)
