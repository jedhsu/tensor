"""

    *Axis*

"""

from dataclasses import dataclass

__all__ = ["Axis"]


@dataclass
class Axis:
    ordinal: int
    origin: int
    flipped: bool

    @classmethod
    def create(
        cls,
        ordinal: int,
        value: int = 0,
    ):
        flipped = True if value < 0 else False
        return cls(
            ordinal,
            origin=abs(value),
            flipped=flipped,
        )

    def update(
        self,
        value: int,
    ):
        self.flipped = True if value < 0 else False
        self.origin = abs(value)
