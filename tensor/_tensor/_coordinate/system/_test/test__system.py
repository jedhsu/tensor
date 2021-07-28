"""

    *Coordinate System,   [Unit Tests]*

"""

from .._system import Axis
from .._system import CoordinateSystem


class TestCoordinateSystem:
    def test_init(self):
        a = CoordinateSystem(3)
        assert len(a.axes) == 3
        assert a.axes[0] == Axis(0, 0, 1)
        assert a.axes[1] == Axis(1, 0, 1)
        assert a.axes[2] == Axis(2, 0, 1)

    def test_orient(self):
        a = CoordinateSystem(3)
        a.orient(
            (
                (3, -1),
                (4, 1),
                (2, -1),
            )
        )
        assert a.axes[0].ordinal == 0
        assert a.axes[0].origin == 3
        assert a.axes[0].direction == -1

        assert a.axes[1].ordinal == 1
        assert a.axes[1].origin == 4
        assert a.axes[1].direction == 1

        assert a.axes[2].ordinal == 2
        assert a.axes[2].origin == 2
        assert a.axes[2].direction == -1
