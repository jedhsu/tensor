"""

    *Tensor*

"""

import numpy as np
from dataclasses import dataclass

from .coordinate import CoordinateSystem


__all__ = ["Tensor"]


@dataclass
class Tensor:
    _tensor: np.ndarray
    coordinate_system: CoordinateSystem

    @classmethod
    def create(
        cls,
        *args,
        **kwargs,
    ):
        _tensor = np.array(
            *args,
            **kwargs,
        )
        coordinate_system = CoordinateSystem(dimensions=len(_tensor.shape))
        return cls(
            _tensor,
            coordinate_system,
        )
