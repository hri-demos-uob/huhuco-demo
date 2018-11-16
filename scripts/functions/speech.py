

# Imports
import argparse
import time
from naoqi import ALProxy


def Rec(IP,PORT,tts):
    data=[]
    # Creates a proxy on the speech-recognition module
    asr = ALProxy("ALSpeechRecognition",IP, PORT)
    memProxy = ALProxy("ALMemory",IP,PORT)
    asr.pause(True)
    asr.setLanguage("English")

    vocabulary = ["Green", "Yellow", "Blue", "Red","Green Brick","Pick Green Brick","Pick Up Green Brick","Please Pick Up Green Brick"]
    asr.setVocabulary(vocabulary, False)

    # Start the speech recognition engine with user Test_ASR
    #tts.say("I am listening")
    asr.subscribe("Test_ASR")
    print 'Speech recognition engine started'
    asr.pause(False)
    time.sleep(3)
    data=memProxy.getData("WordRecognized")
    asr.unsubscribe("Test_ASR")
 
    return data


def colour(IP,PORT,tts):
    while True:
        colour=Rec(IP,PORT,tts)
        brick,number=colour
        print brick,number
        if number!=-3:
            break
        else:
            continue
    return brick


