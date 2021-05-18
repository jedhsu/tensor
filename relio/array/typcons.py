"""
Type constructor.
"""

from .base import AbstractArray, AbstractTypedArray


def declare_size(cls, size):
    return AbstractArray


AbstractTypedArray.__class_getitem__ = classmethod(declare_size)
