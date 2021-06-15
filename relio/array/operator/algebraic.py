"""

Algebraic polynomial operators.

"""

import jax.numpy as jnp

from .base import ArrayOperator


class PolynomialOperator(ArrayOperator):
    """
    Polynomial operations.

    """

    # [TODO] clarify
    polyadd = jnp.polyadd
    polysub = jnp.polysub
    polymul = jnp.polymul

    polyder = jnp.polyder
    polyint = jnp.polyint
    polyval = jnp.polyval
