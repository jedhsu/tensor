from ._operator import Logarithm

from .natural import NaturalLogarithm
from .bitwise import BitwiseLogarithm
from .denary import DenaryLogarithm


__all__ = [
    "Logarithm",
    "NaturalLogarithm",
    "BitwiseLogarithm",
    "DenaryLogarithm",
]


# class LogarithmicOperator(TranscendentalOperator):
#     Log1p = jnp.log1p
#     LogAddExp = jnp.logaddexp
#     LogAddExp2 = jnp.logaddexp2
