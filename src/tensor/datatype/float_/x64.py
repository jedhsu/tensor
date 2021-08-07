"""

    *f64*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._float import Float

__all__ = ["f64"]


class f64(
    jnp.float64,
    Float,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(f64, self).__init__(
            self,
            value,
        )
