"""
This module demonstrates how to do the following in PyGame:
  -- user-defined classes, and instances thereof
  -- geometric objects (circles)

Authors: Dave Fisher, David Mutchler, many others before them, and
         PUT_YOUR_NAME_HERE.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.
# -----------------------------------------------------------------------------
# TODO: IN-CLASS, WITH YOUR INSTRUCTOR:
#   1. Implement a Ball class with stubs for its methods.
#      Construct a single Ball.
#   2. Make the Ball appear on the screen.
#   3. Make the Ball move.
#   4. Make the Ball bounce.
#   5. Construct two Balls (instead of just a single Ball), on top of each other.
#      Then make each Ball start:
#        a. At a random place in the screen.
#        b. With a random speed within some reasonable range.
#        c. With a random radius within some reasonable range.
#        d. With a random color.
#   6. Make a list of (say) 100 Ball objects that all move and draw.
#      Make the screen bigger (say, 1000 by 800) to accommodate them.
#   7. Make a Balls class that stores its own list of Balls and moves/draws them.
#      Construct 25 slow, big Balls instance and 75 fast, small Balls instance.
#   8. Make a ScoreBoard that displays the number of bounces of (say) the initial Ball.
# -----------------------------------------------------------------------------

import pygame
import sys
from Ball import Ball
from Balls import Balls

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_BACKGROUND = "gray"


def main():
    # Initialization:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bouncing Balls")
    clock = pygame.time.Clock()

    ball1 = Ball(screen, SCREEN_WIDTH, SCREEN_HEIGHT, max_speed=10)
    ball2 = Ball(screen, SCREEN_WIDTH, SCREEN_HEIGHT, max_speed=2)
    balls = []
    for k in range(10):
        balls.append(Ball(screen, SCREEN_WIDTH, SCREEN_HEIGHT))
    slow_balls = Balls(screen, SCREEN_WIDTH, SCREEN_HEIGHT, 25,
                       max_speed=2, max_radius=30)
    fast_balls = Balls(screen, SCREEN_WIDTH, SCREEN_HEIGHT, 75,
                       max_speed=15, max_radius=8)

    # Game loop:
    while True:
        clock.tick(60)

        # Check for and handle events:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

        # Do every-cycle actions:
        ball1.move()
        ball2.move()
        for ball in balls:
            ball.move()
        slow_balls.move()
        fast_balls.move()

        # Draw everything:
        screen.fill(SCREEN_BACKGROUND)
        ball1.draw()
        ball2.draw()
        for ball in balls:
            ball.draw()
        slow_balls.draw()
        fast_balls.draw()
        pygame.display.update()


main()
