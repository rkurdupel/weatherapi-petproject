from django.shortcuts import render
import requests, json
import datetime

API_KEY = '2fe213d1667649adae1130616241904'
BASE_URL = 'http://api.weatherapi.com/v1/forecast.json?'

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        city_name = request.POST.get('input_city')
        
        params = {
            'key':API_KEY,
            'q': city_name,
            'days': 14,
            'aqi': 'no',
            'alerts': 'no'
        }

        response = requests.get(BASE_URL, params = params)
        data = response.json()
        date = data['forecast']['forecastday'][0]['date']
        year, month, day = (int(x) for x in date.split('-'))
        weekday = datetime.date(year, month, day).strftime('%a')    # date to Fri (Friday) Sat, Sun
    

        context = {
            'city_name': f"{data['location']['name']}, {data['location']['country']}",
            'current_temperature': round(data['current']['temp_c']),
            'current_time': data['current']['last_updated'].split(' ')[1],
            'humidity': f"{data['current']['humidity']}%",
            'wind': f"{data['current']['wind_kph']}km/h",
            'weather_type': data['current']['condition']['text'],
            'weekday': weekday
        }

        return render(request, 'homepage.html', context)

    return render(request, 'homepage.html')



