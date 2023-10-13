import pygame
import random


class Ball:
    def __init__(self, screen, screen_width, screen_height, min_speed=1,
                 max_speed=5, min_radius=5, max_radius=20):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, self.screen_height)
        self.y = random.randint(0, self.screen_height)
        self.color = pygame.Color((random.randint(0, 255),
                                   random.randint(0, 255),
                                   random.randint(0, 255)))
        self.radius = random.randint(min_radius, max_radius)
        self.speed_x = min_speed + random.random() * (max_speed - min_speed)
        self.speed_x *= random.choice((1, -1))
        self.speed_y = min_speed + random.random() * (max_speed - min_speed)
        self.speed_y *= random.choice((1, -1))

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y

        if self.x > self.screen_width or self.x < 0:
            self.speed_x = -self.speed_x
        if self.y > self.screen_height or self.y < 0:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y),
                           self.radius)
