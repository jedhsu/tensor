"""

    *Axis Orientation,   [Unit Tests]*

"""
from tensor.tensor.coordinate.system.axis.orientation import AxisOrientation


class TestAxisOrientation:
    def test_init(self):
        a = AxisOrientation(-3, -1)
        assert isinstance(a, AxisOrientation)
        assert a.origin == -3
        assert a.direction == -1

    def test_orient(self):
        a = AxisOrientation(-3, -1)
        a.orient(3, 1)
        assert a.origin == 3
        assert a.direction == 1
        a.orient(5, -1)
        assert a.origin == 5
        assert a.direction == -1
