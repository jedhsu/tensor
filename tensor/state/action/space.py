"""
    Action Space

  The set of actions at a state.

"""

from dataclasses import dataclass
from typing import Any, Mapping, Sequence, TypeVar

from ..state import State


class Step(int):
    def __new__(cls, val: int):
        super(Step, cls).__new__(int, val)


class _Equivalence_:
    def equivalence():
        ...


class Hashable:
    ...


T = TypeVar("T")

Expectation[U | T]


class Distribution(Mapping[T, float]):
    ...


@dataclass
class Action(Hashable):
    __slots__ = (
        "name",
        "state",
    )
    name: str
    state: State
    outcomes: Distribution[StateSpace]


class _Select_(Action):
    def select(self) -> Result:
        return ActionSpace[self]


class Reward(float):
    def __new__(cls, value: float):
        return super(Reward, cls).__new__(Reward, value)


@dataclass
class Result:
    origin: State
    action: State
    reward: Reward
    destination: State


class Reward(float):
    def __new__(cls, val: float):
        return super(Reward, cls).__new__(cls, val)


class Actionable(
    State,
):
    ...


class ActionSpace(set[Action]):
    def __init__(self, space: set[Action]):
        super().__init__(space)
