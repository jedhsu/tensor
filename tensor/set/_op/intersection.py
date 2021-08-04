class Intersection(VectorOperator, BinaryOperator):
    """
    Set-wise intersection of two vectors.

    """

    func = jnp.intersect1d
