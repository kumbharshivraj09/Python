#7d60451b6c11d03d0c0af793503acc31
import requests
API_KEY='7d60451b6c11d03d0c0af793503acc31'
city_name=input("enter a city name : ")

url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'


response=requests.get(url)
# print(response)

if response.status_code==200:
    weather_data=response.json()
    # print(weather_data)

    weather_desciption=weather_data['weather'][0]['description']
    # print(weather_desciption)

    temp=weather_data['main']['temp'] - 273.15
    print(f'weather in {city_name} : {round(temp,2)}*c with {weather_desciption}')