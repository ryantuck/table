
import sys

class Color:

	def __init__(self,r,g,b):
		self.r = r
		self.g = g
		self.b = b

	def printColor(self):
		print "R: %i | G: %i | B: %i" % (self.r, self.g, self.b)

class Point:
	def __init__(self,row,col):
		self.r = row
		self.c = col

	def printPoint(self):
		print "X: %i | Y: %i" % (self.r, self.c)


class Grid:

	def __init__(self,rows,columns):
		self.rows = rows
		self.cols = columns
		black = Color(0,0,0)
		self.pixels = [black]*self.rows*self.cols

	def printGrid(self):
		print "Rows: %i | Columns: %i" % (self.rows, self.cols)
		for i in range(self.rows * self.cols):
			print self.pixels[i]

	def setPixel(self,row,column,color):
		idx = row * self.cols + column
		self.pixels[idx] = color

	def drawRect(self,pt1,pt2,color,filled=True):

		for r in range(pt1.r,pt2.r+1):
			for c in range(pt1.c,pt2.c+1):
				self.setPixel(r,c,color)








myGrid = Grid(7,25)


yellow = Color(255,255,0)
green = Color(0,255,0)

yellow.printColor()

print myGrid.pixels[0]

myGrid.pixels[2].printColor()

myGrid.setPixel(1,3,green)

myGrid.pixels[28].printColor()

p1 = Point(2,12)
p2 = Point(3,15)

myGrid.drawRect(p1,p2,yellow)

myGrid.printGrid()

flag = Grid(7,25)

red = Color(255,0,0)
white = Color(255,255,255)
blue = Color(0,0,255)

# draw stripes
for i in range(7):
	if i % 2 == 0:
		flag.drawRect(Point(i,0),Point(i,24),red)
	else:
		flag.drawRect(Point(i,0),Point(i,24),white)

# draw stars

for r in range(4):
	for c in range(12):
		rc = r + c
		if rc % 2 == 0:
			flag.setPixel(r,c,white)
		else:
			flag.setPixel(r,c,blue)















