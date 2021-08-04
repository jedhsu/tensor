class Union(VectorOperator, BinaryOperator):
    """
    Set-wise union of two vectors.

    """

    func = jnp.union1d
