"""
This module demonstrates how to do the following in PyGame:
  -- user-defined classes, and instances thereof
  -- animated geometric objects (moving circles)

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # TODO: If you got help from anyone on this module, list their names here.

# ------------------------------------------------------------------------------
# TODO: IN-CLASS, WITH YOUR INSTRUCTOR:
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

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
SCREEN_BACKGROUND = "gray"


def main():
    # Initialization:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bouncing Balls")
    clock = pygame.time.Clock()

    # Game loop:
    while True:
        clock.tick(60)

        # Check for and handle events:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

        # Do every-cycle actions:

        # Draw everything:
        screen.fill(SCREEN_BACKGROUND)
        pygame.display.update()


main()
