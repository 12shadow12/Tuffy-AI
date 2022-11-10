#!/usr/bin/env python3
import requests


url = 'https://v2.jokeapi.dev/joke/'
#headers = {'content-type': 'application/json',}

def getJoke(type: str='Any'):
    response = requests.get(url + type).json()
    if not response['error']:
        joke = []
        if response['type'] == 'single':
            joke.append('single')
            joke.append(response['joke'])
        elif response['type'] == 'twopart':
            joke.append(response['setup'])
            joke.append(response['delivery'])
    return joke
