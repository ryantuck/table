
# Checkerboard

# this is a test element, designed to light up like a checkerboard (one LED per square)
# using transform.scale() to scale back up to a large surface retains hard edges on lines
# transform.smoothscale() gives a cool effect

from ..element import *
from ..color import *

class Checkerboard(Element):

  colorIdx1 = 0
  colorIdx2 = 127
  totalColors = 255

  color1 = calculateRGB(totalColors,colorIdx1)
  color2 = calculateRGB(totalColors,colorIdx2)

  def setup(self):
    pass

  def update(self):
    self.colorIdx1 = (self.colorIdx1 + 1) % self.totalColors
    self.colorIdx2 = (self.colorIdx2 + 1) % self.totalColors
    self.color1 = calculateRGB(self.totalColors,self.colorIdx1)
    self.color2 = calculateRGB(self.totalColors,self.colorIdx2)

  def show(self):

    for i in range(7):
      for j in range(25):

        tmpColor = self.color1
        if (i+j) % 2 == 0:
          tmpColor = self.color2

        gfx.box(self.screen,
          pygame.Rect(50*j,50*i,50*j+49,50*i+49),
          tmpColor)


