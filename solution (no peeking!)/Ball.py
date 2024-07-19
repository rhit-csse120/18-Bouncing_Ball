import pygame
import random


class Ball:
    def __init__(self, screen: pygame.Surface,
                 min_radius=10, max_radius=40,
                 min_speed=1, max_speed=8):
        self.screen = screen
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.x = random.randint(0, self.screen.get_width() - 1)
        self.y = random.randint(0, self.screen.get_height() - 1)
        self.radius = random.randint(min_radius, max_radius)

        direction = random.choice((-1, 1))
        x_above_min = random.random() * (max_speed - min_speed)
        self.speed_x = direction * x_above_min

        direction = random.choice((-1, 1))
        y_above_min = random.random() * (max_speed - min_speed)
        self.speed_y = direction * y_above_min

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.bounce_if_offscreen()

    def bounce_if_offscreen(self):
        if self.x < 0 or self.x >= self.screen.get_width():
            self.speed_x = -self.speed_x
        if self.y < 0 or self.y >= self.screen.get_height():
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.x, self.y), self.radius)
