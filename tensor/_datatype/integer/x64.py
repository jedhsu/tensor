"""

    *i64*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._integer import Integer

__all__ = ["i64"]


class i64(
    jnp.uint64,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(i64, self).__init__(
            self,
            value,
        )
