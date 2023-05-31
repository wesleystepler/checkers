import pygame
import os
from pieces import BlackKing, BlackPawn, CheckerSquare, RedKing, RedPawn, WOOD_TILE_1, WOOD_TILE_2


# Set up the Display
pygame.init()
pygame.display.set_caption("Checkers")

WIDTH = 900
HEIGHT = 700
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Initialize Board
board = pygame.sprite.Group()

# Some variables we will use to loop through the initialization of the board
cur_tile = WOOD_TILE_1
x, y, = 150, 50
step = 75

# A two-dimensional list to use as a convenient reference to all the board sprites later
board_reference = []
for i in range(0, 8):
    row = []
    for j in range (0, 8):
        if j % 2 == 0 and i % 2 == 0 or j % 2 != 0 and i % 2 != 0:
            cur_tile = WOOD_TILE_1
        else:
            cur_tile = WOOD_TILE_2

        tile = CheckerSquare(x, y, cur_tile)
        board.add(tile)
        row.append(tile)
        x += step
    y += step
    x = 150
    board_reference.append(row)

# Initialize Pieces
red_pawn = RedPawn(50, 50)
red_king = RedKing(300, 50)
black_pawn = BlackPawn(50, 650)
black_king = BlackKing(100, 650)

red_pieces = pygame.sprite.Group()
red_pieces.add(red_pawn)
red_pieces.add(red_king)

black_pieces = pygame.sprite.Group()
black_pieces.add(black_pawn)
black_pieces.add(black_king)

# Method for drawing the screen
def draw_window():
  WIN.fill((1,50,32))
  board.draw(WIN)
  #red_pieces.draw(WIN)
  #black_pieces.draw(WIN)
  pygame.display.flip()
  

def main():
  clock = pygame.time.Clock()

  running = True
  while running:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # We will be using this later when we implement moving pieces   
    keys_pressed = pygame.key.get_pressed()
    draw_window()

if __name__ == "__main__":
  main()