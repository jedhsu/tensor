from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator


# TODO: very clear that state needs a join function

# MAKE STATE A MONOID
# make monadic protocols for python - proven to be helpful


class _From:
    @staticmethod
    def from_dataclass(dc: object) -> State:
        ...

    @staticmethod
    def from_dict(dct: dict) -> State:
        ...


class Space:
    def _get_space():
        ...


class State(Timestep, Space):
    def sweep(self) -> Iterator[Update]:
        ...
