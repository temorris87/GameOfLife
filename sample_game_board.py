# Import a library of functions called 'pygame'
import pygame

BACKGROUND_COLOR = (0, 0, 0)
BOX_COLOR = (255, 255, 255)

BOARD_WIDTH = 500
BOARD_HEIGHT = 400
BOX_WIDTH = 10
BOXES_IN_ROW = BOARD_WIDTH // BOX_WIDTH
BOXES_IN_COL = BOARD_HEIGHT // BOX_WIDTH
NUM_BOXES = BOXES_IN_ROW * BOXES_IN_COL


def draw_game_board(boxes, screen):
    for i in boxes:
        row = i % BOXES_IN_ROW
        col = i // BOXES_IN_ROW
        pygame.draw.rect(screen, BOX_COLOR, [row * BOX_WIDTH,
                                             col * BOX_WIDTH,
                                             BOX_WIDTH,
                                             BOX_WIDTH])


def animation(screen):
    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BACKGROUND_COLOR)
        draw_game_board([1, 5, 8, 52, 200], screen)
        pygame.display.flip()


def main():
    pygame.init()
    size = [BOARD_WIDTH, BOARD_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game of Life")
    animation(screen)
    pygame.quit()


if __name__ == "__main__":
    main()