
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
		idx = row * 25 + column
		self.pixels[idx] = color

	# def drawLine(self,horizontal=True,row,c1,c2,color):
		
	# 	if horizontal:
	# 		for i in range(pt1,pt2+1):
	# 			self.setPixel(row,i,color)
	# 	else:
	# 		# vertical - reinterpret row as col
	# 		for i in range(pt1, pt2+1):
	# 			self.setPixel(i,row,color)


	def drawRect(self,pt1,pt2,color,filled=True):

		for r in range(pt1.r,pt2.r+1):
			for c in range(pt1.c,pt2.c+1):
				self.setPixel(r,c,color)






myGrid = Grid(7,25)

red = Color(255,0,0)
yellow = Color(255,255,0)
green = Color(0,255,0)

yellow.printColor()

print myGrid.pixels[0]

myGrid.pixels[2] = red

myGrid.pixels[2].printColor()

myGrid.setPixel(1,3,green)

myGrid.pixels[28].printColor()

p1 = Point(2,12)
p2 = Point(3,15)

myGrid.drawRect(p1,p2,yellow)

myGrid.printGrid()

















