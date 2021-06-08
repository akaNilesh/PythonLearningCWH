import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(statement):
    engine.say(statement)
    engine.runAndWait()

def wishMe():
    if int(datetime.datetime.now().strftime("%H"))>=00 and int(datetime.datetime.now().strftime("%H"))<=12:
        speak("Good Morning!")
    elif int(datetime.datetime.now().strftime("%H"))>12 and int(datetime.datetime.now().strftime("%H"))<=4:
        speak("Good Evening!")
    else :
        speak("Good Evening!")
    speak("I am your assistant. How may I help you?")

def takeOrder():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 0.8
        rec.energy_threshold = 5000
        # rec.adjust_for_ambient_noise(sr.Microphone, duration=1)
        rec.operation_timeout = 1
        audio = rec.listen(source)
        try:
            print("Recognizing...")
            userRequest = rec.recognize_google(audio, language='en-in')
        except Exception as e:
            speak("I didn't understand what u said. Can you please say that again!")
            return "None"
        return userRequest


if __name__ == '__main__':
    wishMe()
    while 1:
        userCommand = takeOrder().lower()
        print(userCommand)
        if "time" in userCommand:
            currentTime= f"{datetime.datetime.now().date()}  {datetime.datetime.now().hour} hours and {datetime.datetime.now().minute} minutes"
            speak(f"Current time is {currentTime}")

        elif "wikipedia" in userCommand:
            searchString= userCommand.replace("wikipedia","")
            searchResult= wikipedia.summary(searchString,sentences=2)
            speak(f"According to wikipedia {searchResult}")

        elif "open youtube" in userCommand:
            webbrowser.open("www.youtube.com")

        elif "open google" in userCommand:
            webbrowser.open("www.google.com")

        elif "open myntra" in userCommand:
            webbrowser.open("www.myntra.com")

        elif "open amazon" in userCommand:
            webbrowser.open("www.amazon.com")

        elif "play music"  in userCommand:
            songsDir= "N:\Entertainment\mp3 Songs"
            songs= os.listdir(songsDir)
            os.startfile(os.path.join(songsDir,songs[0]))

        else:
            speak("Sorry I didn't understand what you just said. Please say that again!")