from backend import Point, Row, Player
from board import Board

import unittest

class TestContainsMethods(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)
        self.row_1 = Row([Point(0, 0, "1"), Point(0, 1, "1")], self.board)
        self.row_1_copy = Row([Point(0, 0, "1"), Point(0, 1, "1")], self.board)
        self.row_2 = Row([Point(1, 0, "2"), Point(1, 1, "2")], self.board)
        self.row_1_smol = Row([Point(0, 0, "1")], self.board)
        self.row_2_smol = Row([Point(1, 0, "2")], self.board)

        self.player_1 = Player(0)
        self.player_2 = Player(1)

    def test_assert_contains(self):
        self.assertTrue(self.row_1.contains(self.row_1_smol))

    def test_assert_not_contains(self):
        self.assertFalse(self.row_1.contains(self.row_2))

    def test_assert_contains_equal(self):
        self.assertTrue(self.row_1.contains(self.row_1))

    def test_assert_contains_copy(self):
        self.assertTrue(self.row_1.contains(self.row_1_copy))

    def test_player_contains(self):
        self.player_1.add_row(self.row_1)
        self.assertTrue(self.player_1.contains(self.row_1))

    def test_player_contains_smol(self):
        self.player_1.add_row(self.row_1)
        self.assertTrue(self.player_1.contains(self.row_1_smol))

    def test_player_update_rows(self):
        self.player_1.add_row(self.row_1_smol)
        self.assertTrue(self.player_1.contains(self.row_1))

if __name__ == "__main__":
    unittest.main()
