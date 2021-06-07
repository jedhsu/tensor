"""

Random Variable / Stochastic.

"""

from typing import Generic, TypeVar

from .distribution import Distribution

T = TypeVar("T")


class RandomVariable(Generic[T], Distribution):
    pass


# -- Alias
Stochastic = RandomVariable
