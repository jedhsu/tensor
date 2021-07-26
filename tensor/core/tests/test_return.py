from ..ret import Return
from ..step import Step


class TestReturn:
    def test_getitem(self):
        r = Return[Step]

        assert r.step is True
        assert isinstance(r, Return)
