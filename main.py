import sys
import PyPDF2
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import wolframalpha
import psutil
import speedtest
import requests
import PySimpleGUI as sg

client = wolframalpha.Client('TW8HXV-5U4YAY9EEA')



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif hour <= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("Good Evening")

    speak("I Am Jarvis sir. please tell me how me i help you")


def anyother():
    speak("do you have any other work me to do")


def pdf_reader():
    book = open('D:\\Campus lectures\\Second Year\\Information System Management\\Chapter 01 MIS Student version.pdf',
                'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number..."))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def takeCommand():
    # it takes microphone input from user and returns string outputs
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def Weather_focast():
    speak('please tell me the location sir')

    location = takeCommand().lower()
    Api = 'ab49e8a59d02773c9610b303501f43e0'

    api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={Api}"

    api_req = requests.get(api_link)
    api_data = api_req.json()

    if api_data['cod'] == '404':
        speak("city is not clear sir please enter it again")

    else:
        temp_city = ((api_data['main']['temp']) - 273.15)

        weather_desc = api_data['weather'][0]['description']

        print(f"{location}'s Temperature is {temp_city} celcious and weather mostly like {weather_desc}")

        speak(f"{location}'s Temperature is {temp_city} celcious and weather mostly like {weather_desc}")

def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning")

    elif hour <= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("Good Evening")

    speak("I Am Jarvis sir. please tell me how me i help you")

def taskExecution():
    while True:
        query = takeCommand().lower()

        # take commands in query
        if 'wikipedia' in query:
            speak("Searching..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipeadia")
            print(results)
            speak(results)
            speak("do you have any other work me to do")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("do you have any other work me to do")

        elif 'play some music' in query:
            music_dir = "E:\\music\\english"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("do you have any other work me to do")

        #     elif 'namaste' in query: I make this for

        

        elif 'what is the time' in query:
            startTime = datetime.datetime.now().strftime("%H%M")
            speak(f"Sir,the time is{startTime}")
            anyother()

        elif 'how much power left' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir your system has {percentage} percent battery")
            anyother()

        elif 'internet speed' in query:

            speak(f"please wait sir i will chek it")

            st = speedtest.Speedtest()
            dl = st.download()
            ul = st.upload()
            speak(f"sir you have {dl} bit per second download speed and {ul} per second upload speed ")

        elif 'read book' in query:
            pdf_reader()

        elif 'weather' in query:

            Weather_focast()

        elif 'how are you' in query:
            speak("i am fine sir , how about you?")

        elif 'i am fine' in query:
            speak("awesome")
            speak("do you have any work me to do sir")

        elif 'go sleep' in query:
            speak('okay sir i am going to sleep but you can call me anytime')
            break

        elif 'no thanks' in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()




if __name__ == "__main__":

    while True:
        permission = takeCommand()
        if "wake up" in permission:
            wishme()
            taskExecution()
        elif "goodbye" in permission:
            sys.exit()
