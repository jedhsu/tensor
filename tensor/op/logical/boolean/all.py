"""

    *Boolean All*

"""

import jax.numpy as jnp

from ._operator import BooleanOperator

__all__ = ["HyperbolicCosine"]


class BooleanAll(
    BooleanOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(HyperbolicCosine, self).__init__(
            *args,
            **kwargs,
        )
