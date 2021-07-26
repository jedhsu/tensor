"""

    *Axis,   [Unit Tests]*

"""

from .._axis import Axis


class TestAxis:
    def test_init(self):
        a = Axis(5, 0, False)
        assert isinstance(a, Axis)
        assert a.origin == 0
        assert a.flipped is False

    def test_create(self):
        a = Axis.create(5)
        assert a.origin == 0
        assert a.flipped is False

    def test_update(self):
        a = Axis(5, 0, False)
        a.update(-3)
        assert a.origin == 3
        assert a.flipped is True
