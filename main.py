#!/usr/bin/env python3
import pyttsx3
import speech_recognition as sr
import weather
import greetings
from datetime import datetime
import time
import wikipedia
import canvas
import jokes


def say(audio: str) -> None:   
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[0].id)
    tts.setProperty('rate', 200)

    tts.say(audio)
    tts.runAndWait()

def command(q=True) -> str:
    recognizer = sr.Recognizer()
    command = None
    with sr.Microphone() as source:
        recognizer.pause_threshold = .6
        try:
            audio = recognizer.listen(source, 5)
        except sr.WaitTimeoutError:
            pass
            return command
        try:
            command = recognizer.recognize_google(audio, language='en')
        except:
            if q:
                say("I'm sorry, I could not understand. How may I help you?")
            return None
        return command

def greet() -> None:
    say(greetings.greet("Donald"))

def listen():
    c = command(q=False)
    if c:
        c = c.lower()
        if "tuffy" in c or "toffee" in c or "taffy" in c:
            respondToCommand()

def respondToCommand() -> None:
    greet()
    say("How can I help you?")
    while True:
        c = command()
        if c:
            c = c.lower().split(" ")
            if "weather" in c:
                i = c.index("in")
                city = ' '.join(c[i+1:])
                say(weather.Weather().getWeather(city))
            elif "joke" in c:
                joke = jokes.getJoke()
                if joke[0] == 'single':
                    say(joke[1])
                else:
                    say(joke[0])
                    say(joke[1])
                pass
            elif "date" in c:
                date = datetime.now().strftime('%A %B %d %Y')
                say(f"The current date is {date}")
            elif "time" in c:
                t = time.strftime('%H:%M', time.localtime())
                h = int(t.split(":")[0])
                post = "p m" if (h >= 12) else "a m"
                h = h%12 if h%12 > 0 else 12
                m = t.split(":")[1]
                say(f'The current time is {h, m, post}')
            elif "wikipedia" in c:
                e = c.index("on")
                q = ' '.join(c[:e])
                say(wikipedia.summary(q, sentences=2))
            elif "homework" in c or "home work" in c or "assignments" in c:
                assignments = canvas.getAssignments()
                for key, value in assignments.items():
                    size = "is" if len(value) == 1 else "are"
                    for v in value:
                        say(f'{v}')
                    inx = key.index('-')
                    say(f'{size} due for class {key[:inx]}')
            elif "goodbye" in c or "bye" in c:
                say("goodbye")
                break


if __name__ == '__main__':
    while True:
        listen()