from __future__ import annotations
from collections.abc import Collection
from typing import Hashable, Iterator

from .state import State


class _From:
    @staticmethod
    def from_state() -> StateSpace:
        State


# class Stateful(Hashable):
#     def __init__(self, state: dict[str, Union[dict, Hashable]]):
#         ...

#     def __hash__(self) -> str:
#         ...


class StateSpace(
    Collection[State],
    _From,
    _Into,
):
    def __init__(self):
        ...

    def __iter__(self) -> Iterator[Stateful]:
        ...

    @property
    def state(self) -> Stateful:
        return self.__state
