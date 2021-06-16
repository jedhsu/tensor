import jax.numpy as jnp

from .base import NumericOperator


class ExponentialOperator(NumericOperator):
    Exp = jnp.exp
    Exp2 = jnp.exp2  # [TODO] clarify what this is

    ExpM1 = jnp.expm1

    LdExp = jnp.ldexp  # [TODO] clarify
    FrExp = jnp.frexp


class LogarithmicOperator(NumericOperator):
    Log = jnp.log
    Log2 = jnp.log2
    Log10 = jnp.log10
    Log1p = jnp.log1p

    LogAddExp = jnp.logaddexp
    LogAddExp2 = jnp.logaddexp2
