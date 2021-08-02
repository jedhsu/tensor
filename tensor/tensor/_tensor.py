"""

    *Tensor*

"""

import numpy as np
from dataclasses import dataclass

from ._cell import Cell

__all__ = ["Tensor"]


@dataclass
class Tensor:
    _tensor: np.ndarray

    focused: Cell

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self._tensor = np.array(
            *args,
            **kwargs,
        )

    def __getitem__(
        self,
        size: int,
    ):
        return self._tensor[size]
