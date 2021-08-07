"""

    *u16*

"""

import jax.numpy as jnp

from ..._datatype import Datatype
from .._integer import Integer
from ._unsigned import Unsigned

__all__ = ["u16"]


class u16(
    jnp.uint16,
    Unsigned,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(u16, self).__init__(
            self,
            value,
        )
