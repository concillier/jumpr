from django.shortcuts import render

import requests
import json

# Create your views here.

def home(request): 

    url = 'https://api.open-meteo.com/v1/forecast?latitude=55.68&longitude=12.57&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset&timezone=Europe%2FBerlin'

    city = 'Copenhagen'

 #2. Pull & convert the data into json

    weather = requests.get(url).json()

    return render(request, 'home.html', {
        'weather':weather
    })
