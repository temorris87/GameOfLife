import gui_game_board
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
        test_map = {'*': (255, 255, 255), '-': (0, 0, 0)}
        #: :type: gui_game_board.GUIGameBoard
        self.gboard = gui_game_board.GUIGameBoard(screen, test_map, "-******-", board_width=4, board_height=2, box_width=BOARD_WIDTH//4)

    def animation(self):
        done = False
        clock = pygame.time.Clock()

        while not done:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.gboard.screen.fill(self.gboard.box_drawing_map['*'])
            self.gboard.update_screen()
            pygame.display.flip()

    def run(self):
        self.animation()
        pygame.quit()


    def game_iteration(self):
        pass

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
