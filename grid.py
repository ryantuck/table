import opc, time

import tableGraphics

# testing comment from pi

opcClient = opc.Client('localhost:7890')

myGrid = tableGraphics.Grid(7,25)

blue = tableGraphics.Color(0,0,255)
purple = tableGraphics.Color(255,0,255)



p1 = tableGraphics.Point(2,2)
p2 = tableGraphics.Point(2,7)
p3 = tableGraphics.Point(4,13)
p4 = tableGraphics.Point(6,17)
p5 = tableGraphics.Point(2,20)
p6 = tableGraphics.Point(6,23)


myGrid.drawRect(p1,p2,blue)
myGrid.drawRect(p3,p4,purple)
myGrid.drawRect(p5,p6,tableGraphics.yellow)

myGrid.drawRect(tableGraphics.Point(4,0),tableGraphics.Point(6,10),blue)

flag = tableGraphics.flag

def flagToOPC():

	opcPixels = [(0,0,0)] * len(flag.pixels)

	for i in range(len(flag.pixels)):
		tmpColor = flag.pixels[i]
		opcPixels[i] = (tmpColor.r,tmpColor.g,tmpColor.b)

	opcClient.put_pixels(opcPixels)

def gridToOPC():
	opcPixels = [(0,0,0)] * len(myGrid.pixels)

	for i in range(len(myGrid.pixels)):
		tmpColor = myGrid.pixels[i]
		opcPixels[i] = (tmpColor.r,tmpColor.g,tmpColor.b)

	opcClient.put_pixels(opcPixels)

def clearGrid():
	opcPixels = [(0,0,0)] * len(myGrid.pixels)
	
	opcClient.put_pixels(opcPixels)



	
while True:
	gridToOPC()
	time.sleep(7)
	clearGrid()
	flagToOPC()
	time.sleep(7)
	clearGrid()























