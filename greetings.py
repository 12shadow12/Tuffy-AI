#!/usr/bin/env python3
import requests


def greet(name: str) -> str:
    response = requests.get("https://www.greetingsapi.com/random")

    t = response.json()['type']
    greeting = response.json()['greeting']
    language = response.json()['language']

    return greeting + "," +  name + '! That is ' + t + ' in ' + language