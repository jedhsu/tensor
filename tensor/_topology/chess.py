"""

    *Chess Topology*

"""

from .._tensor import Coordinate
from ._topology import Topology

__all__ = ["ChessTopology"]


class ChessTopology(
    Topology,
):
    def neighborhood(self) -> set[Coordinate]:
        return
