from ..step import Step


class TestStep:
    def test_step(self):
        a = Step(1)
        assert a == 1

        assert isinstance(a, Step)
        assert isinstance(a, int)
