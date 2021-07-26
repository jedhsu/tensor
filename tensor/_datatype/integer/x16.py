"""

    *i16*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._integer import Integer

__all__ = ["i16"]


class i16(
    jnp.uint16,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(i16, self).__init__(
            self,
            value,
        )
