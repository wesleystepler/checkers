import pygame
import os
from pieces import King, Pawn, CheckerSquare

# Set up the Display
pygame.init()
pygame.display.set_caption("Checkers")

WIDTH = 900
HEIGHT = 700
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Create Rect object in place of normal mouse cursor
pygame.mouse.set_visible(False)
CURSOR_IMAGE = pygame.image.load(os.path.join('images', 'cursor.png'))
CURSOR = pygame.transform.scale(CURSOR_IMAGE, (35, 35))

cursor = CURSOR.get_rect()

# Load and scale images for the Board
WOOD_TILE_IMAGE_1 = pygame.image.load(os.path.join('images', 'wood-tile-1.jpg'))
WOOD_TILE_IMAGE_2 = pygame.image.load(os.path.join('images', 'wood-tile-2.jpg'))

WOOD_TILE_1 = pygame.transform.scale(WOOD_TILE_IMAGE_1, (75, 75))
WOOD_TILE_2 = pygame.transform.scale(WOOD_TILE_IMAGE_2, (75, 75))


# Some variables we will use to loop through the initialization of the board
cur_tile = 'tile1'
x, y, = 150, 50
step = 75

""" A Two-Dimensional list which enables convenient referencing of each tile sprite. The board
    is laid out in the list as follows:
       0  1  2  3  4  5  6  7
    0  X  X  X  X  X  X  X  X
    1  X  X  X  X  X  X  X  X
    2  X  X  X  X  X  X  X  X
    3  X  X  X  X  X  X  X  X
    4  X  X  X  X  X  X  X  X
    5  X  X  X  X  X  X  X  X
    6  X  X  X  X  X  X  X  X
    7  X  X  X  X  X  X  X  X
"""
board_reference = []

# Initialize Board and Pieces
board = pygame.sprite.Group()
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
# A generic list of all the pieces we will reference later
pieces = []
red_pieces = pygame.sprite.Group()
black_pieces = pygame.sprite.Group()

for a in range(0, 2):
    if a == 0:
        i = 0
        j = 1
    else:
        i = 1
        j = 0

    for b in range(0, 4):
        piece = Pawn(0, 0, 'red')
        piece.rect.center = board_reference[i][j].rect.center
        red_pieces.add(piece)
        pieces.append(piece)
        j += 2

for a in range(0, 2):
    if a == 0:
        i = 6
        j = 1
    else:
        i = 7
        j = 0

    for b in range(0, 4):
        piece = Pawn(0, 0, 'black')
        piece.rect.center = board_reference[i][j].rect.center
        black_pieces.add(piece)
        pieces.append(piece)
        j += 2

# Method for drawing the screen
def draw_window():
  WIN.fill((1,50,32))
  board.draw(WIN)
  red_pieces.draw(WIN)
  black_pieces.draw(WIN)
  pygame.draw.rect(WIN, (0,0,0), cursor)
  pygame.display.flip()
  

def main():
  clock = pygame.time.Clock()

  running = True
  while running:
    pos = pygame.mouse.get_pos()
    cursor.center = pos
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in pieces:
                if piece.rect.colliderect(cursor):
                    piece.move()
                
    # We will be using this later when we implement moving pieces   
    keys_pressed = pygame.key.get_pressed()
    draw_window()

if __name__ == "__main__":
  main()