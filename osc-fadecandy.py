import opc, time



from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import time
import types
import os
import RPi.GPIO as GPIO


server = OSCServer( ("192.168.1.13", 8000) )#This has to be the IP of the RaspberryPi on the network
oscClient = OSCClient()
opcClient = opc.Client('localhost:7890')

r = 0
g = 0
b = 0
num = 0
maxNum = 150

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

# while True:
# 	for i in range(numLEDs):
# 		pixels = [ (0,0,0) ] * numLEDs
# 		pixels[i] = (255, 255, 255)
# 		client.put_pixels(pixels)
# 		time.sleep(0.01)

# main loop
while True:
	# read data
	server.handle_request()
	# adjust LEDs
	pixels = [ (0,0,0) ] * maxNum
	for i in range(num):
		pixels[i] = (r,g,b)
	opcClient.put_pixels(pixels)
	print "%i %i %i %i " % (r,g,b,num)


server.close()
#This will kill the server when the program ends
























