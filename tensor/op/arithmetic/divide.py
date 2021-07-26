class Divide(
    ElementOperator,
    BinaryOperator,
    ArrayOperator,
):
    """
    Element-wise division.

    """

    func = jnp.divide
