import jax.numpy as jnp

from .base import TranscendentalOperator


__all__ = [
    "TrigonometricOperator",
    "TranscendentalOperator",
]


class TrigonometricOperator(TranscendentalOperator):
    sin = jnp.sin
    sinh = jnp.sinh

    cos = jnp.cos
    cosh = jnp.cosh

    tan = jnp.tan
    tanh = jnp.tanh


class InverseTrigonometricOperator(TranscendentalOperator):
    arcsin = jnp.arcsin
    arcsinh = jnp.arcsinh

    arccos = jnp.arccos
    arccosh = jnp.arccosh

    arctan = jnp.arctan
    arctan2 = jnp.arctan2  # [TODO] what is this
    arctanh = jnp.arctanh
