# Custom elements


from ..element import *
from ..color import *


class ScrollingRainbow(Element):

  colWidth = 0

  colors = [red,yellow,green,cyan,blue,magenta]

  position = 0
  colorIndex = 0

  def setup(self):
    self.colWidth = self.cols / 6
    print self.colWidth


  def update(self):
    # update scrolling stuff
    self.position += 4
    if self.position >= self.colWidth:
      self.position = 0
      self.colorIndex -= 1
      if self.colorIndex < 0:
        self.colorIndex += len(self.colors)


  def show(self):
    # draw rectangles of our color

    tmpIdx = self.colorIndex
    tmpX = self.position

    # draw from 0 to position
    gfx.box(self.screen,
      pygame.Rect(0,0,self.position,self.rows),
      self.colors[tmpIdx])

    tmpIdx = (tmpIdx + 1) % len(self.colors)

    # draw five full-width boxes
    for i in range(5):
      
      gfx.box(self.screen,
        pygame.Rect(tmpX,0,self.colWidth,self.rows),
        self.colors[tmpIdx])
      
      tmpIdx = (tmpIdx + 1) % len(self.colors)
      tmpX += self.colWidth

    # fill in end
    remainingWidth = self.cols - tmpX
    gfx.box(self.screen,
      pygame.Rect(tmpX,0,remainingWidth,self.rows),
      self.colors[tmpIdx])




