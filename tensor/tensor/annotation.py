"""

    *Tensor,   [Annotation]*

"""

from typing import Union

from .._datatype import Datatype
from ._tensor import Tensor
from ._shape import Shape

__all__ = ["Annotation"]


class Annotation(
    Tensor,
):
    @classmethod
    def __class_getitem__(
        cls,
        item: Union[Datatype, tuple[int]],
    ) -> Union[Datatype, tuple[int]]:
        return item
