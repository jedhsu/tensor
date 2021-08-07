from ._operator import PercentileOperator

from .maximum import Maximum
from .minimum import Minimum
from .median import Median
from .quantile import Quantile
from .percentile import Percentile

__all__ = [
    "PercentileOperator",
    "Maximum",
    "Minimum",
    "Median",
    "Quantile",
    "Percentile",
]
