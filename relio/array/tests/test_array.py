import jax.numpy as jnp

from ..array import *
from ..dtype import *


class TestDeviceArray:
    def test_new(self):
        arr = DeviceArray(i32, (5, 5), jnp.zeros)

        assert arr._arr[0, 0] == 0
        assert isinstance(arr, DeviceArray)


class TestArray:
    def test_init(self):
        arr = Array(i32, (5, 6), jnp.zeros)

        assert arr.dtype == i32, dir(arr)

        assert isinstance(arr, Array)
        assert isinstance(arr, AbstractTypedArray)
        assert isinstance(arr, AbstractArray)

    def test_mro(self):
        assert Array.__mro__[:5] == (
            Array,
            AbstractArray,
            AbstractTypedArray,
            AbstractSizedArray,
            DeviceArray,
        )
