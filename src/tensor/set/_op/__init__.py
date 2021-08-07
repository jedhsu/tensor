from ._operator import SetOperator

from .union import Union
from .intersection import Intersection
from .in_ import In
from .diff import Difference
from .cumdiff import CumulativeDifference

__all__ = [
    "SetOperator",
    "Union",
    "Intersection",
    "In",
    "Difference",
    "CumulativeDifference",
]
