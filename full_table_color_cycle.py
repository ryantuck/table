# full-table rotating color

# cycles through a primary color over the whole table

# could benefit from messing around with brightness levels

from element import *
from color import *

class FullTableColorCycle(Element):

  differentColors = 255
  colorIndex = 0

  currentColor = (0,0,0)

  def setup(self):
    pass

  def update(self):
    self.colorIndex = (self.colorIndex + 1) % self.differentColors
    self.currentColor = calculateRGB(self.differentColors,self.colorIndex)
    print self.currentColor[0],self.currentColor[1],self.currentColor[2]

  def show(self):
    gfx.box(self.screen,
      pygame.Rect(0,0,self.cols,self.rows),
      self.currentColor)



