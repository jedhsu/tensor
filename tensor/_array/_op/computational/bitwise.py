"""

    *Bitwise Computational Operator*

  A bitwise computational operator.

"""

import jax.numpy as jnp

from ._operator import ComputationalOperator

__all__ = ["BitwiseComputationalOperator"]


class BitwiseComputationalOperator(
    ComputationalOperator,
):
    bitwise_and = jnp.bitwise_and
    # bitwise_not = jnp.bitwise_not
    bitwise_or = jnp.bitwise_or
    bitwise_xor = jnp.bitwise_xor
    bitwise_not = jnp.bitwise_not  # unary!
