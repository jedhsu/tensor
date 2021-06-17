"""

Type conversion / casting operators.

"""

import jax.numpy as jnp

from .base import ArrayOperator


class CastingOperator(ArrayOperator):
    """
    Type promotion and demotion.

    """

    Promote = jnp.promote_types

    EulerGamma = jnp.euler_gamma  # [TODO] clarify

    BitIntoU8 = jnp.packbits  # [TODO] clarify
