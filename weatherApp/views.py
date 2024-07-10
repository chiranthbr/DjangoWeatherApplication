from django.shortcuts import render
import urllib.request
import json

# Create your views here.

OPENWEATHERMAP_API_KEY = '39e79c59545a3f897222433028f22f28'

def getWeather(request):

    if request.method == 'POST':
        city =request.POST.get('city')
        
        source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={OPENWEATHERMAP_API_KEY}').read().decode('utf-8')
        dataList = json.loads(source)

        data = {
            'temperature': str(int(dataList['main']['temp']) - 273) + ' C',
            'humidity': str(dataList['main']['humidity']) + ' %',
            'windSpeed': str(dataList['wind']['speed']) + ' m/s',
            'Description': dataList['weather'][0]['description'],
        }
        return render(request, 'weatherMain.html', data)
    return render(request, 'weatherMain.html', {})