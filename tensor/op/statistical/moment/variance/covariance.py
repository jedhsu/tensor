"""

    *Covariance*

"""

import jax.numpy as jnp

from .._operator import StatisticalInference

__all__ = ["Covariance"]


class Covariance(
    StatisticalInference,
):
    fn = jnp.cov

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Covariance, self).__init__(
            *args,
            **kwargs,
        )
