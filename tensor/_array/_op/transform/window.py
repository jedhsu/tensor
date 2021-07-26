"""

Frequency / window / fft operators.

"""


import jax.numpy as jnp

from .base import ArrayTransform


class Window(ArrayTransform):
    """
    Window functions.

    """

    Bartlett = jnp.bartlett
    Blackman = jnp.blackman
    Hamming = jnp.hamming
    Hanning = jnp.hanning
    Kaiser = jnp.kaiser
