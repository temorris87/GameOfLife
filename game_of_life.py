import gui_game_board
import os
import pygame

BOARD_WIDTH = 500
BOARD_HEIGHT = 500

LIFE_CHAR = '-'
DEAD_CHAR = "*"


class GameOfLife(object):
    def __init__(self):
        pygame.init()
        size = [BOARD_WIDTH, BOARD_HEIGHT]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Game of Life")
        test_map = {'*': ["color", (0, 0, 0), None],
                    '-': ["img", os.path.join("img", "life.png"), None]}
        #: :type: gui_game_board.GUIGameBoard
        self.gboard = gui_game_board.GUIGameBoard(screen,
                                                  test_map,
                                                  "****---*********",
                                                  board_width=4,
                                                  board_height=4,
                                                  box_width=BOARD_WIDTH // 4)

    def animation(self):
        done = False
        clock = pygame.time.Clock()

        while not done:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

#            self.gboard.screen.fill(self.gboard.box_drawing_map['*'])
            self.game_iteration()
            self.gboard.update_screen()
            pygame.display.flip()

    def run(self):
        self.animation()
        pygame.quit()

    def game_iteration(self):
        temp = []
        for i, cell in enumerate(self.gboard.board_state):
            neighbors = self.count_nbr(i)
            if cell == LIFE_CHAR:
                if neighbors < 2 or neighbors > 3:
                    temp.append(DEAD_CHAR)
                else:
                    temp.append(LIFE_CHAR)
            else:
                if neighbors == 3:
                    temp.append(LIFE_CHAR)
                else:
                    temp.append(DEAD_CHAR)
        self.gboard.board_state = "".join(temp)

    def count_nbr(self, pos):
        counter = 0
        positions = self.gboard.get_all_neighbors(pos)

        for p in positions:

            if p == -1:
                continue

            if self.gboard.board_state[p] == LIFE_CHAR:
                counter += 1
        return counter


if __name__ == "__main__":
    game = GameOfLife()
    game.run()
