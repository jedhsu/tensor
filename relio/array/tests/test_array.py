import jax.numpy as jnp

from ..array import *
from ..base import *


# class TestDeviceArray:
#     def test_new(self):
#         arr = DeviceArray(i32, (5, 5), jnp.zeros)

#         assert arr._arr[0, 0] == 0
#         assert isinstance(arr, DeviceArray)


class TestArray:
    def test_init(self):
        arr = Array(i32, (5, 6), jnp.zeros)

        assert arr.dtype == i32, dir(arr)

        assert isinstance(arr, Array)
        assert isinstance(arr, AbstractTypedArray)
        assert isinstance(arr, AbstractArray)
        assert isinstance(arr._arr, jnp.ndarray)


class TestBuild:
    def test_build_abstract_typed(self):
        arr = Array[i32]

        assert arr == AbstractTypedArray(i32)

    def test_build_abstract(self):
        arr = Array[i32][5, 7]

        assert arr == AbstractArray(i32, (5, 7))


#     def test_mro(self):
#         assert Array.__mro__[:5] == (
#             Array,
#             AbstractArray,
#             AbstractTypedArray,
#             AbstractSizedArray,
#             DeviceArray,
#         )
