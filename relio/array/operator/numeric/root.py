import jax.numpy as jnp

from .base import NumericOperator


class Root(NumericOperator):

    CubeRoot = jnp.cbrt
