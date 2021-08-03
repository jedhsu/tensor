"""

    *Move,   [Unit Tests]*

"""

import pytest

from tensor.tensor._bind import Test


class TestMove:
    def test_jump(self):
        tensor = Test.square_5x5
        assert tensor.focus == tensor[0, 0]
        tensor.jump(1, 1)
        assert tensor.focus == tensor[1, 1]
        tensor.jump(-1, 2)
        assert tensor.focus == tensor[0, 2]

        with pytest.raises(AssertionError):
            tensor.jump(0)
        with pytest.raises(AssertionError):
            tensor.jump(0, 1, 2)

    def test_step(self):
        pass
