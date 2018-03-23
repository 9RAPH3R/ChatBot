# Speech to Text conversion also used Tkinter for GUI
'''
For this to work we need to download Speechrecognition and googleapiclient in python 
'''
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something!!!!")
    audio = r.listen(source)
    print("Got it!!!")
   
try:
    print("You said: " + r.recognize_google(audio))

except Exception as e:
    print(e)
