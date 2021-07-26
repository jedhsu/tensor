import jax.numpy as jnp

from .base import StatisticalOperator


class CorrelationOperator(StatisticalOperator):
    CorrelationCoefficients = jnp.corrcoef
    Correlate = jnp.correlate
