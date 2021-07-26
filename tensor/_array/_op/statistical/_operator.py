"""

    *Statistical Inference*

  Operators of statistical types.

"""

from abc import ABCMeta
from .._operator import ArrayOperator

__all__ = ["StatisticalOperator"]


class StatisticalOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
