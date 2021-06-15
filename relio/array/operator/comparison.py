import jax.numpy as jnp

from .base import ArrayOperator


class ComparisonOperator(ArrayOperator):
    """
    Element-wise comparison operators.

    """

    equal = jnp.equal
    isclose = jnp.isclose

    greater = jnp.greater
    greater_equal = jnp.greater_equal

    lesser = jnp.less
    lesser_equal = jnp.less_equal

    where = jnp.where  # predicate evaluation

    allclose = jnp.allclose  # element-wise equality within tolerance
