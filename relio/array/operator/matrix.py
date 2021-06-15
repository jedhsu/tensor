"""

Matrix arithmetic operators.

"""

import jax.numpy as jnp

from .base import ArrayOperator

# [TODO] name is meh, arithmetic?


class MatrixArithmeticOperator(ArrayOperator):
    DotProduct = jnp.dot
    CrossProduct = jnp.cross

    OuterProduct = jnp.outer
    InnerProduct = jnp.inner

    KroneckerProduct = jnp.kron
