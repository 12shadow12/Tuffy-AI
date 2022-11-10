#!/usr/bin/env python3
import requests
import config
import strings


class Weather:

    def getWeather(self, city: str) -> dict:

        url = f'''
{strings.URLS['weather']}appid={config.APIKEYS['weather']}&q={city}&units=imperial
        '''.strip()

        response = requests.get(url).json()

        desc = response["weather"][0]["description"]
        temp = response["main"]["temp"]
        high = response["main"]["temp_max"]
        low = response["main"]["temp_min"]

        return strings.FSTRINGS["weather"].format(city, desc, temp, high, low)