from ..dtype import Dtype


class TestDtype:
    def test_init(self):
        assert Dtype.u8.name == "u8"


class TestDisplay:
    def test_repr(self):
        assert repr(Dtype.u8) == "Datatype[u8]"
