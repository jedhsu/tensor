import jax.numpy as jnp

from .base import ArrayOperator

# [TODO] typing can get much tighter


class ArrayConstructor(ArrayOperator):
    zeros = jnp.zeros
    ones = jnp.ones

    empty = jnp.empty
    full = jnp.full

    arange = jnp.arange

    Tile = jnp.tile

    Eye = jnp.eye

    Identity = jnp.identity

    # TODO: IDEALLY want Fn[N, Array[Dtype][N]]
    # arange: Callable[[N],


class ArrayRelativeConstructor(ArrayOperator):
    zeros_like = jnp.zeros_like
    ones_like = jnp.ones_like

    empty_like = jnp.empty_like
    full_like = jnp.full_like
