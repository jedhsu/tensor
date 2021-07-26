"""

    *Topology*

  Give some comments on topology in lens of category theory.

"""

from abc import ABCMeta
from abc import abstractmethod

import numpy as np

from .._tensor import Coordinate

__all__ = ["Topology"]


class Topology(
    np.array,
):
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_open(self) -> bool:
        """
        Describe the conditions to be an open set.

        Note that you can only use bool, which is what is evaluated to...

        What exactly are these fundamental elements?

        # [TODO] use category theory to prove equivalence.

        """
        pass
