import pyttsx3
import datetime
import os

import query as query
import speech_recognition as sr
import wikipedia


import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newvoicerate = 150
engine.setProperty('rate', newvoicerate)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon Sir!")
    else:
        speak('Good Evening Sir!')

    speak('How may i help you')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return "none"
    return query

def main():

    path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print('recognizing now...')


    try:
        dest = r.recognize_google(audio)
        print('user said :' + dest)
        webbrowser.get(path).open(dest)

    except Exception as e:

        print('Error :' + str(e))



if __name__ == '__main__':
    Wishme()
    while True:
        query = takeCommand().lower()
        chpath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accorind to wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query:
            speak("I am Ela, your virtual assistant")

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.get(chpath).open("youtube.com")

        elif 'open twitch' in query:
            speak("Opening Twitch")
            webbrowser.get(chpath).open("twitch.tv")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.get(chpath).open("google.com")

        elif 'search' in query:
            speak("web address, please")
            main()
            speak("here it is")

        elif 'open meet' in query:
            speak("Opening Google Meet")
            webbrowser.get(chpath).open("meet.google.com")

        elif 'open twitter' in query:
            speak("Opening twitter")
            webbrowser.get(chpath).open("twitter.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, it is {strTime} right now")
            print(strTime)

        elif 'good' in query:
            speak(f"My pleasure Master")

        elif 'pycharm' in query:
            pypath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.2\\bin\\pycharm64.exe"
            os.startfile(pypath)

        elif 'open riot' in query:
            valpath = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(valpath)
            speak("opening Valorant")

        elif 'photoshop' in query:
            pspath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"
            os.startfile(pspath)
            speak("opening photoshop")

        elif 'illustrator' in query:
            AIpath = "C:\\Program Files\\Adobe\\Adobe Illustrator 2022\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(AIpath)
            speak("opening Illustrator")

        elif 'open chrome' in query:
            CHpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(CHpath)
            speak("opening Google Chrome")

        elif 'quit' in query:
            speak("Good bye sir!")
            quit()
