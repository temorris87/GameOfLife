from unittest import TestCase
import game_board


class TestGameBoard(TestCase):
    def setUp(self):
        self.board = game_board.GameBoard("********", 4, 2)

    def test_get_coord_from_pos(self):
        [x, y] = self.board.get_coord_from_pos(0)
        self.assertEqual(x, 0, "The x position is incorrect.")
        self.assertEqual(y, 0, "The y position is incorrect.")

        [x, y] = self.board.get_coord_from_pos(6)
        self.assertEqual(x, 2, "The x position is incorrect.")
        self.assertEqual(y, 1, "The y position is incorrect.")

        [x, y] = self.board.get_coord_from_pos(-1)
        self.assertEqual(x, -1, "The x position is incorrect.")
        self.assertEqual(y, -1, "The y position is incorrect.")

        [x, y] = self.board.get_coord_from_pos(8)
        self.assertEqual(x, -1, "The x position is incorrect.")
        self.assertEqual(y, -1, "The y position is incorrect.")

    def test_get_board_height(self):
        self.assertEqual(self.board.board_height, 2, "Heights are not the same.")

    def test_get_board_width(self):
        self.assertEqual(self.board.board_width, 4, "Widths are not the same.")

    def test_get_relative_location(self):
        self.assertEqual(self.board.get_relative_location(2, 1, 1),
                         7,
                         "Position is incorrect.")
        self.assertEqual(self.board.get_relative_location(5, 1, -1),
                         2,
                         "Position is incorrect.")
        self.assertEqual(self.board.get_relative_location(4, 3, -1),
                         3,
                         "Position is incorrect.")
        self.assertEqual(self.board.get_relative_location(4, -1, 0),
                         -1,
                         "Position is incorrect.")
        self.assertEqual(self.board.get_relative_location(3, 1, 0),
                         -1,
                         "Position is incorrect.")
        self.assertEqual(self.board.get_relative_location(6, 0, 1),
                         -1,
                         "Position is incorrect.")
        self.assertEqual(self.board.get_relative_location(2, 0, -1),
                         -1,
                         "Position is incorrect.")

    def test_get_location_up(self):
        self.assertEqual(self.board.get_location_up(5),
                         1,
                         "Position up is incorrect.")
        self.assertEqual(self.board.get_location_up(1),
                         -1,
                         "Position up is incorrect.")

    def test_get_location_up_left(self):
        self.assertEqual(self.board.get_location_up_left(6),
                         1,
                         "Position up left is incorrect.")
        self.assertEqual(self.board.get_location_up_left(1),
                         -1,
                         "Position up left is incorrect.")

    def test_get_location_left(self):
        self.assertEqual(self.board.get_location_left(5),
                         4,
                         "Position left is incorrect.")
        self.assertEqual(self.board.get_location_left(4),
                         -1,
                         "Position left is incorrect.")

    def test_get_location_down_left(self):
        self.assertEqual(self.board.get_location_down_left(3),
                         6,
                         "Position down left is incorrect.")
        self.assertEqual(self.board.get_location_down_left(6),
                         -1,
                         "Position down left is incorrect.")

    def test_get_location_down(self):
        self.assertEqual(self.board.get_location_down(3),
                         7,
                         "Position down is incorrect.")
        self.assertEqual(self.board.get_location_down(7),
                         -1,
                         "Position down is incorrect.")

    def test_get_location_down_right(self):
        self.assertEqual(self.board.get_location_down_right(2),
                         7,
                         "Position down right is incorrect.")
        self.assertEqual(self.board.get_location_down_right(7),
                         -1,
                         "Position down right is incorrect.")

    def test_get_location_right(self):
        self.assertEqual(self.board.get_location_right(6),
                         7,
                         "Position right is incorrect.")
        self.assertEqual(self.board.get_location_right(7),
                         -1,
                         "Position right is incorrect.")

    def test_get_location_up_right(self):
        self.assertEqual(self.board.get_location_up_right(6),
                         3,
                         "Position up right is incorrect.")
        self.assertEqual(self.board.get_location_up_right(3),
                         -1,
                         "Position up right is incorrect.")

    def test_is_coord_in_board(self):
        self.assertTrue(self.board.is_coord_in_board(0, 1),
                        "Coordinates should be in board.")
        self.assertFalse(self.board.is_coord_in_board(-1, 2),
                         "Coordinates should not be in board.")
        self.assertFalse(self.board.is_coord_in_board(2, -1),
                         "Coordinates should not be in board.")
        self.assertFalse(self.board.is_coord_in_board(-1, -1),
                         "Coordinates should not be in board.")
        self.assertFalse(self.board.is_coord_in_board(4, 0),
                         "Coordinates should not be in board.")
        self.assertFalse(self.board.is_coord_in_board(2, 2),
                         "Coordinates should not be in board.")

    def test_is_pos_in_board(self):
        self.assertTrue(self.board.is_pos_in_board(2),
                        "Value should be in board.")
        self.assertFalse(self.board.is_pos_in_board(-1),
                         "Value should not be in board.")
        self.assertFalse(self.board.is_pos_in_board(8),
                         "Value should not be in board.")

    def test_update_board(self):
        success = self.board.update_board('-', 3)
        updated_board = self.board.board_state
        self.assertTrue(success, "Updating board failed.")
        self.assertEqual(updated_board, "***-****", "Incorrect board update.")

        success = self.board.update_board('+', 5)
        updated_board = self.board.board_state
        self.assertTrue(success, "Updating board failed.")
        self.assertEqual(updated_board, "***-*+**", "Incorrect board update.")

        success = self.board.update_board('-', -1)
        updated_board = self.board.board_state
        self.assertFalse(success, "Updating board failed.")
        self.assertEqual(updated_board, "***-*+**", "Incorrect board update.")

        success = self.board.update_board('-', 8)
        updated_board = self.board.board_state
        self.assertFalse(success, "Updating board failed.")
        self.assertEqual(updated_board, "***-*+**", "Incorrect board update.")

        success = self.board.update_board('--', 2)
        updated_board = self.board.board_state
        self.assertFalse(success, "Updating board failed.")
        self.assertEqual(updated_board, "***-*+**", "Incorrect board update.")

        success = self.board.update_board('', 2)
        updated_board = self.board.board_state
        self.assertFalse(success, "Updating board failed.")
        self.assertEqual(updated_board, "***-*+**", "Incorrect board update.")