"""

Value function.

"""
from ..policy import Policy
from .state import State


class Value(State, Policy):
    def value(state: State, policy: Policy):
        ...
