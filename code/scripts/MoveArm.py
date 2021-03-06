#
#
# NAO: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
#
# Reference: https://github.com/DylanZhangzzz/Cooperative-Robot-Nao/blob/Robot-code/MoveArm.py
#


# Imports
import cv2
from naoqi import ALProxy
import time

#Importing scripts
import Arm




#Testing X functions 
def movementX(IP,PORT,x,y,tts,proxy):
    Lefthand_flag=0
    Righthand_flag=0

	############
	## A column
    if y>90 and y<=158: 
        if x>150 and x<=234:
            tts.say("The target location is A 1")
            tts.say("But brick is too far, I can't pick it")
            #Arm.A1(IP,PORT,proxy)
        elif x>234 and x<=315:
            tts.say("The target location is A 2")
            #Arm.A2(IP,PORT,proxy)
            tts.say("But brick is too far, I can't pick it")
        elif x>315 and x<=396:
            tts.say("The target location is A 3")
            #Arm.A3(IP,PORT,proxy)
            tts.say("But brick is too far, I can't pick it")
        elif x>396 and x<=477:
            tts.say("The target location is A 4")
            #Arm.A4(IP,PORT,proxy)
            tts.say("But brick is too far, I can't pick it")
        else:
            tts.say("Too far I can't pick it")
       

	############
	## B column
    elif y>158 and y<=213:
        if x>140 and x<=225:
            tts.say("The target location is B 1")
            Arm.B1(IP,PORT,proxy)
            Lefthand_flag=1
        elif x>225 and x<=316:
            tts.say("The target location is B 2")
            Arm.B2(IP,PORT,proxy)
            Lefthand_flag=1
        elif x>316 and x<=407:
            tts.say("The target location is B 3")
            Arm.B3(IP,PORT,proxy)
            Righthand_flag=1
        elif x>407 and x<=500:
            tts.say("The target location is B 4")
            Arm.B4(IP,PORT,proxy)
            Righthand_flag=1
        else:
            tts.say("Too far I can't pick it")

	############
	## C column
    elif y>213 and y<=300:
        if x>120 and x<=180:
            tts.say("The target location is C 1")
            Arm.C1(IP,PORT,proxy)
            Lefthand_flag=1
        elif x>220 and x<=315:
            tts.say("The target location is C 2")
            Arm.C2(IP,PORT,proxy)
            Lefthand_flag=1
        elif x>315 and x<=419:
            tts.say("The target location is C 3")
            Arm.C3(IP,PORT,proxy)
            Righthand_flag=1
        elif x>419 and x<=530:
            tts.say("The target location is C 4")
            Arm.C4(IP,PORT,proxy)
            Righthand_flag=1
        else:
            tts.say("Too far I can't pick it")

	############
	## D column
    elif y>300 and y<=370:
        if x>74 and x<=194:
            tts.say("The target location is D 1")
            Arm.D1(IP,PORT,proxy)
            Lefthand_flag=1
        elif x>194 and x<=316:
            tts.say("The target location is D 2")
            Arm.D2(IP,PORT,proxy)
            Lefthand_flag=1
        elif x>316 and x<=438:
            tts.say("The target location is D 3")
            Arm.D3(IP,PORT,proxy)
            Righthand_flag=1
        elif x>438 and x<=550:
            tts.say("The target location is D 4")
            Arm.D4(IP,PORT,proxy)
            Righthand_flag=1
        else:
            tts.say("Too far I can't pick it")


    else:
        tts.say("Too far I can't pick it")


    return Lefthand_flag, Righthand_flag




        
