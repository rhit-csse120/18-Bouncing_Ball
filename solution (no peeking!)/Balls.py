from Ball import Ball


class Balls:
    def __init__(self, screen, number_of_balls,
                 min_speed=1, max_speed=5,
                 min_radius=5, max_radius=20):
        self.balls = []
        for k in range(number_of_balls):
            ball = Ball(screen, min_speed, max_speed, min_radius, max_radius)
            self.balls.append(ball)

    def move(self):
        for ball in self.balls:
            ball.move()

    def draw(self):
        for ball in self.balls:
            ball.draw()
