import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Nitika!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Nitika!")
    else:
        speak("Good Evening Nitika!")

    speak("I am your Desktop Assistant, Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninzing...")
        query = r.recognize_google(audio,language='en=in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again Please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while(True):
        query = takeCommand().lower()
        #logic on executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences =2)
            speak('According to wikipedia...')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

        elif 'play music' in query:
            music_dir = 'F:\\songs\\mp3'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'friends' in query:
            fdir = 'F:\\movies\\friends\\Friends Season 6'
            epi = os.listdir(fdir)
            print(epi)
            os.startfile(os.path.join(fdir,random.choice(epi)))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Nitika, the time is {strtime}")

        elif 'the date' in query:
            strdate = datetime.datetime.now().date()
            speak(f"Nitika, the date is {strdate}")

        elif 'open code' in query:
            code_path = "C:\\Program Files\\JetBrains\PyCharm Community Edition 2021.3\\bin\pycharm64.exe"
            os.startfile(code_path)

        elif 'quit' in query:
            exit()










