import jax.numpy as jnp

from .base import ArrayOperator


class Union(VectorOperator, BinaryOperator):
    """
    Set-wise union of two vectors.

    """

    func = jnp.union1d


class Union(VectorOperator, BinaryOperator):
    """
    Set-wise intersection of two vectors.

    """

    func = jnp.intersect1d


class CumulativeDifference(
    OffsetElementOperator,
    VectorOperator,
    UnaryOperator,
):
    func = jnp.ediff1d


class In(
    ComparisonOperator,
    BinaryOperator,
    VectorOperator,
):
    func = jnp.in1d


class Difference(
    BinaryOperator,
    VectorOperator,
):
    """
    Set-wise difference of a vector.

    """

    func = jnp.setdiff1d


class Xor(
    BinaryOperator,
    VectorOperator,
):
    """
    Set-wise exclusive or of a vector.

    """

    func = jnp.setxor1d
