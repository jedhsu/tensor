"""

    *Creational Operator*   S -> Array[T, G]

  Operators that instantiate objects of the type.

"""

import jax.numpy as jnp

from .._operator import ArrayOperator

# [TODO] typing can get much tighter


class CreationalOperator(ArrayOperator):
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


class ArraySpacedConstructor(ArrayOperator):
    """
    Constructors based on element-wise difference equation.

    """

    LinearSpaced = jnp.linspace
    GeometricSpaced = jnp.geomspace
    LogarithmicSpaced = jnp.logspace


class ArrayRelativeConstructor(ArrayOperator):
    ZerosLike = jnp.zeros_like
    OnesLike = jnp.ones_like

    EmptyLike = jnp.empty_like
    FullLike = jnp.full_like
