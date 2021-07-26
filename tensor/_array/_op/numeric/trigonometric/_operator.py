"""

    *Trigonometric Operator*   :: Array[Angle] --> Array[Number]

  Operators that map angles to numbers.

"""

import jax.numpy as jnp

from .._operator import TranscendentalOperator

__all__ = ["TrigonometricOperator"]


class TrigonometricOperator(TranscendentalOperator):
    sin = jnp.sin
    sinh = jnp.sinh

    cos = jnp.cos
    cosh = jnp.cosh

    tan = jnp.tan
    tanh = jnp.tanh
