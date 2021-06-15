import jax.numpy as jnp

from .base import ArrayTransform


class FunctionalTransform(ArrayTransform):
    """
    Functional transforms.

    """

    positive = jnp.positive  # y = +x
    negative = jnp.negative  # y = -x
    sign = jnp.sign
    heaviside = jnp.heaviside  # [TODO] does ths really go here??
