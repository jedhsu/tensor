"""

    *Coordinate,   [Unit Tests]*

"""

from tensor.tensor.coordinate._coordinate import Coordinate


class TestCoordinate:
    def test_init_and_create(self):
        a = Coordinate.create(20, 10, 5)
        assert a == (20, 10, 5)
        assert a[0] == 20
        assert a[1] == 10
        assert a[2] == 5
