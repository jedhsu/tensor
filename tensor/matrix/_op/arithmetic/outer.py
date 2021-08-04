"""

    *Outer Product*

"""

from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import MatrixArithmetic

__all__ = ["OuterProduct"]


@dataclass
class OuterProduct(
    MatrixArithmetic,
):
    operator = jnp.outer
