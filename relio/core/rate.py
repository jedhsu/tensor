class DiscountRate(float):
    symbol = "\u03b3"

    def __init__(self, rate: float):
        return super(DiscountRate, self).__new__(float, rate)
