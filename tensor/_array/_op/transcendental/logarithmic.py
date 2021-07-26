import jax.numpy as jnp

from .base import TranscendentalOperator


__all__ = ["LogarithmicOperator"]


class LogarithmicOperator(TranscendentalOperator):
    Log = jnp.log
    Log2 = jnp.log2
    Log10 = jnp.log10
    Log1p = jnp.log1p

    LogAddExp = jnp.logaddexp
    LogAddExp2 = jnp.logaddexp2
