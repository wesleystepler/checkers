import pygame
import os

# Load and scale images for the pieces
RED_PAWN_IMAGE = pygame.image.load(os.path.join('images', 'red-pawn.png'))
RED_KING_IMAGE = pygame.image.load(os.path.join('images', 'red-king.png'))
BLACK_PAWN_IMAGE = pygame.image.load(os.path.join('images', 'black-pawn.png'))
BLACK_KING_IMAGE = pygame.image.load(os.path.join('images', 'black-king.png'))

RED_PAWN = pygame.transform.scale(RED_PAWN_IMAGE, (60, 60))
RED_KING = pygame.transform.scale(RED_KING_IMAGE, (60, 60))
BLACK_PAWN = pygame.transform.scale(BLACK_PAWN_IMAGE, (60, 60))
BLACK_KING = pygame.transform.scale(BLACK_KING_IMAGE, (60, 60))
class CheckerSquare(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, tile):
        super().__init__()
        self.image = tile
        self.rect = self.image.get_rect()
        self.rect.topleft = [x_pos, y_pos]
    
    def __str__(self):
        return f"Checker Square a position ({self.x_pos}, {self.y_pos})"

class Pawn(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color) -> None:
        super().__init__()
        self.color = color
        if color == "red":
            self.image = RED_PAWN
        elif color == "black":
            self.image = BLACK_PAWN
        else:
            Exception("Invalid Input: Please enter 'red' or 'black' for Pawn or King color attribute")

        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]


class King(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color) -> None:
        super().__init__()
        self.color = color
        if color == "red":
            self.image = RED_KING
        elif color == "black": 
            self.image = BLACK_KING
        else:
            Exception("Invalid Input: Please enter 'red' or 'black' for King color attribute")
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
    
    def move(self, board_reference):
        pass
