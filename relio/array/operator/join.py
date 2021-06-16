import jax.numpy as jnp

from .base import ArrayOperator


class Join(ArrayOperator):
    append = jnp.append  # Appends values to end of array

    Concatenate = jnp.concatenate


# [TODO] which one is vertical / horizontal


class Stack(Join):
    Stack = jnp.stack  # [TODO] clarify

    HorizontalStack = jnp.hstack
    VerticalStack = jnp.vstack
    DiagonalStack = jnp.dstack


# [TODO] belong?
class Split(Join):
    Split = jnp.split

    HorizontalSplit = jnp.hsplit
    VerticalSplit = jnp.vsplit
    DiagonalSplit = jnp.dsplit


class Vertical(Join):
    pass


class Horizontal(Join):
    pass
