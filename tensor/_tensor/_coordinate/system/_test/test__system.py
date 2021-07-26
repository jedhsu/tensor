"""

    *Coordinate System,   [Unit Tests]*

"""

from .._system import CoordinateSystem


class TestCoordinateSystem:
    def test_init(self):
        a = CoordinateSystem(5, 10)
        assert len(a.axes) == 2
        assert a.axes[0] == 
