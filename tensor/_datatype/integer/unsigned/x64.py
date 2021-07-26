"""

    *u64*

"""

import jax.numpy as jnp

from ..._datatype import Datatype
from .._integer import Integer
from ._unsigned import Unsigned

__all__ = ["u64"]


class u64(
    jnp.uint64,
    Unsigned,
    Integer,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(u64, self).__init__(
            self,
            value,
        )
