from typing import Any, Sequence

from sympy import Symbol
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


class Return(Stochastic):

    # def split(self, offset) -> tuple[Reward, Return]:
    #     ...

    def rewards(self):
        """
        Returns an infinite iterator of the rewards.

        """

        return Sum(Symbol("r"), (Symbol("t") + 1, Symbol("T")))

    @classmethod
    def __class_getitem__(cls, items: Sequence[Any]):

        if isinstance(items, Step):
            return Return(has_step=True)
