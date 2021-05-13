from __future__ import annotations

from .evaluate import Evaluate
from .improve import Improve
from .iterate import Iterate

__all__ = ["Policy"]


class Compute:
    @staticmethod
    def compute_bellman_optimality(policy: Policy):
        ...


class Initialize:
    @staticmethod
    def initialize_arbitrarily(policy: Policy) -> Policy:
        """Initializes a randomly-chosen policy."""
        ...


class Policy(
    ProbDistribution[State, Action],
    Compute,
    Initialize,
    Evaluate,
    Improve,
    Iterate,
    Optimize,
):
    ...
