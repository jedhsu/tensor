"""

    *Shape,   [Unit Tests]*

"""
from tensor.tensor.shape._shape import Shape
from tensor.tensor.shape._shape import Test


class TestShape:
    def test_vector(self):
        assert Test.vector() == Shape.create(5)
        assert Test.vector() == (5,)

    def test_grid(self):
        assert Test.grid() == Shape.create(5, 5)
        assert Test.grid() == (5, 5)

    def test_threetope(self):
        assert Test.threetope() == Shape.create(5, 5, 5)
        assert Test.threetope() == (5, 5, 5)
