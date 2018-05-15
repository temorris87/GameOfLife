import game_board


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
                 board_width=400,
                 board_height=300,
                 box_width=50,
                 background_color=(0, 0, 0)):
        self.screen = screen
        self.box_drawing_map = box_drawing_map
        super.init_board_state = init_board_state
        super.board_width = board_width            # Not true, needs to be converted to non pixel value
        super.board_height = board_height          # Not true, needs to be converted to non pixel value
        self.box_width = box_width
        self.background_color = background_color

    def update_screen(self):
        pass

    def draw_game_board(self, boxes, screen):
        pass
#        for i in boxes:
#            row = i % BOXES_IN_ROW
#            col = i // BOXES_IN_ROW
#            pygame.draw.rect(screen, BOX_COLOR, [row * BOX_WIDTH,
#                                                 col * BOX_WIDTH,
#                                                 BOX_WIDTH,
#                                                 BOX_WIDTH])

#    def get_background_color(self):
#       return self.background_color
