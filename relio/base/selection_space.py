from __future__ import annotations
from typing import Mapping, overload


class Definable:
    @overload
    @staticmethod
    def define(
        mdp: MarkovDecisionProcess,
        dynamics: Mapping[Selection, Realizable],
    ) -> MarkovDecisionProcess:
        ...

    Onto = Mapping
    Surjection = Onto

    @overload
    @staticmethod
    def define(selection_space: SelectionSpace, dynamics: Onto[Selection, Realizable]):
        ...

    @staticmethod
    def define(selection_space, dynamics):
        ...


class MarkovDecisionProcess(Definable):
    def define_dynamics(self):
        ...
