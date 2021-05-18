from __future__ import annotations
from typing import Sequence

from .dtype import *

__all__ = ["AbstractSizedArray"]


class _Default_:
    @staticmethod
    def _1d():
        return AbstractSizedArray((5,))

    @staticmethod
    def _2d_square():
        return AbstractSizedArray((5, 5))

    @staticmethod
    def _2d_rect():
        return AbstractSizedArray((5, 10))

    @staticmethod
    def _3d_cube():
        return AbstractSizedArray((5, 5, 5))


class _Eq_:
    dim: Sequence[int]

    def __eq__(self, arr: AbstractSizedArray) -> bool:
        return self.dim == arr.dim


class AbstractSizedArray(_Default_, _Eq_):
    dim: Sequence[int]

    def __init__(self, dim: Sequence[int], *args, **kwargs):
        self.dim = dim
        super(AbstractSizedArray, self).__init__(*args, **kwargs)

    def _repr_dim(self) -> str:
        string = repr(self.dim)[1:-1]
        return string if len(self.dim) > 1 else string[:-1]

    def __repr__(self):
        return f"AbstractSizedArray[{self._repr_dim()}]"
