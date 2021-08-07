"""

    *Cumulative Difference*

"""

from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SetOperator

__all__ = ["OuterProduct"]


@dataclass
class CumulativeDifference(
    SetOperator,
):
    operator = jnp.ediff1d
