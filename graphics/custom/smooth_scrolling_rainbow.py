# Custom elements


from ..element import *
from ..color import *


class SmoothScrollingRainbow(Element):

  position = 0

  def setup(self):
    pass

  def update(self):
    self.position = (self.position + 1) % 25

  def show(self):
    
    # draw 25 columns of different colors
    for i in range(25):

      tmpIdx = (self.position + i) % 25
      tmpColor = calculateRGB(25,tmpIdx)
      tmpColor = expandColor(tmpColor)
      tmpX = i*50

      gfx.box(self.screen,
        pygame.Rect(tmpX,0,50,self.rows),
        tmpColor)




