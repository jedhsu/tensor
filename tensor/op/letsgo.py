from typing import Annotated

T = Annotated[int, ValueRange(5, 10)]

a: T
a = 3
