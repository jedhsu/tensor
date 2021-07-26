"""

    *Index*

  A fixed cell label expressing the one-to-one correspondence to the tensor.

"""

from dataclasses import dataclass

from typing import Sequence

from ..._shape import Shape
from ..._tensor import Tensor

__all__ = ["Index"]


@dataclass
class Index(
    tuple[int],
):
    tensor: Tensor
    shape: Shape

    def __init__(
        self,
        tensor: Tensor,
        shape: Shape,
        indices: Sequence[int],
    ):
        self.tensor = tensor
        self.shape = shape
        return super(Index, self).__new__(
            tuple,
            indices,
        )

    @classmethod
    def create(
        cls,
        tensor: Tensor,
        shape: Shape,
        *index: int,
    ):
        indices = [*index]
        return cls(
            tensor,
            shape,
            indices,
        )
