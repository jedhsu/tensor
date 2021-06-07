from __future__ import annotations


class Compute:
    @staticmethod
    def compute_expected_value(distribution: Probabilistic) -> float:
        ...

    @staticmethod
    def compute_variance(distribution: Probabilistic) -> float:
        ...

    @staticmethod
    def compute_standard_deviation(distribution: Probabilistic) -> float:
        ...


class Probabilistic(Compute):
    @property
    def expectation(self) -> float:
        ...

    @property
    def variance(self) -> float:
        ...

    @property
    def std(self) -> float:
        ...


class Probability(float):
    ...
