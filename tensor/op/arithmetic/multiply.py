class Multiply(
    ElementOperator,
    BinaryOperator,
    ArrayOperator,
):
    """
    Element-wise multiplication.

    """

    func = jnp.multiply
