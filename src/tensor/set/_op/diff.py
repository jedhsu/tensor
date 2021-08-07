class Difference(
    BinaryOperator,
    VectorOperator,
):
    """
    Set-wise difference of a vector.

    """

    func = jnp.setdiff1d
