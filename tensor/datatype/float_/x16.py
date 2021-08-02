"""

    *f16*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._float import Float

__all__ = ["f16"]


class f16(
    jnp.float16,
    Float,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(f16, self).__init__(
            self,
            value,
        )
