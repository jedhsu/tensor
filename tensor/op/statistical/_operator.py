"""

    *Statistical Inference*

  Operators performing statistical inference.

"""

from abc import ABCMeta
from .._operator import ArrayOperator

__all__ = ["StatisticalOperator"]


class StatisticalOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
