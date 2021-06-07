from typing import Any, Sequence

from sympy.concrete.summations import Sum

from .step import Step

__all__ = ["Return"]

# class _From:
#     @staticmethod
#     def _from_sum(ret: Return):
#         pass


# class Return(
#     float,
#     Timestep,
#     Series,
#     State,
#     _From,
#     _Into,
# ):
#     def __init__(self, value: float):
#         super(Return, self).__new__(float, value)

# Return[Step] = Reward[Step, 1] + Return[Step, 1]
# _Equivalence_


class Return:

    # def split(self, offset) -> tuple[Reward, Return]:
    #     ...

    def rewards(self) -> Iterator[Reward]:
        """
        Returns an infinite iterator of the rewards.

        """

        return Sum(Reward, (t + 1, T))

    @classmethod
    def __class_getitem__(cls, items: Sequence[Any]):

        if isinstance(items, Step):
            return Return(has_step=True)
