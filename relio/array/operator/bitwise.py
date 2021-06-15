import jax.numpy as jnp

from .base import ArrayOperator


class BitwiseOperator(ArrayOperator):
    bitwise_and = jnp.bitwise_and
    # bitwise_not = jnp.bitwise_not
    bitwise_or = jnp.bitwise_or
    bitwise_xor = jnp.bitwise_xor
