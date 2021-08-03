"""

    *Horizontal Reflect*

"""

import jax.numpy as jnp

from ._operator import Reflect

__all__ = ["HorizontalReflect"]


class HorizontalReflect(
    Reflect,
):
    fn = jnp.flipud

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(HorizontalReflect, self).__init__(
            *args,
            **kwargs,
        )
