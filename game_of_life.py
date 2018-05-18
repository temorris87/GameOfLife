import gui_game_board
import pygame
import random
BOARD_WIDTH = 1920
BOARD_HEIGHT = 1080

LIFE_CHAR = '-'
DEAD_CHAR = "*"


class GameOfLife(object):
    def __init__(self):


        print("given a 192 x 108 board, you want to indicate coordinate for where live is created")
        w = int(input("please enter the width:"))
        h = int(input("please enter the height:"))

        bit_vector = self.bit_vector_init(w, h)

        self.brd_file_init(bit_vector)
        pygame.init()
        size = [BOARD_WIDTH, BOARD_HEIGHT]
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        pygame.display.set_caption("Game of Life")
        test_map_path = "themes/default.cfg"
        test_board_path = "boards/default.brd"
        #: :type: gui_game_board.GUIGameBoard
        self.gboard = gui_game_board.GUIGameBoard(screen,
                                                  test_map_path,
                                                  test_board_path)

    def bit_vector_init(self, width, height):
        bit_vector = []
        for x in range(192*108):
            bit_vector.append(0)

        if width <= 10:
            width += 10
        elif width >= 192 - 10:
            width -= 10

        if height <= 10:
            height += 10
        elif height >= 108 - 10:
            height -= 10

        random.seed()

        for x in range(random.randint(0, 50)):
            nh = height + random.randint(-4, 4)
            nw = width + random.randint(-4, 4)

            if nh >= 192:
                continue
            elif nw >= 108:
                continue

            bit_vector[192 * nh + nw] = 1

        return bit_vector

    def brd_file_init(self, bit_vector):
        fd = open("boards/default.brd", 'w')
        w = int(BOARD_WIDTH) // 10
        h = int(BOARD_HEIGHT) // 10
        fd.write(str(w) + '\n')
        fd.write(str(h) + '\n')

        i = 0
        j = 0
        count = 0
        while i < h:
            wline = ""
            while j < w:
                if bit_vector[count] != 0:
                    wline += '-'
                else:
                    wline += '*'
                count += 1
                j += 1
            fd.write(wline + '\n')
            i += 1
            j = 0

        fd.close()


    def animation(self):
        done = False
        clock = pygame.time.Clock()

        while not done:
            clock.tick(11)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type is pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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
