from typing import Iterator

from .batch import Batch


class Load:
    def load(self) -> Iterator[Batch]:
        ...


class Preprocess:
    ...


class Encode:
    ...


class Decode:
    ...


class Dataset(Load):
    ...
