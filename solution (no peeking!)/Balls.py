import pygame
from Ball import Ball


class Balls:
    def __init__(
        self,
        screen: pygame.Surface,
        number_of_balls,
        min_radius=10,
        max_radius=40,
        min_speed=1,
        max_speed=8,
    ):
        self.list_of_balls = []
        for k in range(number_of_balls):
            ball = Ball(screen, min_radius, max_radius, min_speed, max_speed)
            self.list_of_balls.append(ball)

    def move(self):
        for ball in self.list_of_balls:
            ball.move()

    def draw(self):
        for ball in self.list_of_balls:
            ball.draw()
