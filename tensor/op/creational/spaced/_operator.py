class ArraySpacedConstructor(ArrayOperator):
    """
    Constructors based on element-wise difference equation.

    """

    LinearSpaced = jnp.linspace
    GeometricSpaced = jnp.geomspace
    LogarithmicSpaced = jnp.logspace
