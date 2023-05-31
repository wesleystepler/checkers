import pygame
import os
from pieces import BlackKing, BlackPawn, RedKing, RedPawn


# Set up the Display
pygame.init()
pygame.display.set_caption("Checkers")

WIDTH = 700
HEIGHT = 700
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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
  board = pygame.image.load("images/board.jpg").convert()
  WIN.blit(board, (0, 0))
  red_pieces.draw(WIN)
  black_pieces.draw(WIN)
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