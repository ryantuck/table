import opc, time

import tableGraphics


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


def gridToOPC():

	opcPixels = [(0,0,0)] * len(myGrid.pixels)

	for i in range(len(myGrid.pixels)):
		tmpColor = myGrid.pixels[i]
		opcPixels[i] = (tmpColor.r,tmpColor.b,tmpColor.g)

	opcClient.put_pixels(opcPixels)

	

gridToOPC()
























