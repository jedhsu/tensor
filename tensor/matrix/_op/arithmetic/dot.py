"""

    *Dot Product*

"""

from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import MatrixArithmetic

__all__ = ["DotProduct"]


@dataclass
class DotProduct(
    MatrixArithmetic,
):
    operator = jnp.dot
