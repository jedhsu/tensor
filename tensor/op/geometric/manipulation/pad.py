"""

    *Pad*

"""

import jax.numpy as jnp

from ._operator import Manipulation

__all__ = ["Pad"]


class Pad(
    jnp.pad,
    Manipulation,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Pad, self).__init__(
            *args,
            **kwargs,
        )
