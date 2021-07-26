"""

    *Index,   [Bound]*

"""

from typing import Sequence

from ._index import Index

__all__ = ["Bound"]


class Bound(
    Index,
):
    def bound(
        self,
        values: Sequence[int],
    ) -> Sequence[int]:
        """
        Make sure labels stay within bounds.

        """
        bounded = []
        for i, val in enumerate(values):
            val = max(0, val)
            val = min(val, self.shape[i])

            bounded.append(val)

        return bounded
