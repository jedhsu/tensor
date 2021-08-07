"""

    *Matrix Operator*

  Maps to the same type.

"""

__all__ = ["MatrixMorphism"]

from .._operator import MatrixOperator


class MatrixMorphism(
    MatrixOperator,
):
    pass
