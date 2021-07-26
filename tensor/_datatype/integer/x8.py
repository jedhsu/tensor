"""

    *i8*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._integer import Integer

__all__ = ["i8"]


class i8(
    jnp.uint8,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(i8, self).__init__(
            self,
            value,
        )
