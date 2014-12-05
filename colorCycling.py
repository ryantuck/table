import opc, time

# here's a test comment
# here's another test comment

from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import time
import types
import os
import RPi.GPIO as GPIO
import datetime


server = OSCServer( ("192.168.1.17", 8000) )#This has to be the IP of the RaspberryPi on the network
oscClient = OSCClient()
opcClient = opc.Client('localhost:7890')

maxColor = 255

r = maxColor
g = 0
b = 0

maxNum = 175
num = 0

phase = 0
ccStep = 1

isCycling = False
stepTime = datetime.datetime.now()
stepLevel = 1

matrixWidth = 25
matrixHeight = 7

isDot = False
dotX = 0
dotY = 0
dotIndex = 0


def cycleColor():
	global r
	global g
	global b
	global maxColor
	global phase
	global stepTime

	minMaxCheck = False
	
	if (datetime.datetime.now() - stepTime).microseconds >= stepLevel*3:
		
		if phase == 0:
			# green up / red max
			g += ccStep
			minMaxCheck = checkIfMax(g)
			if minMaxCheck:
				g = 255
		elif phase == 1:
			# red down / green max
			r -= ccStep
			minMaxCheck = checkIfMin(r)
			if minMaxCheck:
				r = 0
		elif phase == 2:
			# blue up / green max
			b += ccStep
			minMaxCheck = checkIfMax(b)
			if minMaxCheck:
				b = 255
		elif phase == 3:
			# green down / blue max
			g -= ccStep
			minMaxCheck = checkIfMin(g)
			if minMaxCheck:
				g = 0
		elif phase == 4:
			# red up / blue max
			r += ccStep
			minMaxCheck = checkIfMax(r)
			if minMaxCheck:
				r = 255
		elif phase == 5:
			# blue down / red max
			b -= ccStep
			minMaxCheck = checkIfMin(b)
			if minMaxCheck:
				b = 0

		if minMaxCheck:
			updatePhase()
			
		stepTime = datetime.datetime.now()





def updatePhase():
	global phase

	phase += 1
	phase = phase % 6

def checkIfMax(var):
	global maxColor

	if var >= maxColor:
		return True
	else:
		return False

def checkIfMin(var):
	if var <= 0:
		return True
	else:
		return False








#def handle_timeout(self):
#	print ("I'm IDLE")
#This here is just to do something while the script recieves no information....
#server.handle_timeout = types.MethodType(handle_timeout, server)

# FADERS
#################################################################################################################################################

def faderR(path,tags,args,source):
	global r
	r = int(args[0])
	print "red: ", r
def faderB(path,tags,args,source):
	global g
	g = int(args[0])
	print "green: ", g
def faderG(path,tags,args,source):
	global b
	b = int(args[0])
	print "blue: ", b
def faderN(path,tags,args,source):
	global num
	num = int(args[0])
	print "num: ", num
def ccButton(path,tags,args,source):
	global isCycling
	global cycleTime
	x = int(args[0])
	if x == 1:
		isCycling = True
		cycleTime = datetime.datetime.now()
		global r
		global g
		global b
		global phase
	else:
		isCycling = False
	print "button pressed ",isCycling
def ccStepFader(path,tags,args,source):
	global ccStep
	global stepLevel
	
	ccStep = int(args[0])
	stepLevel = int(args[0])
	print "ccStep: ", ccStep

def dotButton(path,tags,args,source):
	global isDot
	x = int(args[0])
	if x == 1:
		isDot = True
	else:
		isDot = False
	print "dotButton pressed ",isDot

def dotPosition(path,tags,args,source):
	global dotX
	global dotY
	global dotIndex
	
	dotY = int(args[0])
	dotX = int(args[1])
	if dotX > 6:
		dotX=6
	dotIndex = (matrixWidth * dotX) + dotY
	print "dot X:%i Y:%i Index:%i" % (dotX,dotY,dotIndex)
	
	
#These are all the add-ons that you can name in the TouchOSC layout designer (you can set the values and directories)
server.addMsgHandler("redfader",faderR)
server.addMsgHandler("greenfader",faderG)
server.addMsgHandler("bluefader",faderB)
server.addMsgHandler("numfader",faderN)
server.addMsgHandler("colorcycle1",ccButton)
server.addMsgHandler("cyclestep",ccStepFader)
server.addMsgHandler("dotOnOff",dotButton)
server.addMsgHandler("dotXY",dotPosition)

# main loop
while True:
	# read data
	server.handle_request()
	
	if isCycling:
		cycleColor()

	pixels = [ (0,0,0) ] * maxNum
	for i in range(num):
		if i == dotIndex:
			if isDot:
				pixels[i] = (255,255,255)
			else:
				pixels[i] = (r,b,g)
		else:
			pixels[i] = (r,b,g)
	opcClient.put_pixels(pixels)
	print "r:%i g:%i b:%i num:%i " % (r,g,b,num)



server.close()
#This will kill the server when the program ends
























