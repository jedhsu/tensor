import jax.numpy as jnp

from .base import ArrayTransform


class Reflection(ArrayTransform):
    flip = jnp.flip  # flip along axis
    flipud = jnp.flipud  # flips up/down
    fliplr = jnp.fliplr  # flip left/right
