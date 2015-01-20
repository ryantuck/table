# Element

# primitive class for animations

import pygame
from pygame import gfxdraw as gfx

from color import *


class Element:

	def __init__(self, screen, updateFrequency=1):
		
		# dimensions
		self.rows = screen.get_height()
		self.cols = screen.get_width()
		self.screen = screen

		# updating
		self.updateCount = 0
		self.maxUpdateCount = updateFrequency

		self.setup()

	def setup(self):
		# take care of setting shit up
		pass

	def iterate(self):
		self.updateCount += 1
		if self.updateCount == self.maxUpdateCount:
			self.updateCount = 0
			self.update()
		self.show()

	# essentially updates the model - backend stuff
	def update(self):
		# do nothing (if just blank element)
		pass

	# defines how view is updated - front-end stuff
	def show(self):
		# do nothing by default
		pass




class FlashingSquare(Element):

	x = 100
	y = 100

	colorIndex = 1
	colors = [red,green,blue]


	def colorCycle(self,cIdx):
		cIdx += 1
		cIdx = cIdx % 3
		return cIdx

	def update(self):
		self.colorIndex = self.colorCycle(self.colorIndex)
		

	def show(self):
		gfx.box(self.screen,pygame.Rect(self.x,self.y,20,20),self.colors[self.colorIndex])


	def setOrigin(self,x,y):
		self.x = x
		self.y = y


class FlashingMovingSquare(FlashingSquare):

	moveIndex = 0
	maxMoveIndex = 10

	direction = 0
	maxDirection = 4

	def updateMoveIndex(self,m):
		m += 1
		m = m % self.maxMoveIndex
		return m

	def updateDirection(self,d):
		d += 1
		d = d % self.maxDirection
		return d

	def move(self,left=False,right=False,up=False,down=False,unit=1):
		if left:
			self.x -= unit
		if right:
			self.x += unit
		if up:
			self.y -= unit
		if down:
			self.y += unit

	def moveLeft(self,unit=1):
		self.move(left=True,unit=unit)

	def moveRight(self,unit=1):
		self.move(right=True,unit=unit)

	def moveUp(self,unit=1):
		self.move(up=True,unit=unit)

	def moveDown(self,unit=1):
		self.move(down=True,unit=unit)

	def update(self):
		self.colorIndex = self.colorCycle(self.colorIndex)

		if self.direction == 0:
			self.moveLeft(unit=5)
		elif self.direction == 1:
			self.moveDown(unit=5)
		elif self.direction == 2:
			self.moveRight(unit=5)
		else:
			self.moveUp(unit=5)

		self.moveIndex = self.updateMoveIndex(self.moveIndex)
		if self.moveIndex == 0:
			self.direction = self.updateDirection(self.direction)


class MovingBlueCircle(FlashingMovingSquare):

	def update(self):

		if self.direction == 0:
			self.move(up=True,left=True,unit=5)
		elif self.direction == 1:
			self.move(down=True,left=True,unit=5)
		elif self.direction == 2:
			self.move(down=True,right=True,unit=5)
		else:
			self.move(up=True,right=True,unit=5)

		self.moveIndex = self.updateMoveIndex(self.moveIndex)
		if self.moveIndex == 0:
			self.direction = self.updateDirection(self.direction)

	def show(self):
		gfx.circle(self.screen,self.x,self.y,20,blue)



# demonstration class to highlight benefits of subclass system
class StandaloneFlashingSquare:

	x = 20
	y = 20

	# count based on 60 fps frame rate
	updateCount = 0
	maxUpdateCount = 30

	colors = [red,green,blue]
	colorIndex = 0

	def colorCycle(self,cIdx):
		cIdx += 1
		cIdx = cIdx % 3
		return cIdx

	def update(self,screen):

		self.updateCount += 1

		if (self.updateCount == self.maxUpdateCount):
			
			self.updateCount = 0
			self.colorIndex = self.colorCycle(self.colorIndex)
		gfx.box(screen,pygame.Rect(self.x,self.y,20,20),self.colors[self.colorIndex])

