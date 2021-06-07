from typing import Any, Sequence


class Expectation:
    @classmethod
    def __class_getitem__(cls, items: Sequence[Any]):
        assert 1 == 2, items
        return 1
