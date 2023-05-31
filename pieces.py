import pygame
import os

# Load and scale images
RED_PAWN_IMAGE = pygame.image.load(os.path.join('images', 'red-pawn.png'))
RED_KING_IMAGE = pygame.image.load(os.path.join('images', 'red-king.png'))
BLACK_PAWN_IMAGE = pygame.image.load(os.path.join('images', 'black-pawn.png'))
BLACK_KING_IMAGE = pygame.image.load(os.path.join('images', 'black-king.png'))

RED_PAWN = pygame.transform.scale(RED_PAWN_IMAGE, (60, 60))
RED_KING = pygame.transform.scale(RED_KING_IMAGE, (60, 60))
BLACK_PAWN = pygame.transform.scale(BLACK_PAWN_IMAGE, (60, 60))
BLACK_KING = pygame.transform.scale(BLACK_KING_IMAGE, (60, 60))

class RedPawn(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.image = RED_PAWN
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]

class BlackPawn(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.image = BLACK_PAWN
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]

class RedKing(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.image = RED_KING
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]

class BlackKing(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos) -> None:
        super().__init__()
        self.image = BLACK_KING
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
