
# moving circle

# testing to see how color smoothing works on a simple object that doesn't fit neatly in grid

from ..element import *
from ..color import *

class MovingBox(Element):

  location = 0
  boxTop = 120
  boxHeight = 120
  boxWidth = 120

  boxColor = red
  backgroundColor = green

  def __init__(self,screen,updateFrequency=1,speed=1):
    Element.__init__(self,screen,updateFrequency)
    self.speed = speed

  def setup(self):
    pass

  def update(self):
    self.location += self.speed
    self.location = self.location % self.cols

  def show(self):

    gfx.box(self.screen,
      pygame.Rect(0,0,self.cols,self.rows),
      self.backgroundColor)

    gfx.box(self.screen,
      pygame.Rect(self.location,
        self.boxTop,
        self.boxWidth,
        self.boxHeight),
      self.boxColor)



