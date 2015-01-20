
# primary sparkle

# gonna have a ton of sparkles going off randomly

from ..element import *
from ..color import *
import random

class PrimarySparkle(Element):

  totalSparkles = 100
  sparkleSize = 40

  colors = [red,yellow,green,cyan,blue,magenta]

  locations = [(0,0)]*totalSparkles

  def setup(self):
    pass

  def update(self):
    
    for i in range(self.totalSparkles):

      randX = random.randrange(self.cols)
      randY = random.randrange(self.rows)

      self.locations[i] = (randX,randY)

  def show(self):

    for i in range(self.totalSparkles):

      colorIndex = i % 6

      gfx.box(self.screen,
        pygame.Rect(
          self.locations[i][0],
          self.locations[i][1],
          self.sparkleSize,
          self.sparkleSize),
        self.colors[colorIndex])



