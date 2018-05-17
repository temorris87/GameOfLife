import game_board
import pygame


class GUIGameBoard(game_board.GameBoard):
    """
    Extends game_board.GameBoard to contain additional state for screen and
    background color to be used in drawing the board to the given screen.

    For box_drawing_map, must pass in a list of tuples with the following
    pattern: [('char', COLOR), ('char', PATH\\To\\File), ...]
    """

    def __init__(self,
                 screen,
                 box_drawing_map,
                 init_board_state,
                 board_width=8,
                 board_height=6,
                 box_width=50):
        super(GUIGameBoard, self).__init__(init_board_state, board_width, board_height)
        self.screen = screen
        #: :type: dictionary
        self.box_drawing_map = box_drawing_map
        self.box_width = box_width
        self.initialize_images()

    def update_screen(self):
        """
        the method used whenever to update the screen that holds the game_board
        :return: void
        """
        for i, box in enumerate(self.board_state):
            (x, y) = self.get_pixel_coord_from_pos(i)

            if self.box_drawing_map[box][0] == "color":
                pygame.draw.rect(self.screen,
                                 self.box_drawing_map[box][1],
                                 [x,
                                  y,
                                  self.box_width,
                                  self.box_width])
            else:
                self.screen.blit(self.box_drawing_map[box][2], (x, y))

    def get_pixel_coord_from_pos(self, pos):
        """
        Given a board position number, return the pixel coordinates for the
        given position.
        :param pos: Position on the board.
        :return: Success: [x_pixel, y_pixel] Failure: [-1, -1]
        """
        (x, y) = self.get_coord_from_pos(pos)
        if x == -1 and y == -1:
            return [-1, -1]
        return [x * self.box_width, y * self.box_width]

    def initialize_images(self):
        for entry in self.box_drawing_map.items():
            if entry[1][0] == "img":
                img_path = entry[1][1]
                entry[1][2] = pygame.image.load(img_path).convert()

