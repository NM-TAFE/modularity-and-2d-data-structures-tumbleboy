import unittest
import board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.height = 3
        self.width = 3
        self.valid_board = board.Board(self.height, self.width)

        # Horizontal win
        self.horizontal_win_board = board.Board(self.height, self.width)
        self.horizontal_win_board.grid = [["X", "X", "X"],
                                          [" ", " ", " "],
                                          [" ", " ", " "]]

        # Vertical win
        self.vertical_win_board = board.Board(self.height, self.width)
        self.vertical_win_board.grid = [["0", "X", "X"],
                                        [" ", "X", "0"],
                                        [" ", "X", "0"]]

        # Diagonal win
        self.diagonal_win_board = board.Board(self.height, self.width)
        self.diagonal_win_board.grid = [["0", "X", "X"],
                                        ["X", "0", "0"],
                                        [" ", "X", "0"]]

    def test_valid_grid_creation(self):
        # Test cols
        self.assertEqual(self.height, self.valid_board.height)
        # Test rows
        self.assertEqual(self.width, self.valid_board.width)

    def test_invalid_grid_creation(self):
        height = 2
        width = 2
        self.assertRaises(Exception, lambda: board.Board(height, width))

    def test_horizontal_winner(self):
        self.assertTrue(self.horizontal_win_board.get_winner())
        self.assertTrue(self.horizontal_win_board.has_horizontal_winner())

    def test_vertical_winner(self):
        self.assertTrue(self.vertical_win_board.get_winner())
        self.assertTrue(self.vertical_win_board.has_vertical_winner())

    def test_diagonal_winner(self):
        self.assertTrue(self.diagonal_win_board.get_winner())
        self.assertTrue(self.diagonal_win_board.has_diagonal_winner())


if __name__ == '__main__':
    unittest.main()
