"""

    *Index,   [Bindings]*

"""

from ._index import Index as _Index

from .bound import Bound
from .add import Add

__all__ = ["Index"]


class Index(
    Bound,
    Add,
    _Index,
):
    pass
