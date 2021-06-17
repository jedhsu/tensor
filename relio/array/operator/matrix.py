"""

Matrix arithmetic operators.

"""

import jax.numpy as jnp

from .base import ArrayOperator

# [TODO] name is meh, arithmetic?


class MatrixArithmeticOperator(ArrayOperator):
    MatrixProduct = jnp.matmul

    DotProduct = jnp.dot
    CrossProduct = jnp.cross

    OuterProduct = jnp.outer
    InnerProduct = jnp.inner

    TensorProduct = jnp.tensordot  # [TODO] clarify

    KroneckerProduct = jnp.kron

    VectorProduct = jnp.vdot  # [TODO] ???
