import pygame

def main():
  pygame.init()
  pygame.display.set_caption("Checkers")

  screen = pygame.display.set_mode((700, 700))
  board = pygame.image.load("images/board.jpg").convert()
  screen.blit(board, (0, 0))
  pygame.display.flip()

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

if __name__ == "__main__":
  main()