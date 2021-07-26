"""

    *Index,   [Add]*

"""

from ._index import Index

__all__ = ["Add"]


class Add(
    Index,
):
    def __add__(
        self,
        change: tuple[int],
    ):
        position = [a + b for a, b in zip(self, change)]
        return Index(
            self.tensor,
            *position,
        )
