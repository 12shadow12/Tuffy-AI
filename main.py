#!/usr/bin/env python3
import time
from datetime import datetime
from multiprocessing import Process

import pyttsx3
import speech_recognition as sr
import wikipedia

import modules.canvas as canvas
import modules.greetings as greetings
import modules.jokes as jokes
import modules.weather as weather



def say(audio: str) -> None:   
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[0].id)
    tts.setProperty('rate', 200)

    tts.say(audio)
    tts.runAndWait()

# def say(audio: str, wait=False):
#     p = Process(target=init, args=(audio,))
#     p.start()
#     if(wait):
#         p.join()
#     else:
#         return p

def command(q=True) -> str:
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.pause_threshold = .6
            try:
                audio = recognizer.listen(source, 5)
            except sr.WaitTimeoutError:
                pass
                return None
            try:
                return recognizer.recognize_google(audio, language='en')
            except Exception as e:
                return None
    except Exception as e:
        say("Tuffy requires a microphone to work!")
        say("Connect a microphone and run Tuffy Aide again. Goodbye")
        exit()

def greet() -> None:
    say(greetings.greet("Donald"))

def listen():
    c = command(q=False)
    if c:
        c = c.lower()
        if "tuffy" in c or "toffee" in c or "taffy" in c:
            respondToCommand()

def respondToCommand(loop=True, c=None) -> None:
    result = ''
    if loop:
        greet()
        say("How can I help you?")
    while True:
        if not c:
            c = command()
        if c:
            c = c.lower().split(" ")
            if "weather" in c:
                i = c.index("in")
                city = ' '.join(c[i+1:])
                result = weather.Weather().getWeather(city)
                #say(result)
            elif "joke" in c:
                joke = jokes.getJoke()
                if joke[0] == 'single':
                    result = f'{joke[1]}'
                else:
                    result = f"{joke[0]} {joke[1]}"
                #say(result)
                pass
            elif "date" in c:
                date = datetime.now().strftime('%A %B %d %Y')
                result = f"The current date is {date}"
                #say(result)
            elif "time" in c:
                t = time.strftime('%H:%M', time.localtime())
                h = int(t.split(":")[0])
                post = "p m" if (h >= 12) else "a m"
                h = h%12 if h%12 > 0 else 12
                m = t.split(":")[1]
                #say(f'The current time is {h, m, post}')
                result = f'The current time is {h, m, post}'
            elif "wikipedia" in c:
                e = c.index("on")
                q = ' '.join(c[:e])
                result = wikipedia.summary(q, sentences=2)
            elif "homework" in c or ("home" in c and "work" in c) or "assignments" in c:
                assignments = canvas.getAssignments()
                for key, value in assignments.items():
                    size = "is" if len(value) == 1 else "are"
                    for v in value:
                        result += f'{v} '
                    inx = key.index('-')
                    result += f'{size} due for class {key[:inx]}\n'
            elif "goodbye" in c or "bye" in c:
                result = "goodbye"
                return result
                break
            else:
                result = "Im sorry, I do not understand that command."
            say(result)
            c = None
        if not loop:
            return result

if __name__ == '__main__':
    while True:
        listen()