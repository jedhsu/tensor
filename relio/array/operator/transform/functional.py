import jax.numpy as jnp

from .base import ArrayTransform


class FunctionalTransform(ArrayTransform):
    """
    Functional transforms.

    """

    Positive = jnp.positive  # y = +x
    Negative = jnp.negative  # y = -x
    Sign = jnp.sign
    Heaviside = jnp.heaviside  # [TODO] does ths really go here??

    ModifiedBessel0 = jnp.i0
