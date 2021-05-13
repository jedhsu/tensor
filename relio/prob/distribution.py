from abc import ABCMeta, abstractmethod

from torch.distributions import Distribution as _Distribution


class Entropic:
    ...


class Distribution(_Distribution, metaclass=ABCMeta):
    """Wrapper class on `torch.distribution`."""

    def __init__(self):
        ...

    @abstractmethod
    def expand(self) -> Distribution:
        ...

    @property
    @abstractmethod
    def entropy(self) -> Entropic:
        ...

    @property
    @abstractmethod
    def cdf(self) -> Cdf:
        ...
