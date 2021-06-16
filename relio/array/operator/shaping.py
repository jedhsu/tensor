"""

Shaping operators.

"""


import jax.numpy as jnp

from .base import ArrayOperator

# [TODO] is broadcasting this? (or unique because of view concept?)
# [TODO] where does transpose go?


class ShapingOperator(ArrayOperator):
    Reshape = jnp.reshape

    AtLeast1D = jnp.atleast_1d
    AtLeast2D = jnp.atleast_2d
    AtLeast3D = jnp.atleast_3d

    Roll = jnp.roll

    Squeeze = jnp.squeeze


class Broadcast(ArrayOperator):
    BroadcastArrays = jnp.broadcast_arrays
    BroadcastShapes = jnp.broadcast_shapes
    BroadcastTo = jnp.broadcast_to
