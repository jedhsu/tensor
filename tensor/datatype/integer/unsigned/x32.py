"""

    *u32*

"""

import jax.numpy as jnp

from ..._datatype import Datatype
from .._integer import Integer
from ._unsigned import Unsigned

__all__ = ["u32"]


class u32(
    jnp.uint32,
    Unsigned,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(u32, self).__init__(
            self,
            value,
        )
