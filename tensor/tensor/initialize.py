"""

    *Tensor,   [Initialize Interface]*

"""

import numpy as np

from dataclasses import dataclass

from ._tensor import Tensor
from ._cell import Cell
from ._cell import Index

__all__ = ["Initialize"]


@dataclass
class Initialize(
    Tensor,
):
    _cells: dict[Index, Cell]

    def __init__(
        self,
        cells,
        *args,
        **kwargs,
    ):
        self.cells = cells
        super(Initialize, self).__init__(
            np.array(
                *args,
                **kwargs,
            )
        )


#     def __getitem__(
#         self,
#         index,
#     ):
#         return self._cells[index]
