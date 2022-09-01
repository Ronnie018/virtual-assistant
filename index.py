import os
import time
from playsound import playsound as ps
import speech_recognition as sr

def speak(filename, path="feedbacks"):
  filepath = f"{path}/{filename}"
  ps(filename)
  
def get_audio():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    said2 = []
    while True:
      print("end")
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source, timeout=20)
      print("listening...")
      said = ""
      try:
        said = r.recognize_google(audio, language="pt-BR")
        print(said)
        said2.append(said)
      except:
        print("some error ocurred")
        ps()
        
  return said

speak("popup.mp3", )
get_audio()
