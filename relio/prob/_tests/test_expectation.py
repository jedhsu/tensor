from ..expectation import Expectation


class TestExpectation:
    def test_class_getitem(self):
        a = Expectation[2 | 1]
