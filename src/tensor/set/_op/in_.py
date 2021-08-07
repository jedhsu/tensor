class In(
    ComparisonOperator,
    BinaryOperator,
    VectorOperator,
):
    func = jnp.in1d
