"""
This module demonstrates how to do the following in PyGame:
  -- user-defined classes, and instances thereof
  -- animated geometric objects (moving circles)

Authors: Dave Fisher, David Mutchler, many others before them, and
         SOLUTION by David Mutchler.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.
# ------------------------------------------------------------------------------
# DONE: IN-CLASS, WITH YOUR INSTRUCTOR:
#  0. Run the supplied solution and DESIGN (but do not yet IMPLEMENT)
#       the obvious CLASS (type of thing) in this project.
#       What should be its methods?  Its instance variables?
#  0. Read and absorb the starting code (standard for a PyGame project).
#  1. Implement a Ball class with stubs for its methods (__init__, move, draw).
#     Construct a single Ball.
#  2. Make the Ball appear on the screen.
#  3. Make the Ball move.
#  4. Make the Ball bounce.
#  5. Construct two Ball instances (instead of just a single Ball),
#     initially on top of each other.  Then make each Ball start:
#       a. At a random place in the screen.
#       b. With a random color.
#       c. With a random radius within some range specified
#            by __init__ parameters.
#       d. With a random speed within some range specified
#            by __init__ parameters, along with a random direction.
#  6. Make a list of (say) 10 Ball instances that all move and draw.
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

    ball1 = Ball(screen, max_speed=30)
    ball2 = Ball(screen, 15, 20, max_speed=3)
    # ball3 = Ball(screen, max_radius=30)

    balls = []
    for k in range(10):
        ball = Ball(screen)
        balls.append(ball)

    slow_balls = Balls(screen, 25,
                       min_radius=15, max_radius=50,
                       max_speed=4)
    fast_balls = Balls(screen, 75,
                       max_radius=12,
                       min_speed=5, max_speed=25)

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
        for k in range(len(balls)):
            balls[k].move()
        slow_balls.move()
        fast_balls.move()

        # Draw everything:
        screen.fill(SCREEN_BACKGROUND)
        ball1.draw()
        ball2.draw()
        for k in range(len(balls)):
            balls[k].draw()
        slow_balls.draw()
        fast_balls.draw()
        pygame.display.update()


main()
