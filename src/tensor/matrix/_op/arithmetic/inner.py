"""

    *Inner Product*

"""

from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import MatrixArithmetic

__all__ = ["InnerProduct"]


@dataclass
class InnerProduct(
    MatrixArithmetic,
):
    operator = jnp.inner
