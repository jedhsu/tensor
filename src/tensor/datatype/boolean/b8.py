"""

    *b8*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._boolean import Boolean

__all__ = ["b8"]


class b8(
    jnp.bool_,
    Boolean,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(b8, self).__init__(
            self,
            value,
        )
