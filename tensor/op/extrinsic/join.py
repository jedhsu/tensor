"""

    *Join*

"""

import jax.numpy as jnp

from .._operator import ArrayOperator

__all__ = ["Join"]


class Join(ArrayOperator):
    append = jnp.append  # Appends values to end of array

    Concatenate = jnp.concatenate


# [TODO] which one is vertical / horizontal


class Stack(Join):
    Stack = jnp.stack  # [TODO] clarify

    HorizontalStack = jnp.hstack
    VerticalStack = jnp.vstack
    DiagonalStack = jnp.dstack

    # [TODO] clarify
    RowStack = jnp.row_stack
    ColumnStack = jnp.column_stack


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