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
        self.num_positions = board_width * board_height

    def get_coord_from_pos(self, pos):
        """
        Given a board position number, return the x and y coordinates for the
        given position.
        :param pos: Position on the board.
        :return: Success: [x_pos, y_pos] Failure: [-1, -1]
        """
        row = pos // self.board_width
        col = pos % self.board_width

        if (row < 0 or col < 0 or
                (row > self.board_height - 1) or (col > self.board_width - 1)):
            return [-1, -1]

        return [col, row]

    def get_board_height(self):
        """
        Get and return the height of the board.
        :return: The height of the board.
        """
        return self.board_height

    def get_board_width(self):
        """
        Get and return the width of the board.
        :return: The width of the board.
        """
        return self.board_width

    def get_relative_location(self, pos, x_pos, y_pos):
        """
        Given a position for a board and relative coordinates, determine the
        grid number for the relative position.
        :param pos: The position to search relative to.
        :param x_pos: The relative x coordinate.
        :param y_pos: The relative y coordinate.
        :return: The grid number for the targeted relative position.
        """
        [col, row] = self.get_coord_from_pos(pos)

        if col == -1 and row == -1:
            return -1

        row = row + y_pos
        col = col + x_pos

        if not self.is_coord_in_board(col, row):
            return -1

        return row * self.board_width + col

    def get_location_up(self, pos):
        """
        Return the position above the given position.
        :param pos: The target position.
        :return: The number for the above position.
        """
        return self.get_relative_location(pos, 0, -1)

    def get_location_up_left(self, pos):
        """
        Return the position above and left of the given position.
        :param pos: The target position.
        :return: The number for the position above and left of pos.
        """
        return self.get_relative_location(pos, -1, -1)

    def get_location_left(self, pos):
        """
        Return the position left of the given position.
        :param pos: The target position.
        :return: The number for the position left of pos.
        """
        return self.get_relative_location(pos, -1, 0)

    def get_location_down_left(self, pos):
        """
        Return the position down left of the given position.
        :param pos: The target position.
        :return: The number for the position down left of pos.
        """
        return self.get_relative_location(pos, -1, 1)

    def get_location_down(self, pos):
        """
        Return the position down of the given position.
        :param pos: The target position.
        :return: The number for the position down of pos.
        """
        return self.get_relative_location(pos, 0, 1)

    def get_location_down_right(self, pos):
        """
        Return the position down right of the given position.
        :param pos: The target position.
        :return: The number for the position down right of pos.
        """
        return self.get_relative_location(pos, 1, 1)

    def get_location_right(self, pos):
        """
        Return the position right of the given position.
        :param pos: The target position.
        :return: The number for the position right of pos.
        """
        return self.get_relative_location(pos, 1, 0)

    def get_location_up_right(self, pos):
        """
        Return the position up right of the given position.
        :param pos: The target position.
        :return: The number for the position up right of pos.
        """
        return self.get_relative_location(pos, 1, -1)

    def is_coord_in_board(self, col, row):
        """
        Determine if the given coordinates exist on the current board.
        :param col: The current column in question.
        :param row: The current row in question.
        :return: True if coordinates are on board, False otherwise.
        """
        if (row < 0 or col < 0 or
                (row > self.board_height - 1) or (col > self.board_width - 1)):
            return False
        else:
            return True

    def is_pos_in_board(self, pos):
        """
        Determine if the given position exists on the current board.
        :param pos: The position in question.
        :return: True if position is in board, False otherwise.
        """
        if pos < 0 or pos > self.num_positions - 1:
            return False
        else:
            return True

    def update_board(self, box_rep, pos):
        """
        Update the board to contain a character 'box_rep' at position pos.
        :param box_rep: The tile to be replaced, example: '*'
        :param pos: The position in the mapping above to be replaced.
        :return: void
        """
        pass
