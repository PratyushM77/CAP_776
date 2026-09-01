import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

print(audio)

rate = engine.getProperty("rate")
engine.setProperty("rate", 160)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

engine.say("Hello Pratyush")

engine.runAndWait()
