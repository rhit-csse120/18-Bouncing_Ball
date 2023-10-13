from Ball import Ball


class Balls:
    def __init__(self, screen, screen_width, screen_height,
                 number_of_balls, min_speed=1, max_speed=5,
                 min_radius=5, max_radius=20):
        self.balls = []
        for k in range(number_of_balls):
            self.balls.append(Ball(screen, screen_width, screen_height,
                                   min_speed, max_speed, min_radius, max_radius))

    def move(self):
        for ball in self.balls:
            ball.move()

    def draw(self):
        for ball in self.balls:
            ball.draw()
