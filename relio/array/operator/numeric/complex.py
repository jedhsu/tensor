"""
Operations on complex numbers.

"""

import jax.numpy as jnp

from .base import NumericOperator


class ComplexOperator(NumericOperator):
    Real = jnp.real
    Imaginary = jnp.imag
    Angle = jnp.angle  # angle of complex argument

    Conjugate = jnp.conj  # jnp.conjugate is alias
