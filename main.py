from News import *
from weather import *
import datetime     # determine the date and time
from apps import *
import randfacts    # any facts
import random       # I guess its clear XP
import pywhatkit
import speech_recognition as sr   # speech recognition
import pyttsx3 as p               # text to speech conversion
import wikipedia
import pyjokes
import webbrowser

engine = p.init()                                    # its use to conver text to speech
rate = engine.getProperty('rate')
engine.setProperty('rate',170)             # speed
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)   # change voice. (0) is russian, (1) is english 'woman', (2) is english 'man'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("good morning")
    elif hour>=12 and hour<16:
        return("good afternoon")
    else:
        return("good evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()

speak("Hello sir, " + wishme() + ", i'm your voice assistant. ")
speak("Today is " + today_date.strftime("%d") + "of" + today_date.strftime("%B") + ", And it's currently" + (today_date.strftime("%H")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
# (%d) means 'day of month', (%B) means 'month name, full version', (%H = hour 00-23  and %I = 00-12), (%M is minute '00-59'), ( %p = 'AM/PM')
speak("Temperature in Bishkek is " + str(temp()) + " degree celcius " + " and with " + str(des()))
speak("How are you?")
with sr.Microphone() as source:
    r.energy_threshold = 10000                      #increses the specter of  voice. Like, if we increase the value of threshold , it will capture even the low voices
    r.adjust_for_ambient_noise(source, 1.2)          #it cencels unnecessary voices around us
    print("listening...")
    audio = r.listen(source)                        #it listens our speech
    text = r.recognize_google(audio)                #it convers our speech to text
    print(text)

if "what" and "about" in text:
    speak("I am having a good day sir")

while True:
    phrases = ["what can I do for you?", "how can I help you?"]
    speak(random.choice(phrases))

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        try:
            text2 = r.recognize_google(audio).lower()
            print(text2)
        except:
            continue
            print(text2)

    if "bye" in text2:
        speak("Goodbye, Have a nice day.")
        break

    elif "information" in text2:
        speak("you need information related to which topic?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            try:
                infor = r.recognize_google(audio)
            except:
                continue
        speak(f"searching {infor} in wikipedia")
        print(f"searching {infor} in wikipedia")

        info = wikipedia.summary(infor, 2)
        print(info)
        speak(info)

    elif "play" and "video" in text2:
        speak("which video you want me to play?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening...")
            audio = r.listen(source)
            try:
                video = r.recognize_google(audio)
            except:
                continue
        print(f"Playing video {video} on YouTube")
        speak(f"Playing video {video} on YouTube")

        pywhatkit.playonyt(video)

    elif "news" in text2:
        print("Sure sir, Now I will read for you.")
        speak("Sure sir, Now I will read for you.")

        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif "open" and "google" in text2:
        speak("Sure sir, ")
        webbrowser.open('https://google.com')

    elif "open" and "word" in text2:
        speak("Sure sir, ")
        assist = word()

    elif 'joke' in text2:
        print(pyjokes.get_joke())
        speak(pyjokes.get_joke())

    elif 'time' in text2:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time in Bishkek is'+ time)

    elif "open" and "powerpoint" in text2:
        speak("Sure sir, ")
        assist = powerpoint()

    elif "weather" in text2:
        print("Temperature in Bishkek is " + str(temp()) + " degree celcius " + " and with " + str(des()))
        speak("Temperature in Bishkek is " + str(temp()) + " degree celcius " + " and with " + str(des()))

    elif "fact" in text2:
        x = randfacts.get_fact()
        speak("sure ")
        print(x)
        speak("Did you know that, " + x)

    else:
        speak("I don't understand you, please try again")
