import pygame
import os

class CheckerSquare(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, tile):
        super().__init__()
        self.image = tile
        self.rect = self.image.get_rect()
        self.rect.topleft = [x_pos, y_pos]
    
    def __str__(self):
        return f"Checker Square a position ({self.x_pos}, {self.y_pos})"


class Pawn(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, piece) -> None:
        super().__init__()
        self.image = piece
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]

class King(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, piece) -> None:
        super().__init__()
        self.image = piece
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
