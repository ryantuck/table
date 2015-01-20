
# Stripes

# this is a test element, designed to light up the seven distinct rows
# using transform.scale() to scale back up to a large surface retains hard edges on lines
# transform.smoothscale() gives a smoothing rainbow

from ..element import *
from ..color import *

class Stripes(Element):

  def setup(self):
    pass

  def update(self):
    pass

  def show(self):
    for i in range(7):
      tmpColor = calculateRGB(210,30*i)
      gfx.box(self.screen,
      pygame.Rect(0,50*i,self.cols,50*i+49),
      tmpColor)


