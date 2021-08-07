from __future__ import annotations
from typing import Callable, GenericAlias

from .dtype import *

__all__ = [
    "AbstractTypedArray",
    "_Build_",
]


class _Eq_:
    dtype: Dtype

    def __eq__(self, arr: AbstractTypedArray) -> bool:
        return self.dtype == arr.dtype


class _Default_:
    # TODO: class method works for cooperative but static typing obvously doesn't like it

    @staticmethod
    def u8():
        return AbstractTypedArray(u8)

    @staticmethod
    def u16():
        return AbstractTypedArray(u16)

    @staticmethod
    def i8():
        return AbstractTypedArray(i8)

    @staticmethod
    def i16():
        return AbstractTypedArray(i16)

    @staticmethod
    def f16():
        return AbstractTypedArray(f16)

    @staticmethod
    def f32():
        return AbstractTypedArray(f32)


class _Build_:
    dtype: Dtype
    __getitem__: Callable


class _Annotated_:
    """Overloads for static type annotations."""

    __class_getitem__ = classmethod(GenericAlias)


class AbstractTypedArray(
    _Annotated_,
    _Build_,
    _Default_,
    _Eq_,
):
    dtype: Dtype

    def __init__(self, dtype: Dtype, *args, **kwargs):
        self.dtype = dtype
        super(AbstractTypedArray, self).__init__(*args, **kwargs)

    def _repr_dtype(self) -> str:
        return self.dtype.name

    def __repr__(self) -> str:
        return f"AbstractTypedArray[{self._repr_dtype()}]"
