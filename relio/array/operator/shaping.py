"""

Shaping operators.

"""


import jax.numpy as jnp

from .base import ArrayOperator

# [TODO] is broadcasting this? (or unique because of view concept?)
# [TODO] where does transpose go?


class Count(AxisOperator, ShapingOperator):
    """
    Number of elements along an axis.

    """

    func = jnp.size


class ShapingOperator(ArrayOperator):
    Reshape = jnp.reshape

    AtLeast1D = jnp.atleast_1d
    AtLeast2D = jnp.atleast_2d
    AtLeast3D = jnp.atleast_3d

    Roll = jnp.roll

    Squeeze = jnp.squeeze

    Transpose = jnp.transpose


class Broadcast(ArrayOperator):
    BroadcastArrays = jnp.broadcast_arrays
    BroadcastShapes = jnp.broadcast_shapes
    BroadcastTo = jnp.broadcast_to


class Ravel:
    Ravel = jnp.ravel
    RavelMultiIndex = jnp.ravel_multi_index
    UnravelIndex = jnp.unravel_index


class Axis:
    NewAxis = jnp.newaxis
    MoveAxis = jnp.moveaxis
    RollAxis = jnp.rollaxis
    SwapAxes = jnp.swapaxes
