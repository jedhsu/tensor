import jax.numpy as jnp

from .base import ArrayOperator


class TrigOperator(ArrayOperator):
    sin = jnp.sin
    sinh = jnp.sinh

    cos = jnp.cos
    cosh = jnp.cosh

    tan = jnp.tan
    tanh = jnp.tanh


class InverseTrigOperator(ArrayOperator):
    arcsin = jnp.arcsin
    arcsinh = jnp.arcsinh

    arccos = jnp.arccos
    arccosh = jnp.arccosh

    arctan = jnp.arctan
    arctan2 = jnp.arctan2
    arctanh = jnp.arctanh
