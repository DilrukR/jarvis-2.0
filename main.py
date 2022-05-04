import pyttsx3
import pyautogui as gui
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import wolframalpha
client = wolframalpha.Client('TW8HXV-5U4YAY9EEA')







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour<=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good Evening")

    speak("I Am Jarvis sir. please tell me how me i help you")

def takeCommand():
    #it takes microphone input from user and returns string outputs
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
      query =takeCommand().lower()

      #take commonds in query
      if 'wikipedia' in query:
          speak("Searching..")
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query,sentences=2)
          speak("According to wikipeadia")
          print(results)
          speak(results)

      elif 'open youtube'in query:
          webbrowser.open("youtube.com")


      elif 'play music' in query:
          music_dir = "E:\\music\\english"
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[9]))

      elif 'tv series hello' in query:
          halo_dir ="E:\\tv series\\Halo"
          hs = os.listdir(halo_dir)
          os.startfile(os.path.join(halo_dir,hs[1]))

      elif 'what is the time' in query:
          startTime = datetime.datetime.now().strftime("%H:%M")
          speak(f"Sir,the time is{startTime}")


      elif 'who is doll' in query:
          speak("ruchini gimhara mediwaka is your life")

