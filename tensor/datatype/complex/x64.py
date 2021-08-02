"""

    *c64*

"""

import jax.numpy as jnp

from .._datatype import Datatype
from ._complex import Complex

__all__ = ["c64"]


class c64(
    jnp.bool_,
    Complex,
    Datatype,
):
    def __init__(
        self,
        value: int,
    ):
        super(c64, self).__init__(
            self,
            value,
        )
