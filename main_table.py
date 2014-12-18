
# Chromatico PyGame Table

# this will be the main program to deal with table graphics. 
# runs on PyGame.

# OpenGL not needed for this jawn.

# ==================================================


import pygame
import pygame.gfxdraw as gfx

from pattern import *





# initialize with array size
pygame.init()
screen = pygame.display.set_mode((1000,280))
done = False
clock = pygame.time.Clock()

square1 = StandaloneFlashingSquare()
square2 = FlashingSquare(screen,updateFrequency=60)
square3 = FlashingSquare(screen,updateFrequency=20)
square4 = FlashingSquare(screen,updateFrequency=10)

square2.setOrigin(200,200)
square3.setOrigin(500,100)
square4.setOrigin(600,200)

elements = [square2,square3,square4]

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
  
  for element in elements:
  	element.iterate()

  # update display
  pygame.display.flip()