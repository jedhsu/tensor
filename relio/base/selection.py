class Hashable:
    def __init__(self):
        self.__hash_key = hash_key


class Realizable:
    def __init__(self, selection, outcome, probability):
        ...


class Selection(Hashable, Realizable):
    """Selection is tuple of a unique action in some state."""

    def __init__(self):
        ...

    def __hash__(self) -> str:
        ...
