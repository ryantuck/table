
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

square2 = FS(screen,updateFrequency=30)

# main loop
while not done:
  for event in pygame.event.get():

    # handle quit
    if event.type == pygame.QUIT:
      done = True

  # keep frame rate to 60 fps
  clock.tick(60)

  # clear screen
  screen.fill((0,0,0))

  square1.update(screen)

  square2.iterate()

  # update display
  pygame.display.flip()