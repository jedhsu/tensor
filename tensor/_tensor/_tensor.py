"""

    *Tensor*

"""

import numpy as np

from dataclasses import dataclass

__all__ = ["Tensor"]


@dataclass
class Tensor:
    _tensor: np.ndarray

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self._tensor = np.array(
            *args,
            **kwargs,
        )
