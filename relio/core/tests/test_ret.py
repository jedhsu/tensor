from ..ret import Return
from ..step import Step


class TestReturn:
    def test_getitem(self):
        a = Return[Step]
