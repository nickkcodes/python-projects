import requests

def get_coordinates(city):
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json'
    headers = {'User-Agent': 'weather-app'}
    response = requests.get(url, headers=headers)
    data = response.json()
    if data:
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon
    else:
        return None, None

def get_weather(city):
    lat, lon = get_coordinates(city)
    if lat is None:
        print('City not found!')
        return
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
    response = requests.get(url)
    data = response.json()
    weather = data['current_weather']
    print(f'Weather in {city}:')
    print(f'Temperature: {weather["temperature"]}°C')
    print(f'Wind Speed: {weather["windspeed"]} km/h')

while True:
    city = input('Enter city (or quit to exit): ')
    if city.lower() == 'quit':
        break
    get_weather(city)
