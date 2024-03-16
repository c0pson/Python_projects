from datetime import datetime
from api_code import API
import ascii_images
import requests
import time
import os

def print_weather(icon, city, weather, temp, feel_temp, humidity, rain_vol):
    function_map = {
        '01d': ascii_images._01d,
        '02d': ascii_images._02d,
        '03d': ascii_images._03d,
        '04d': ascii_images._04d,
        '09d': ascii_images._09d,
        '10d': ascii_images._10d,
        '11d': ascii_images._11d,
        '13d': ascii_images._13d,
        '50d': ascii_images._50d,
        '01n': ascii_images._01n,
        '02n': ascii_images._02n,
        '03n': ascii_images._03n,
        '04n': ascii_images._04n,
        '09n': ascii_images._09n,
        '10n': ascii_images._10n,
        '11n': ascii_images._11n,
        '13n': ascii_images._13n,
        '50n': ascii_images._50n,
    }
    ascii_art = function_map[icon]()
    lines = ascii_art.split('\n')
    current_time = time.time()
    current_datetime = datetime.fromtimestamp(current_time)
    time_and_location = f'''
\t\t╭─────────────────Current─weather─────────────────╮
\t\t│╭───────────────────────────────────────────────╮│
\t\t││ City: {city}{' '*(40-len(str(city)))}││
\t\t││ Time: {current_datetime.strftime('%H:%M:%S')}{' '*32}││
\t\t│╰───────────────────────────────────────────────╯│'''
    lines[1] +=  '╭──────────────────────────────╮│'
    lines[2] += f'│ {weather}{' '*(29-len(str(weather)))}││' # type: ignore
    lines[3] += f'│ Temperature: {temp}°C{' '*(14-len(str(temp)))}││' # type: ignore
    lines[4] += f'│ Feel temperature: {feel_temp}°C{' '*(9-len(str(feel_temp)))}││' # type: ignore
    lines[5] += f'│ Humidity: {humidity}%{' '*(18-len(str(humidity)))}││' # type: ignore
    lines[6] += f'│ {rain_vol}{' '*(29-len(str(rain_vol)))}││' # type: ignore
    lines[7] +=  '╰──────────────────────────────╯│'

    os.system('cls')
    print(time_and_location, end='')
    for i, item in enumerate(lines):
        if i != len(lines)-1:
            print('\t\t'+item.strip())
        else:
            print('\t\t'+item.strip(), end='')
    print('╰─────────────────────────────────────────────────╯\n')

def get_request():
    country = 'PL'
    zip_code = '41-707'
    city_name = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country}&appid={API}')
    if city_name.status_code == 200:
        data = city_name.json()
        lat = data.get('lat')
        lon = data.get('lon')
        city = data.get('name')
    else:
        print('Not found!')
        return
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric')
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        weather = weather[0].upper() + weather[1:]
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        feel_temp = data['main']['feels_like']
        humidity = data['main']['humidity']
        if 'rain' in data:
            rain_vol = data['rain']['1h']
        else:
            rain_vol = ''
        print_weather(icon, city, weather, temp, feel_temp, humidity, rain_vol)
    elif response.status_code == 400:
        print('NOT FOUND!')

def main():
    get_request()

if __name__ == "__main__":
    main()
