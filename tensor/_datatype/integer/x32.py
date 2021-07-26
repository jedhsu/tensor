"""

    *i32*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._integer import Integer

__all__ = ["i32"]


class i32(
    jnp.uint32,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(i32, self).__init__(
            self,
            value,
        )
