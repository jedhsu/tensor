from collections.abc import MutableMapping
from dataclasses import dataclass
from typing import Optional

from ..base import Return
from ..base.action import Action
from ..state import State
from .policy import Policy

# class Compute:
#     @staticmethod
#     def compute(state: EnvironmentState]


@dataclass
class ActionValueFunction(MutableMapping[State, Return]):
    policy: Policy
    state: State
    action: Optional[Action]
