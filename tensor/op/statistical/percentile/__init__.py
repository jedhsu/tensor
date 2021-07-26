import jax.numpy as jnp

from .base import StatisticalOperator


class PercentileOperator(StatisticalOperator):
    max = jnp.max
    min = jnp.min
    median = jnp.median
    quantile = jnp.quantile
    percentile = jnp.percentile
