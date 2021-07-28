"""

    *Boolean All*

"""

import jax.numpy as jnp

from ._operator import BooleanOperator

__all__ = ["BooleanAll"]


class BooleanAll(
    jnp.all,
    BooleanOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(BooleanAll, self).__init__(
            *args,
            **kwargs,
        )
