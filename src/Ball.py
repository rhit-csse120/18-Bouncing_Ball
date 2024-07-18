import pygame
import random


class Ball:
    def __init__(self, screen: pygame.Surface,
                 min_speed, max_speed):
        self.screen = screen
        self.color = (128, 128, 0)
        self.x = random.randint(0, self.screen.get_width() - 1)
        self.y = random.randint(0, self.screen.get_height() - 1)
        self.radius = 15
        self.x_speed = 3
        self.y_speed = -2

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

        self.bounce_if_off_screen()

    def bounce_if_off_screen(self):
        if self.x < 0 or self.x >= self.screen.get_width():
            self.x_speed = -self.x_speed
        if self.y < 0 or self.y >= self.screen.get_height():
            self.y_speed = -self.y_speed

    def draw(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.x, self.y), self.radius)

