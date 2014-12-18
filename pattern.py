# Pattern

# primitive class for animations

import pygame
from pygame import gfxdraw as gfx


class Element:

	def __init__(self,screen):
		self.rows = rows
		self.cols = columns

	def printGrid(self):
		print "Rows: %i | Columns: %i" % (self.rows, self.cols)
		for i in range(self.rows * self.cols):
			print self.pixels[i]


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

