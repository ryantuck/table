
# Chromatico PyGame Table

# this will be the main program to deal with table graphics. 
# runs on PyGame.

# OpenGL not needed for this jawn.

# ==================================================


import pygame
import pygame.gfxdraw as gfx

from pattern import *

square1 = FlashingSquare()

# initialize with array size
pygame.init()
screen = pygame.display.set_mode((1000,280))
done = False
clock = pygame.time.Clock()


# main loop
while not done:
  for event in pygame.event.get():

    # handle quit
    if event.type == pygame.QUIT:
      done = True

    # cycle the color of our rectangle if space bar is hit
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      cycleColor()

  # keep frame rate to 60 fps
  clock.tick(60)

  # clear screen
  screen.fill((0,0,0))

  square1.update(screen)

  # update display
  pygame.display.flip()