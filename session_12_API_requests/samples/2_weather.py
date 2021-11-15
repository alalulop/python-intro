import requests

url = f"https://api.openweathermap.org/data/2.5/weather"
api_key = ""
location_parameters = dict(q='Berlin,de', units='metric', appid=api_key)

response = requests.get(url, params=location_parameters)

if response:
    print(response.status_code)
    print(response.text)
    json_response = response.json()
    weather_type = json_response['weather'][0]['main']
    weather_type_desc = json_response['weather'][0]['description']
    weather_temperature = json_response["main"]["temp"]
    print(f"Current weather in Berlin: {weather_type} - {weather_type_desc} - {weather_temperature}ºC")
else:
    print('Response Failed')