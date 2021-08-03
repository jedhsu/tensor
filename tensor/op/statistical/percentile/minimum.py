"""

    *Minimum*

"""

import jax.numpy as jnp

from ._operator import PercentileOperator

__all__ = ["Minimum"]


class Minimum(
    PercentileOperator,
):
    operator = jnp.minimum
