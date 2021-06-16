import jax.numpy as jnp

from ..base import ArrayOperator


class DiscreteOperator(ArrayOperator):
    Around = jnp.around

    Floor = jnp.floor
    Ceiling = jnp.ceil

    # limit values in array
    Clip = jnp.clip

    # round to nearest integer towards zero
    Fix = jnp.fix

    Round = jnp.round
