from __future__ import annotations

from ..state import State

__all__ = ["Reward"]


class _From:
    @staticmethod
    def from_result(
        destination: State,
        action: Action,
        origin: State,
    ) -> Reward:
        """Constructs from (state, action, next_state) triple"""
        ...


@dataclass
class Reward(float, _From, _Into, Stochastic):
    result_state: State
    action: Action
    origin_state: Optional[State]
