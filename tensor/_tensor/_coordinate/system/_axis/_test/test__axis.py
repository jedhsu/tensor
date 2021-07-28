"""

    *Axis,   [Unit Tests]*

"""

from .._axis import Axis


class TestAxis:
    def test_init(self):
        a = Axis(5, 0, 1)
        assert isinstance(a, Axis)
        assert a.ordinal == 5
        assert a.origin == 0
        assert a.direction == 1

    def test_create(self):
        a = Axis.create(5)
        assert a.origin == 0
        assert a.direction == 1
