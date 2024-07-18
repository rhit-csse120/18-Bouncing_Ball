from Ball import Ball


class Balls:
    def __init__(self, screen, number_of_balls,
                 min_radius=5, max_radius=20,
                 min_speed=1, max_speed=5):
        self.balls = []
        for k in range(number_of_balls):
            ball = Ball(screen, min_radius, max_radius, min_speed, max_speed)
            self.balls.append(ball)

    def move(self):
        for ball in self.balls:
            ball.move()

    def draw(self):
        for ball in self.balls:
            ball.draw()
