"""

    *Bitwise Arithmetic Operator*

  A bitwise elemental arithmetic operator.

"""

from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["ComputationalOperator"]


class ComputationalOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
