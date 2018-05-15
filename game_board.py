class GameBoard(object):
    """
    Hold the state for a game board for use in any general tiled game.
    A game board is defined as having the following numbering system:

        ---------------------
        | 0 | 1 | 2 | 3 | 4 |
        ---------------------
        | 5 | 6 | 7 | 8 | 9 |
        ---------------------
        | . | . | . | . | . |
        ---------------------

    The key attributes that make up the size of a game board are its width,
    height, and box_width, which all must be passed in upon initialization.
    Support for drawing both color filled rectangles and images exist. The
    screen that the board is to be drawn upon must also be passed in upon
    initialization.

    Initial board state should be a single string where str[i] is the ith box
    in the game board. Example for the above could be "**********".
    """

    def __init__(self,
                 init_board_state,
                 board_width=20,
                 board_height=10):
        self.board_state = init_board_state
        self.board_width = board_width
        self.board_height = board_height

    def get_board_height(self):
        '''
        Get and return the height of the board.
        :return: The height of the board.
        '''
        return self.board_height

    def get_board_width(self):
        '''
        Get and return the width of the board.
        :return: The width of the board.
        '''
        return self.board_width

    def get_relative_location(self, pos, x_pos, y_pos):
        pass

    def get_location_up(self, pos):
        pass

    def get_location_up_left(self, pos):
        pass

    def get_location_left(self, pos):
        pass

    def get_location_down_left(self, pos):
        pass

    def get_location_down(self, pos):
        pass

    def get_location_down_right(self, pos):
        pass

    def get_location_right(self, pos):
        pass

    def get_location_up_right(self, pos):
        pass

    def update_board(self, box_rep, pos):
        """
        Update the board to contain a character 'box_rep' at position pos.
        :param box_rep: The tile to be replaced, example: '*'
        :param pos: The position in the mapping above to be replaced.
        :return: void
        """
        pass

