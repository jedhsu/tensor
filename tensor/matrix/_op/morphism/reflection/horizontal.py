"""

    *Horizontal Reflect*

"""

import jax.numpy as jnp

from ._operator import StatisticalInference

__all__ = ["HorizontalReflect"]


class MeanInference(
    StatisticalInference,
):
    fn = jnp.flipud

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(MeanInference, self).__init__(
            *args,
            **kwargs,
        )
