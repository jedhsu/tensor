"""

    *u8*

"""

import jax.numpy as jnp

from ..._datatype import Datatype
from .._integer import Integer
from ._unsigned import Unsigned

__all__ = ["u8"]


class u8(
    jnp.uint8,
    Unsigned,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(u8, self).__init__(
            self,
            value,
        )
