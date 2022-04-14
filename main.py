import pygame, sys
import numpy as np

pygame.init()

SCREEN_SIZE = 600, 600
COLOR_LINE = (23, 145, 156)
COLOR_BG = (28, 170, 156)
LINE_WIDTH = 10
BOARD_ROWS = BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR = 255, 255, 255
CROSS_WIDTH = 25
SPACE = 55
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('TIC TAC TOE')
screen.fill(COLOR_BG)

board = np.zeros((BOARD_ROWS, BOARD_COLS))
#print(board)


def draw_lines():
    #1 Horizontal
    pygame.draw.line(screen, COLOR_LINE, (0, 200), (600, 200), LINE_WIDTH)
    #2 Horizontal
    pygame.draw.line(screen, COLOR_LINE, (0, 400), (600, 400), LINE_WIDTH)

    # 1 Vertical
    pygame.draw.line(screen, COLOR_LINE, (200, 0), (200, 600), LINE_WIDTH)
    # 2 Vertical
    pygame.draw.line(screen, COLOR_LINE, (400, 0), (400, 600), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            if board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0
    if board[row][col] == 0:
        return True
    else:
        return False


draw_lines()

player = 1

#main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            print(clicked_row, clicked_col)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1

                draw_figures()

                print(board)

    pygame.display.update()
