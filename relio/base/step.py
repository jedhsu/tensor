__all__ = ["Step"]


class Step(int):
    def __new__(cls, val: int):
        return super(Step, cls).__new__(cls, val)
