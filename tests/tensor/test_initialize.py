"""

    *Initialize Tensor,   [Unit Tests]*

"""
from tensor.tensor.initialize import InitializeTensor
from tensor.tensor.initialize import Tensor
from tensor.tensor.initialize import Test


class TestInitializeTensor:
    def test_init_and_create(self):
        tensor = Test.square
        assert isinstance(tensor, InitializeTensor)
        assert isinstance(tensor, Tensor)
        assert tensor._tensor.shape == (3, 3)
        assert tensor._tensor[0][0] == 1
        assert tensor._tensor[2][2] == 9
