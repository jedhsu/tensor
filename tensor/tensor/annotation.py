"""

    *Tensor,   [Annotation]*

"""

from typing import Union

from typing import TypeVar
from typing import Generic

from tensor.datatype import Datatype as _Datatype
from tensor.shape import Datatype as _Shape


from ..datatype import Datatype
from ._tensor import Tensor
from .shape import Shape

Datatype = TypeVar("Datatype", bound=_Datatype)
Shape = TypeVar("Shape", bound=_Shape)

__all__ = ["Annotation"]


class Annotation(
    Generic[Datatype, Shape],
    Tensor,
):
    @classmethod
    def __class_getitem__(
        cls,
        item: Union[Datatype, tuple[int]],
    ) -> Union[Datatype, tuple[int]]:
        return item
