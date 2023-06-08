import pygame
import os
from pieces import King, Pawn, CheckerSquare, BLACK_KING, RED_KING

# Set up the Display
pygame.init()
pygame.display.set_caption("Checkers")

# Some global variables that will be helpful to us
WIDTH = 900
HEIGHT = 700
FPS = 60
FONT = pygame.font.SysFont("Times New Roman", 30)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
P1TURN = True

#Create Rect object in place of normal mouse cursor
pygame.mouse.set_visible(False)
CURSOR_IMAGE = pygame.image.load(os.path.join('images', 'cursor.png'))
CURSOR = pygame.transform.scale(CURSOR_IMAGE, (35, 35))
cursor = CURSOR.get_rect()

# Load and scale images for the Board
WOOD_TILE_IMAGE_1 = pygame.image.load(os.path.join('images', 'wood-tile-1.jpg'))
WOOD_TILE_IMAGE_2 = pygame.image.load(os.path.join('images', 'wood-tile-2.jpg'))
POSSIBLE_MOVE_IMAGE = pygame.image.load(os.path.join('images', 'can-move.png'))

WOOD_TILE_1 = pygame.transform.scale(WOOD_TILE_IMAGE_1, (75, 75))
WOOD_TILE_2 = pygame.transform.scale(WOOD_TILE_IMAGE_2, (75, 75))
POSSIBLE_MOVE = pygame.transform.scale(POSSIBLE_MOVE_IMAGE, (75, 75))


# Some variables we will use to loop through the initialization of the board
cur_tile = 'placeholder'
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

# Two Groups each set of pieces
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


def whose_turn(text, font, text_col, x, y):
    """Helper method that displays whose turn it is on the screen"""
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))

def midpoint(p1, p2):
    """Helper method that returns the midpoint of a line.
        Used in this program to help determine the outcome of jumps"""
    
    m1 = int((p1[0] + p2[0])/2)
    m2 = int((p1[1] + p2[1])/2)
    return (m1, m2)

def draw_window():
  """Updates the screen"""
  WIN.fill((1,50,32))
  if P1TURN:
      whose_turn("Player 1, it's your turn!", FONT, (255, 255, 255), 150, 0)
  if not P1TURN:
      whose_turn("Player 2, it's your turn!", FONT, (255, 255, 255), 150, 0)
  board.draw(WIN)
  red_pieces.draw(WIN)
  black_pieces.draw(WIN)
  pygame.draw.rect(WIN, (0,0,0), cursor)
  pygame.display.flip()


def get_current_square(piece, board_reference):
    """Returns the i and j indicies of the square the selected piece is currently on"""
    for i in range(0, len(board_reference)):
        for j in range(0, len(board_reference[i])):
            if piece.rect.colliderect(board_reference[i][j]):
                return (i, j)
            

def get_possible_moves(piece, board_reference, pieces, black_pieces, red_pieces):
    """Returns all possible moves for a given piece and highlights them on the board"""
    possible_moves = []
    for i in range(0, len(board_reference)):
        for j in range(0, len(board_reference[i])):
            if board_reference[i][j].rect.colliderect(piece):

                if piece.color == 'red' or piece.type == "King":
                    if (j+1) < len(board_reference[i]) and (i + 1) < len(board_reference):
                        if not board_reference[i+1][j+1].occupied(pieces):
                            possible_moves.append(board_reference[i+1][j+1])
                        elif (i+2) < len(board_reference) and (j+2) < len(board_reference[i]):
                            if not board_reference[i+2][j+2].occupied(pieces):
                                for p in pieces:
                                    if p.rect.colliderect(board_reference[i+1][j+1]) and p.color != piece.color:
                                        possible_moves.append(board_reference[i+2][j+2])

                    if (j-1) >= 0 and (i + 1) < len(board_reference):
                        if not board_reference[i+1][j-1].occupied(pieces):
                            possible_moves.append(board_reference[i+1][j-1])
                        elif (i+2) < len(board_reference) and (j-2) >= 0:
                            if not board_reference[i+2][j-2].occupied(pieces):
                                for p in pieces:
                                    if p.rect.colliderect(board_reference[i+1][j-1]) and p.color != piece.color:
                                        possible_moves.append(board_reference[i+2][j-2])

                if piece.color == 'black' or piece.type == "King":
                    if (j+1) < len(board_reference[i]) and (i - 1) >= 0:
                        if not board_reference[i-1][j+1].occupied(pieces):
                            possible_moves.append(board_reference[i-1][j+1])
                        elif (i-2) >= 0 and (j+2) < len(board_reference[i]):
                            if not board_reference[i-2][j+2].occupied(pieces):
                                for p in pieces:
                                    if p.rect.colliderect(board_reference[i-1][j+1]) and p.color != piece.color:
                                        possible_moves.append(board_reference[i-2][j+2])
                        

                    if (j-1) >= 0 and (i - 1) >= 0:
                        if not board_reference[i-1][j-1].occupied(pieces):
                            possible_moves.append(board_reference[i-1][j-1])
                        elif (i-2) >= 0 and (j-2) >= 0:
                            if not board_reference[i-2][j-2].occupied(pieces):
                                for p in pieces:
                                    if p.rect.colliderect(board_reference[i-1][j-1]) and p.color != piece.color:
                                        possible_moves.append(board_reference[i-2][j-2])
                break
    for move in possible_moves:
        move.image = POSSIBLE_MOVE
    return possible_moves

def cursor_on_piece(cursor, black_pieces, red_pieces, turn):
    """ Checks if the cursor is over a piece on the board. Will
        only return True if it's a piece that belongs to the correct player."""
    if turn:
        for piece in black_pieces:
            if piece.rect.colliderect(cursor):
                return True
    else:
        for piece in red_pieces:
            if piece.rect.colliderect(cursor):
                return True
    return False

def cursor_on_square(cursor, board_reference, pieces, options):
    """ Checks if the cursor is over an open square on the board"""
    for i in range(0, len(board_reference)):
        for j in range(0, len(board_reference[i])):
            if board_reference[i][j].rect.colliderect(cursor) and not board_reference[i][j].occupied(pieces) and board_reference[i][j] in options:
                return True
    return False

def jump(cur_piece, prev_square, cur_square, board_reference, pieces, black_pieces, red_pieces, turn):
    mid_square = midpoint(cur_square, prev_square)
    i, j = mid_square[0], mid_square[1]
    taken = board_reference[i][j]
    if turn:
        for piece in red_pieces:
            if piece.rect.colliderect(taken):
                piece.kill()
                pieces.remove(piece)
    else:
        for piece in black_pieces:
            if piece.rect.colliderect(taken):
                piece.kill()
                pieces.remove(piece)


def move(cur_piece, board_reference, pieces, black_pieces, red_pieces, turn, options):
    """Moves a given piece to the selected available square"""
    prev_square = get_current_square(cur_piece, board_reference)
    for i in range(0, len(options)):
        if options[i].rect.colliderect(cursor):
            cur_piece.rect.center = options[i].rect.center
            break
    cur_square = get_current_square(cur_piece, board_reference)
    if abs(cur_square[0] - prev_square[0]) == 2 and abs(prev_square[1] - cur_square[1]) == 2:
        jump(cur_piece, prev_square, cur_square, board_reference, pieces, black_pieces, red_pieces, turn)


def king_me(piece, pieces):
    """Delete the Pawn() that has made it to the other side of the board and
        replace it with a King()"""
    king = King(piece.rect.center[0], piece.rect.center[1], piece.color)
    piece.kill()
    pieces.add(king)


def deselect(options):
    """Clear the possible moves list and un-highlight the squares"""
    for squares in options:
        squares.image = WOOD_TILE_2
    options.clear()
    return options

                
def main():
  """Main method that runs the game"""
  global P1TURN
  clock = pygame.time.Clock()

  running = True

  options = []
  piece_selected = False
  cur_piece = None

  while running:
    draw_window()
    pos = pygame.mouse.get_pos()
    cursor.center = pos
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        # Check if the player has clicked on a valid piece or clicked on an unoccupied square to move to
        if event.type == pygame.MOUSEBUTTONDOWN and cursor_on_piece(cursor, black_pieces, red_pieces, P1TURN):
            for piece in pieces:
                if piece.rect.colliderect(cursor):
                    cur_piece = piece
                    piece_selected = True
                    if len(options) != 0:
                        deselect(options)
                    options = get_possible_moves(piece, board_reference, pieces, black_pieces, red_pieces)
                    break

        # Only allow this to execute if a piece has been selected to prevent any click on a square
        # resulting in a turn ending
        elif piece_selected and event.type == pygame.MOUSEBUTTONDOWN and cursor_on_square(cursor, board_reference, pieces, options):
            move(cur_piece, board_reference, pieces, black_pieces, red_pieces, P1TURN, options) 
            if P1TURN:
                for square in board_reference[0]:
                    if cur_piece.rect.colliderect(square):
                        king = King(piece.rect.center[0], piece.rect.center[1], piece.color)
                        cur_piece.kill()
                        pieces.remove(cur_piece)
                        black_pieces.add(king)
                        cur_piece = king
                        pieces.append(cur_piece)
                        break
            else:
                for square in board_reference[7]:
                    if cur_piece.rect.colliderect(square):
                        king = King(piece.rect.center[0], piece.rect.center[1], piece.color)
                        cur_piece.kill()
                        pieces.remove(cur_piece)
                        red_pieces.add(king)
                        cur_piece = king
                        pieces.append(cur_piece)
                        break

            options = deselect(options) 
            # It's P1s turn when this is True, and P2s turn when this is False
            P1TURN = not P1TURN  
            piece_selected = False 

if __name__ == "__main__":
    main()