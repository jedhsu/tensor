"""

    *Boolean All*

"""

import jax.numpy as jnp

from ._operator import BooleanOperator

__all__ = ["BooleanAll"]


class BooleanAll(
    BooleanOperator,
):
    operator = jnp.all

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(BooleanAll, self).__init__(
            *args,
            **kwargs,
        )
