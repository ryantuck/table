
# Chromatico PyGame Table

# this will be the main program to deal with table graphics. 
# runs on PyGame.

# ==================================================

import pygame
import pygame.gfxdraw as gfx

from graphics.element import *
from graphics.custom_elements import *

# ------------------------------------------------
# Setup
# ------------------------------------------------

# initialize with array size
pygame.init()

# set LED grid dimensions
xDim = 25
yDim = 7

# set whether LEDs should be covered by opaque screen
opaqueCover = True

# multiplier for python simulation
pixelMultiplier = 50

# define surface and screen for modifying and displaying, respectively
surf = pygame.Surface((pixelMultiplier*xDim,pixelMultiplier*yDim))
screen = pygame.display.set_mode((pixelMultiplier*xDim,pixelMultiplier*yDim))

# additional parameters
done = False
clock = pygame.time.Clock()


# ------------------------------------------------
# Element(s)
# ------------------------------------------------

sr1 = ScrollingRainbow(surf)
ft = FullTableColorCycle(surf,updateFrequency=1)
stripes = Stripes(surf)
checkers = Checkerboard(surf)
mvBox = MovingBox(surf,updateFrequency=10,speed=20)
sparkles = PrimarySparkle(surf,updateFrequency=5)

elements = [mvBox]


# ------------------------------------------------
# Main Loop
# ------------------------------------------------

while not done:
  for event in pygame.event.get():

    # handle quit
    if event.type == pygame.QUIT:
      done = True

  # keep frame rate to 60 fps
  clock.tick(60)

  # clear screen
  surf.fill((0,0,0))

  # update elements if applicable
  for element in elements:
  	element.iterate()

  # scale down surf to 7x25 grid (using averaging algorithm)
  # would use this surface to output to LEDs as needed
  smallSurf = pygame.transform.smoothscale(surf,(xDim,yDim))

  # scale up to large display
  # note - transform.scale is more glitchy
  # transform.smoothscale is my best bet of what it will look like with opaque glass over LEDs
  if opaqueCover:
    bigSurf = pygame.transform.smoothscale(smallSurf,(pixelMultiplier*xDim,pixelMultiplier*yDim))
  else:
    bigSurf = pygame.transform.scale(smallSurf,(pixelMultiplier*xDim,pixelMultiplier*yDim))

  # write surface to display
  pygame.display.get_surface().blit(bigSurf,(0,0))

  # update display
  pygame.display.flip()










  