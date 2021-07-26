from ..base import Action
from .state import State


class From:
    def from_sas():
        ...

    def from_sasr():
        ...


@dataclass
class Transition(
    Probability,
    Hashable,
    _From,
):
    state: State
    prev_action: Action
    prev_state: State
    reward: Optional[Reward] = None
