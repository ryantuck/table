# Pattern

# primitive class for animations

import pygame
from pygame import gfxdraw as gfx


class Element:

	def __init__(self, screen, updateFrequency=1):
		
		# dimensions
		self.rows = screen.get_height()
		self.cols = screen.get_width()
		self.screen = screen

		# updating
		self.updateCount = 0
		self.maxUpdateCount = updateFrequency

	def iterate(self):
		self.updateCount += 1
		if self.updateCount == self.maxUpdateCount:
			self.updateCount = 0
			self.update()
		self.show()
					

	def update(self):
		# do nothing (if just blank element)
		pass

	def show(self):
		# do nothing by default
		pass




class FS(Element):

	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)

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





class FlashingSquare:

	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)

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

