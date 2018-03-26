import speech_recognition as sr #importing Speech_recognition module as sr to recognize
import webbrowser as wb #importing web browser to open the web browser

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
r = sr.Recognizer() #Creating a voice recorder

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) #for Noise reduction (optional)
    print("Say Something!!!!")
    audio = r.listen(source) #Listening to the voice and records it
    print("Got it!! Lets's see what happens......")
   
try:
    text = r.recognize_google(audio) #Using googleapi to recognize the audio
    print("You said: " + text)
    wb.get(chrome_path).open(text) #opens chrome 
except Exception as e:
    print(e)
