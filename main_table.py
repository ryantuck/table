
# Chromatico PyGame Table

# this will be the main program to deal with table graphics. 
# runs on PyGame.

# ==================================================

import pygame
import pygame.gfxdraw as gfx

from graphics.element import *
from graphics.custom_elements import *

import opc

# ------------------------------------------------
# Setup
# ------------------------------------------------

# working on hardware, or simulator?
hardware = True

if hardware:
  opcClient = opc.Client('localhost:7890')

# initialize with array size
pygame.init()

# set LED grid dimensions
xDim = 25
yDim = 7

# set whether LEDs should be covered by opaque screen
opaqueCover = False

# multiplier for python simulation
pixelMultiplier = 50

# define surface and screen for modifying and displaying, respectively
surf = pygame.Surface((pixelMultiplier*xDim,pixelMultiplier*yDim))

if not hardware:
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
checkers = Checkerboard(surf,updateFrequency=5)
mvBox = MovingBox(surf,updateFrequency=10,speed=20)
sparkles = PrimarySparkle(surf,updateFrequency=5)

elements = [checkers]


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

  if hardware:
    # actually write to the fadecandy
    pixels = [(0,0,0)] * xDim * yDim
    for x in range(xDim):
      for y in range(yDim):
        idx = 25*y + x
        tmpColor = smallSurf.get_at((x,y))
        pixels[idx] = (tmpColor.r,tmpColor.b,tmpColor.g)
    opcClient.put_pixels(pixels)
  else:
    # write surface to display
    pygame.display.get_surface().blit(bigSurf,(0,0))

    # update display
    pygame.display.flip()












  