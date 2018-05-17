from unittest import TestCase
import gui_game_board
import pygame


class TestGUIGameBoard(TestCase):
    def setUp(self):
        pygame.init()
        size = [500, 400]
        screen = pygame.display.set_mode(size)
        test_map = {'*': (255, 255, 255), '-': (0, 0, 0)}
        self.board = gui_game_board.GUIGameBoard(screen, test_map, "********", board_width=4, board_height=2)

    def tearDown(self):
        pygame.quit()

    def test_get_pixel_coord_from_pos(self):
        (x, y) = self.board.get_pixel_coord_from_pos(2)
        self.assertEqual(x, 100, "x coord is incorrect")
        self.assertEqual(y, 0, "y coord is incorrect")

        (x, y) = self.board.get_pixel_coord_from_pos(4)
        self.assertEqual(x, 0, "x coord is incorrect")
        self.assertEqual(y, 50, "y coord is incorrect")

        (x, y) = self.board.get_pixel_coord_from_pos(-1)
        self.assertEqual(x, -1, "x coord is incorrect")
        self.assertEqual(y, -1, "y coord is incorrect")

        (x, y) = self.board.get_pixel_coord_from_pos(8)
        self.assertEqual(x, -1, "x coord is incorrect")
        self.assertEqual(y, -1, "y coord is incorrect")