import jax.numpy as jnp

from .base import NumericOperator


class ExponentialOperator(NumericOperator):
    exp = jnp.exp
    exp2 = jnp.exp2  # [TODO] clarify what this is


class LogarithmicOperator(NumericOperator):
    log = jnp.log
    log10 = jnp.log10
    log1p = jnp.log1p
    log2 = jnp.log2
