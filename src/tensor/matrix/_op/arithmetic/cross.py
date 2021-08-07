"""

    *Cross Product*

"""

from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import MatrixArithmetic

__all__ = ["CrossProduct"]


@dataclass
class CrossProduct(
    MatrixArithmetic,
):
    operator = jnp.cross
