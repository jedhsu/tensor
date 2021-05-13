class _From:
    @staticmethod
    def _from_sum(ret: Return):
        pass


class Return(
    float,
    Timestep,
    Series,
    State,
    _From,
    _Into,
):
    def __init__(self, value: float):
        super(Return, self).__new__(float, value)
