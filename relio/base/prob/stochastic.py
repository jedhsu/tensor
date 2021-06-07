"""

A stochastic is a random variable.

"""

from typing import Generic, Mapping, TypeVar

from .probabilty import Probability

T = TypeVar("T")


class Stochastic(Generic[T]):
    pass


class SigmaAlgebra:
    pass


class EventSpace(
    SigmaAlgebra,
    set[Generic[T]],
):
    """
    Omega.

    """


class ProbabilityMeasure(
    Mapping[SigmaAlgebra, Probability],
):
    pass
