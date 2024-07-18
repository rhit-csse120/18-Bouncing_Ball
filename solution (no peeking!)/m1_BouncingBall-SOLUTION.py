"""
This module demonstrates how to do the following in PyGame:
  -- user-defined classes, and instances thereof
  -- animated geometric objects (moving circles)

Authors: Dave Fisher, David Mutchler, many others before them, and
         SOLUTION by David Mutchler.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.
# ------------------------------------------------------------------------------
# DONE: IN-CLASS, WITH YOUR INSTRUCTOR:
#  0. Read and absorb the starting code (standard for a PyGame project).
#  1. Implement a Ball class with stubs for its methods (__init__, move, draw).
#     Construct a single Ball.
#  2. Make the Ball appear on the screen.
#  3. Make the Ball move.
#  4. Make the Ball bounce.
#  5. Construct two Ball instances (instead of just a single Ball),
#     on top of each other.  After testing that, make each Ball start:
#       a. At a random place in the screen.
#       b. With a random speed within some range specified
#            by __init__ parameters.
#       c. With a random radius within some range specified
#            by __init__ parameters.
#       d. With a random color.
#  6. Make a list of (say) 100 Ball instances that all move and draw.
#     Make the screen bigger (say, 1000 by 650) to accommodate them.
#  7. Make a Balls class that stores its own list of Ball instances
#     and moves/draws them. Construct two Balls instances, with (respectively):
#       -- 25 slow, big Ball instances
#       -- 75 fast, small Ball instances
#  8. (Optional) Make a ScoreBoard that displays the number of bounces
#     of (say) the initial Ball.
# ------------------------------------------------------------------------------

import pygame
import sys
from Ball import Ball
from Balls import Balls

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_BACKGROUND = "gray"


def main():
    # Initialization:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bouncing Balls")
    clock = pygame.time.Clock()

    ball1 = Ball(screen, 3, 10)
    ball2 = Ball(screen, max_speed=2)
    balls = []
    for k in range(10):
        balls.append(Ball(screen))
    slow_balls = Balls(screen,25, max_speed=2, max_radius=30)
    fast_balls = Balls(screen,75, max_speed=15, max_radius=8)

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
