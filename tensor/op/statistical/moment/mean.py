"""

    *Mean Inferece*

"""

import jax.numpy as jnp

from ._operator import StatisticalInference

__all__ = ["MeanInference"]


class MeanInference(
    StatisticalInference,
):
    fn = jnp.mean

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(MeanInference, self).__init__(
            *args,
            **kwargs,
        )
