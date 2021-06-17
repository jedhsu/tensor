import jax.numpy as jnp

from .base import ArrayOperator


class BooleanOperator(ArrayOperator):
    pass


class BooleanUnaryOperator(
    BooleanOperator,
    BinaryOperator,
):
    all = jnp.all
    alltrue = jnp.alltrue

    any = jnp.any  # jnp.sometrue is equivalent


class BooleanBinaryOperator(
    BooleanOperator,
    BinaryOperator,
):
    logical_and = jnp.logical_and
    # logical_not = jnp.logical_not
    logical_or = jnp.logical_or
    logical_xor = jnp.logical_xor
