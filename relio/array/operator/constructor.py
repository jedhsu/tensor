import jax.numpy as jnp

from .base import ArrayOperator

# [TODO] typing can get much tighter


class ArrayConstructor(ArrayOperator):
    # low-level constructor
    Array = jnp.ndarray

    Zeros = jnp.zeros
    Ones = jnp.ones

    Empty = jnp.empty
    Full = jnp.full

    # TODO: IDEALLY want Fn[N, Array[Dtype][N]]
    # arange: Callable[[N],
    Range = jnp.arange

    Tile = jnp.tile

    Eye = jnp.eye

    Identity = jnp.identity


class ArrayRelativeConstructor(ArrayOperator):
    zeros_like = jnp.zeros_like
    ones_like = jnp.ones_like

    empty_like = jnp.empty_like
    full_like = jnp.full_like
