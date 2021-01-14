import requests
from django.shortcuts import render


# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5781e702dd9999353cba1bd5fe47da06'

    # getting the user input

    city = request.POST.get('city')

    data = requests.get(url.format(city)).json(
    )  #request the API data and convert the JSON to Python data types

    weather_data = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    context = {'weather': weather_data}
    return render(request, 'index.html', context)
