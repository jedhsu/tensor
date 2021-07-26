"""

Probability distribution estimation.

"""

import jax.numpy as jnp

from .base import StatisticalOperator

# [TODO] meh... bad conceptual separation from percnetile


class Variance(
    StatisticalOperator,
    Extrinsic,
    Intrinsic,
):
    """
    Second moment.

    """

    # average = jnp.average  # mean
    var = jnp.var  # variance
    cov = jnp.cov  # covariance
    std = jnp.std  # standard deviation
