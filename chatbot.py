
import requests

def get_weather(city):
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json'
    headers = {'User-Agent': 'weather-app'}
    response = requests.get(url, headers=headers)
    data = response.json()
    if data:
        lat = data[0]['lat']
        lon = data[0]['lon']
        weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
        weather = requests.get(weather_url).json()['current_weather']
        return {'temperature': weather['temperature'] , 'windspeed': weather['windspeed']}
    return None

def save_history(user_message, bot_response):
    with open('chat_history.txt', 'a', encoding='utf-8') as file:
        file.write(f'You: {user_message}\n')
        file.write(f'Chatbot: {bot_response}\n')
        file.write('---\n')

print("Chatbot: Hello! How can I help you?")

while True:
    user = input('You: ')
    if user.lower() == 'quit':
        print('Chatbot: Goodbye!')
        break

    elif user in ['hi', 'hello', 'hey']:
        response = 'Hey! How are you?'
        print(f'Chatbot: {response}')
        save_history(user, response)

    elif 'how are you' in user:
        response = 'I am doing great, thanks for asking!'
        print(f'Chatbot: {response}')
        save_history(user, response)

    elif 'name' in user:
        response = 'My name is Nick Bot!'
        print(f'Chatbot: {response}')
        save_history(user, response)

    elif 'weather' in user:
        city = user.replace('weather in', '').replace('weather', '').strip()
        result = get_weather(city)
        if result is None:
            response = 'City not found!'
        else:
            temp = result['temperature']
            wind = result['windspeed']
            if temp >= 30:
                advice = 'Pretty hot! Drink plenty of water!'
            elif temp <= 10:
                advice = 'Pretty cold! Wear a jacket!'
            else:
                advice = 'Lovely weather!'
            response = f'{city} - {temp}°C, {wind} km/h. {advice}'
        print(f'Chatbot: {response}')
        save_history(user, response)

    else:
        response = "I don't understand that yet!"
        print(f'Chatbot: {response}')
        save_history(user, response)
