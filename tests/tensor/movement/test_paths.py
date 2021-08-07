"""

    *Movement Paths,   [Unit Tests]*

"""
from tensor.tensor.movement.paths import Movement
from tensor.tensor.movement.paths import MovementPath
from tensor.tensor.movement.paths import MovementPaths
from tensor.tensor.movement.paths import Test


class TestMovementPaths:
    def test_init(self):
        chessboard = Test.chessboard
        assert isinstance(chessboard, MovementPaths)
        assert isinstance(chessboard, Movement)
        assert len(chessboard) == 2

        neighborhood = Test.neighborhood
        assert isinstance(chessboard, MovementPaths)
        assert isinstance(neighborhood, Movement)
        assert len(neighborhood) == 4

    def test_dimension(self):
        chessboard = Test.chessboard
        assert chessboard.dimension == 1

        neighborhood = Test.neighborhood
        assert neighborhood.dimension == 2

    def test_permute_dimensions(self):
        chessboard = Test.chessboard
        assert tuple(chessboard.permute_dimensions(5)) == ((0,), (1,), (2,), (3,), (4,))

    def test_into_paths(self):
        chessboard = Test.chessboard
        assert chessboard.into_paths(dimensions=4) == {
            MovementPath.create(-1, 0, 0, 0),
            MovementPath.create(1, 0, 0, 0),
            MovementPath.create(0, -1, 0, 0),
            MovementPath.create(0, 1, 0, 0),
            MovementPath.create(0, 0, -1, 0),
            MovementPath.create(0, 0, 1, 0),
            MovementPath.create(0, 0, 0, -1),
            MovementPath.create(0, 0, 0, 1),
        }
