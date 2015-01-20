
# Checkerboard

# this is a test element, designed to light up like a checkerboard (one LED per square)
# using transform.scale() to scale back up to a large surface retains hard edges on lines
# transform.smoothscale() gives a cool effect

from ..element import *
from ..color import *

class Checkerboard(Element):

  def setup(self):
    pass

  def update(self):
    pass

  def show(self):

    for i in range(7):
      for j in range(25):

        tmpColor = red
        if (i+j) % 2 == 0:
          tmpColor = blue

        gfx.box(self.screen,
          pygame.Rect(50*j,50*i,50*j+49,50*i+49),
          tmpColor)


