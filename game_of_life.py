import gui_game_board
import pygame

BOARD_WIDTH = 500
BOARD_HEIGHT = 400
BOX_WIDTH = 10

BACKGROUND_COLOR = (0, 0, 0)
BOX_COLOR = (255, 255, 255)

class GameOfLife(object):
    def __init__(self, gboard):
        #: :type: gui_game_board.GUIGameBoard
        self.gboard = gboard #gui_game_board(gboard)

    def draw_game_board(self):
        boxes = self.gboard
        for i in boxes:
            row = i % BOXES_IN_ROW
            col = i // BOXES_IN_ROW
            pygame.draw.rect(screen, BOX_COLOR, [row * BOX_WIDTH,
                                                 col * BOX_WIDTH,
                                                 BOX_WIDTH,
                                                 BOX_WIDTH])

    def animation(self,screen):
        done = False
        clock = pygame.time.Clock()

        while not done:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill(BACKGROUND_COLOR)
            draw_game_board()
            pygame.display.flip()


    def run(self):
        pygame.init()
        size = [BOARD_WIDTH, BOARD_HEIGHT]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Game of Life")

        self.gboard = gui_game_board.GUIGameBoard()
        animation(screen)
        pygame.quit()




'''
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
'''
if __name__ == "__main__":
    game = GameOfLife(gui_game_board.GUIGameBoard)
    game.run()
