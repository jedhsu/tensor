"""

    *c128*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._complex import Complex

__all__ = ["c128"]


class c128(
    jnp.bool_,
    Complex,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(c128, self).__init__(
            self,
            value,
        )
