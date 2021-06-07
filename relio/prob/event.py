from typing import Generic, TypeVar

T = TypeVar("T")

# [TODO] this typing impl can be cleaner


class Occurable(Generic[T]):
    """
    Occurable represents a probabilistic event.

    """

    # [TODO] strucutral subtyping would work well here i think
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# -- Aliases
Event = Occurable


class EventSpace(
    set[Occurable[T]],
):
    """
    Event Space.    (Omega)

    """

    pass


class SigmaAlgebra(EventSpace[T]):
    @staticmethod
    def _closed_under_complement():
        pass

    @staticmethod
    def _contains_generating_set():
        """
        Sigma-Algebra is a power set.

        """

    @staticmethod
    def _closed_under_countable_union():
        pass

    def __call__(self):
        pass


class _EventSpaces_:
    @staticmethod
    def dice_roll():
        return EventSpace(
            {
                Occurable(1),
                Occurable(2),
                Occurable(3),
                Occurable(4),
                Occurable(5),
                Occurable(6),
            }
        )
