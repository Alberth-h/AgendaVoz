import speech_recognition as sr
import time
import schedule
import webbrowser
import playsound
import random
import os
from gtts import gTTS
from time import ctime

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)
alexa_speak('what do you need to schedule?')
task = input("")
alexa_speak('what time?')
timee = input("")
alexa_speak('Got it!')

def event():
    alexa_speak('Hey! You need ' + task)

schedule.every().day.at(timee).do(event)

while True:
    schedule.run_pending()
    time.sleep(1)