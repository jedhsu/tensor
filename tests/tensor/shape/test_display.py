"""

    *Display,   [Unit Tests]*

"""

from tensor.tensor.shape.display import Test
from tensor.tensor.shape.display import Display


class TestDisplay:
    def test_vector(self):
        assert repr(Display.create(5)) == Test.vector()

    def test_grid(self):
        assert repr(Display.create(5, 5)) == Test.grid()

    def test_threetope(self):
        assert repr(Display.create(5, 5, 5)) == Test.threetope()
