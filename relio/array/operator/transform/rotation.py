import jax.numpy as jnp

from .base import ArrayOperator


class Rotation(ArrayOperator):

    rot90 = jnp.rot90
