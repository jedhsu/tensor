import jax.numpy as jnp

from ..array import *


class TestAbstractSizedArray:
    def test_init(self):
        arr = AbstractSizedArray((1, 2))

        assert arr.dim == (1, 2)
        assert isinstance(arr, AbstractSizedArray)

    def test_mro(self):
        assert AbstractSizedArray.__mro__ == (AbstractSizedArray, object)

        arr = AbstractSizedArray((1, 2))
        # assert 1 == 2, super(
        #     AbstractSizedArray, super(AbstractSizedArray, arr).__self__
        # ).__subclasshook__
        # assert super(AbstractSizedArray, arr).__self_class__ == object


class TestAbstractTypedArray:
    def test_init(self):
        arr = AbstractTypedArray(i32)

        assert arr.dtype == i32
        assert isinstance(arr, AbstractTypedArray)

    def test_mro(self):
        assert AbstractTypedArray.__mro__ == (AbstractTypedArray, object)

    def test_declare_size(self):
        assert AbstractTypedArray[1, 2] == AbstractArray


class TestAbstractArray:
    def test_init(self):
        arr = AbstractArray(i32, (1, 2))

        assert arr.dtype == i32
        assert arr.dim == (1, 2)

        assert isinstance(arr, AbstractArray)
        assert isinstance(arr, AbstractSizedArray)
        assert isinstance(arr, AbstractTypedArray)

    def test_mro(self):
        assert AbstractArray.__mro__ == (
            AbstractArray,
            AbstractTypedArray,
            AbstractSizedArray,
            object,
        )


class TestDeviceArray:
    def test_new(self):
        arr = DeviceArray(i32, (5, 5), jnp.zeros)

        assert arr._arr[0, 0] == 0
        assert isinstance(arr, DeviceArray)


class TestArray:
    def test_init(self):
        arr = Array(i32, (5, 6), jnp.zeros)

        assert 1 == 2, arr.__mro__
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
