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


class Vertical(Join):
    pass


class Horizontal(Join):
    pass
