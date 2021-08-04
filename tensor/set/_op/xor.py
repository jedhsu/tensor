class Xor(
    BinaryOperator,
    VectorOperator,
):
    """
    Set-wise exclusive or of a vector.

    """

    func = jnp.setxor1d
