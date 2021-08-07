import jax.numpy as jnp

from .array import Array
from .base.dtype import Dtype


class Matrix(Array[Dtype][int, int]):
    def __init__(self, dtype: Dtype, dim: tuple[int, int]):
        super(Matrix, self).__init__(dtype, dim, constructor=jnp.zeros)
