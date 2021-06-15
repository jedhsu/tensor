"""

Type casting operators.

"""

import jax.numpy as jnp

from .base import ArrayOperator


class CastingOperator(ArrayOperator):
    """
    Type promotion and demotion.

    """

    promote_types = jnp.promote_types
