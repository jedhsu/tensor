from ..dtype import *
from ..sized import *
from ..sized import _Default_, _Eq_


class TestAbstractSizedArray:
    def test_init(self):
        arr = AbstractSizedArray((1, 2))

        assert arr.dim == (1, 2)
        assert isinstance(arr, AbstractSizedArray)

    def test_mro(self):
        assert AbstractSizedArray.__mro__ == (
            AbstractSizedArray,
            _Default_,
            _Eq_,
            object,
        )

        # TODO: was trying to be explicit on testing super calls
        # arr = AbstractSizedArray((1, 2))
        # assert 1 == 2, super(
        #     AbstractSizedArray, super(AbstractSizedArray, arr).__self__
        # ).__subclasshook__
        # assert super(AbstractSizedArray, arr).__self_class__ == object

    def test_eq(self):
        assert AbstractSizedArray((5, 3)) == AbstractSizedArray((5, 3))

    def test_defaults(self):
        assert AbstractSizedArray._1d() == AbstractSizedArray((5,))

    def test_repr(self):
        assert repr(AbstractSizedArray._1d()) == "AbstractSizedArray[5]"
        assert repr(AbstractSizedArray._2d_square()) == "AbstractSizedArray[5, 5]"
