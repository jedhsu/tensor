"""

    *f32*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._float import Float

__all__ = ["f32"]


class f32(
    jnp.float32,
    Float,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(f32, self).__init__(
            self,
            value,
        )
