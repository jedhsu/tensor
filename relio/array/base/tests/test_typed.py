from ..dtype import *
from ..typed import *
from ..typed import _Default_, _Eq_


class TestAbstractTypedArray:
    def test_init(self):
        arr = AbstractTypedArray(i32)

        assert arr.dtype == i32
        assert isinstance(arr, AbstractTypedArray)

    def test_mro(self):
        assert AbstractTypedArray.__mro__ == (
            AbstractTypedArray,
            _Default_,
            _Eq_,
            object,
        )

    #     def test_declare_size(self):
    #         assert AbstractTypedArray[1, 2] == AbstractArray

    def test_eq(self):
        assert AbstractTypedArray(i32) == AbstractTypedArray(i32)

    def test_defaults(self):
        assert AbstractTypedArray.i16() == AbstractTypedArray(i16)

    def test_repr(self):
        assert repr(AbstractTypedArray(i32)) == "AbstractTypedArray[i32]"
