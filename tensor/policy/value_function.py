from .world import WorldState

class Compute:
    @staticmethod
    def compute(state: EnvironmentState):
        ..

class ValueFunction(Policy, MutableMapping[State, Value]):
    def __init__(self, state: EnvironmentState):
        super(ValueFunction, self).__init__()

