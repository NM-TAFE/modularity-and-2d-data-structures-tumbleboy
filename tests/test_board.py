import unittest
import board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.height = 3
        self.width = 3
        self.valid_board = board.Board(self.height, self.width)

    def test_valid_grid_creation(self):
        # Test cols
        self.assertEqual(self.height, self.valid_board.height)
        # Test rows
        self.assertEqual(self.width, self.valid_board.width)

    def test_invalid_grid_creation(self):
        height = 2
        width = 2
        invalid_board = board.Board(height, width)
        self.assertIsNone(invalid_board.grid)


if __name__ == '__main__':
    unittest.main()
