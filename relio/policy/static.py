"""

A probability distribution under the probability space of the StateSpace,
into the measurable space of ActionSpace.

"""
class StaticPolicy(
    ProbabilityDistribution[StateSpace, ActionSpace],


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
