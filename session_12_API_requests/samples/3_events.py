import requests
from datetime import datetime

weather_api_key = "2b4c4fe1521e93982618afd9a02eacca"
events_api_key = "6HglTAIf1EofoqT2TSwSur0sTJQtde6N"
url = f"https://app.ticketmaster.com/discovery/v2/events.json"
url_weather = f"https://api.openweathermap.org/data/2.5/onecall"


def convert_unix_timestamp_to_local(event_date):
    weather_dt = datetime.fromtimestamp(event_date)
    weather_date = weather_dt.date()
    return str(weather_date)

try:
    #call events api
    if response:
        #parse response to json
        event_location = #get event coordinates
        event_city = #get event city
        event_name = #get event name
        #set weather api call parameters
        #call weather api
        if response_weather:
            #parse response to json
            for day in json_response_weather['daily']:
                weather_date = convert_unix_timestamp_to_local(day['dt'])
                if event_date == weather_date:
                    weather_type = #get event weather
                    print(f"{event_name} - {event_city} - {event_date} - {weather_type}")
                    break
        else:
            print('Weather Response Failed')
            print(response_weather.content)
    else:
        print('Events Response Failed')
        print(response.content)
except Exception as e:
    print(e)