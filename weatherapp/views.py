from django.shortcuts import render
import requests
import datetime
import math


def weather(request):
    
    if request.method =='POST':
        city=request.POST.get('city')
        appid='7dffc8456d5bc572f1bb7f1ea69d83e8'
        URL='https://api.openweathermap.org/data/2.5/weather'
        info={'q':city,'appid':appid,'units':'metric'}
        r=requests.get(url=URL,params=info).json()
        day=datetime.date.today()
        data={
            
            'coordinate':str(r['coord']['lon'])+ ',' +str(r['coord']['lat']),
            "temp":str(r['main']['temp'] )+ '°C',
            'main':r['weather'][0]['main'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            "city":city,
            'day':day,

        }
    else:
        data={}


    return render(request,'weatherapp/index.html',data)
