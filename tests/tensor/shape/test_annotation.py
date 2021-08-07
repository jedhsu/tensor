"""

    *Annotation,   [Unit Tests]*

"""
from tensor.tensor.shape.annotation import Annotation


class TestDisplay:
    def test_vector(self):
        assert Annotation[5] == (5,)

    def test_grid(self):
        assert Annotation[5, 5] == (5, 5)

    def test_threetope(self):
        assert Annotation[5, 5, 5] == (5, 5, 5)
