import pygame
import random


class Cell:
    """This file contains the cell class representing each square in the game"""

    def __init__(self, x, y, width, height, bomb_chance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_color = (200, 255, 255)  # RGB color
        self.font_color = (0, 0, 0)  # RGB color
        self.font = pygame.font.SysFont('Arial', 20)
        self.cell_thickness = 2
        self.neighbouring_bombs = 0
        self.selected = False

        self.cell_center = (
            self.x + (self.width / 2) // 2,
            self.y + (self.height / 2) // 2,
        )  # useful for drawing
        self.bomb = (
            random.random() < bomb_chance
        )  # each cell has a chance of being a bomb

    def log(self):
        print("X:" , self.x, " , Y:" , self.y, ", Bomb:", self.bomb, ", Selected:", self.selected, ", Neighbouring bombs:", self.neighbouring_bombs)

    def draw(self, screen):
        """This method is called in the main.py files draw_cells fkn"""
        # Hint: Should draw each cell, i.e something to do with pygame.draw.rect
        # Later on in the assignment it will do more as well such as drawing X for bombs or writing digits
        # Important: Remember that pygame starts with (0,0) coordinate in upper left corner!
        self.log()
        pygame.draw.rect(screen, self.cell_color, pygame.Rect(self.x, self.y, self.width, self.height), self.cell_thickness)

        if self.selected:
            if self.bomb:
                screen.blit(self.font.render('X', True, self.font_color), self.cell_center)
                screen.blit(pygame.font.SysFont('Comic Sans MS', 80).render('GAME OVER', True, (255,0,0)), (80,200))
            else:
                screen.blit(self.font.render(str(self.neighbouring_bombs), True, self.font_color), self.cell_center)

