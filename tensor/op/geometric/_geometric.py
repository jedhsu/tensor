"""

    *Geometric Operator*

"""

from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["GeometricOperator"]


class GeometricOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
