"""

    *Rotation*

"""

import jax.numpy as jnp

from _operator import Transform

__all__ = ["Rotation"]


class Rotation(
    Transform,
):
    rot90 = jnp.rot90
