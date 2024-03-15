import ascii_images
from api_code import API
import requests

def get_request():
    data_list = []
    zip_code = '41-707'
    country = 'PL'
    city_name = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country}&appid={API}')
    if city_name.status_code == 200:
        data = city_name.json()
        print(data)
        lat = data.get('lat')
        lon = data.get('lon')
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric')
    if response.status_code == 200:
        print(response.json())
    elif response.status_code == 400:
        print('NOT FOUND!')

def main():
    # get_request()
    print('DAY: ')
    ascii_images._01d()
    ascii_images._02d()
    ascii_images._03d()
    ascii_images._04d()
    ascii_images._09d()
    ascii_images._10d()
    ascii_images._11d()
    ascii_images._13d()
    ascii_images._50d()

    print('NIGHT: ')
    ascii_images._01n()
    ascii_images._02n()
    ascii_images._03n()
    ascii_images._04n()
    ascii_images._09n()
    ascii_images._10n()
    ascii_images._11n()
    ascii_images._13n()
    ascii_images._50n()

if __name__ == "__main__":
    main()
