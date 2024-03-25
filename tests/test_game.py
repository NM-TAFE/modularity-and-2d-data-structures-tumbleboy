from unittest import mock
from unittest import TestCase
import game


class TestGame(TestCase):
    def setUp(self) -> None:
        self.game = game.Game()
        self.game.board.grid = [[" ", "X", " "],
                                [" ", " ", "0"],
                                [" ", " ", " "]]

    def test_move_is_valid(self):
        self.assertTrue(self.game.move_is_valid("8"))

    def test_move_is_invalid(self):
        self.assertFalse(self.game.move_is_valid("1"))
