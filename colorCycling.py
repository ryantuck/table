import opc, time



from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import time
import types
import os
import RPi.GPIO as GPIO


server = OSCServer( ("192.168.1.17", 8000) )#This has to be the IP of the RaspberryPi on the network
oscClient = OSCClient()
opcClient = opc.Client('localhost:7890')

maxColor = 255

r = maxColor
g = 0
b = 0

maxNum = 150
num = maxNum

phase = 0

def cycleColor():
	global r
	global g
	global b
	global maxColor
	global phase

	minMaxCheck = False

	if phase == 0:
		# green up / red max
		g += 1
		minMaxCheck = checkIfMax(g)
	elif phase == 1:
		# red down / green max
		r -= 1
		minMaxCheck = checkifMin(r)
	elif phase == 2:
		# blue up / green max
		b += 1
		minMaxCheck = checkIfMax(b)
	elif phase == 3:
		# green down / blue max
		g -= 1
		minMaxCheck = checkIfMin(g)
	elif phase == 4:
		# red up / blue max
		r += 1
		minMaxCheck = checkIfMax(r)
	elif phase == 5:
		# blue down / red max
		b -= 1
		minMaxCheck = checkIfMin(b)

	if minMaxCheck:
		updatePhase()




def updatePhase():
	global phase

	phase += 1
	phase = phase % 6

def checkIfMax(var):
	global maxColor

	if var == maxColor:
		return True
	else:
		return False

def checkIfMin(var):
	if var == 0:
		return True
	else:
		return False








def handle_timeout(self):
	print ("I'm IDLE")
#This here is just to do something while the script recieves no information....
server.handle_timeout = types.MethodType(handle_timeout, server)

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

	
#These are all the add-ons that you can name in the TouchOSC layout designer (you can set the values and directories)
server.addMsgHandler("redfader",faderR)
server.addMsgHandler("greenfader",faderG)
server.addMsgHandler("bluefader",faderB)
server.addMsgHandler("numfader",faderN)


# main loop
while True:
	# read data
	server.handle_request()
	# adjust LEDs
	cycleColor()
	pixels = [ (0,0,0) ] * maxNum
	for i in range(num):
		pixels[i] = (r,b,g)
	opcClient.put_pixels(pixels)
	print "r:%i g:%i b:%i num:%i " % (r,g,b,num)


server.close()
#This will kill the server when the program ends
























