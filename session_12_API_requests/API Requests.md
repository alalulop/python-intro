# Session 12 - API Requests
In this session we will learn how to get data from an API with Python requests library.
## What is an API
Application programming interfaces, or APIs, allow different apps and services to work together and to exchange data.
### Examples
- Sharing flight information between airlines and travel sites
- Using Google Maps in a rideshare app
- Building Chatbots in a messaging service

### How it works

1. A client application initiates an API call to retrieve information—also known as a request. This request is processed from an application to the web server via the API’s Uniform Resource Identifier (URI) and includes a request verb, headers, and sometimes, a request body.
2. After receiving a valid request, the API makes a call to the external program or web server.
3. The server sends a response to the API with the requested information.
4. The API transfers the data to the initial requesting application.

![How it works](http://www.steves-internet-guide.com/wp-content/uploads/HTTP-Protocol-Basics.jpg)

APIs can provide the following functionalities: Create, Read, Update, and Delete resources

### HTTP Requests
A HTTP request has the following structure
- Method
- Header
- Body (Optional)
#### Methods
HTTP methods determine which action you’re trying to perform when making an HTTP request.
Currently, there are five available methods:
- GET
- POST
- PUT
- DELETE
- PATCH
#### Headers
HTTP headers let the client pass additional information, so that the server can tailor the response. Some examples are:
- User-Agent
- Accept
- Authorization
- [Others](https://developer.mozilla.org/en-US/docs/Glossary/Request_header)
### HTTP Response
Each request has a response. The Response consists of a

- Status code And Description
- Headers
- Optional Body message can be many lines including binary data
#### Response Status ####
- Response Status codes are split into 5 groups each group has a meaning and a three digit code.

- 1xx – Informational
- 2xx – Successful
- 3xx - Multiple Choice
- 4xx – Client Error
- 5xx - Server Error
For example a successful page request will return a 200 response code and an unsuccessful a 400 response code.
### Headers
HTTP Response headers let the server pass additional information to the client. You can find a list of available headers [here](https://developer.mozilla.org/en-US/docs/Glossary/Response_header)
### JSON Format
The response body can have different formats. The most common one is JSON (JavaScript Object Notation).
JSON is a syntax for serializing objects, arrays, numbers, strings, booleans, and null.
```JSON
Example:
{
"count": 3,
"products": [
    {
        "_id": "5bdd9d946d97be54a4dc5666",
        "name": "Book",
        "price": 100
    },
    {
        "_id": "5bdda09560e88d867454fea3",
        "name": "Mobile",
        "price": 1800
    },
    {
        "_id": "5bddbd3a3ab5bb2184a14764",
        "name": "headphones",
        "price": 300
    }
  ]
}
```
We will use JSON response format in this session.
### API Browser ###
There are many APIs available for free. You can find below two collections of APIs:
- [AWESOME APIs](https://github.com/TonnyL/Awesome_APIs) 
- [Programmable Web APIs Directory](https://www.programmableweb.com/apis/directory?page=1)

## Python requests library
Requests is the most common and simplest HTTP library for Python to send HTTP requests easily. You can get more details in the [official documentation](https://docs.python-requests.org/en/latest/) <br/>
### Pre requisites ###
1. Installation: <br/>
Create a project in PyCharm and run the following command in the terminal 
```python
pip install requests
```
2. Import
```python
import requests
```
### Making a simple request ###
For this example we are going to get info about a postal code using [Zippotam Open API](https://api.zippopotam.us/)
Make a request and check if we got a successful response
```python
import requests
url = 'https://api.zippopotam.us/us/33162'
response = requests.get(url)
print(response.status_code)
if response:
    print('Response OK')
else:
    print('Response Failed')
```
Make a request and access the data
```python
import requests
zip_code = "33162"
url = f"https://api.zippopotam.us/us/{zip_code}"
response = requests.get(url)
print(response.status_code)
if response:
    print(response.text)
    json_response = response.json()
    city = json_response['places'][0]['place name']
    country = json_response['country']
    print(f"Zip Code {zip_code} is located in {city} - {country} ")
else:
    print('Response Failed')
```

### Making a request with parameters in the header ###
For this example, we are going to request information about the weather from the [OpenWeatherMap API](https://openweathermap.org/api)
```python
import requests

url = f"https://api.openweathermap.org/data/2.5/weather"
api_key = ""
location_parameters = dict(q='Berlin,de', appid=api_key)
#url_with_params = f"https://api.openweathermap.org/data/2.5/weather?q=Berlin,de&appid={api_key}"
response = requests.get(url, params=location_parameters)

if response:
    print(response.status_code)
    print(response.text)
    json_response = response.json()
    weather_type = json_response['weather'][0]['main']
    weather_type_desc = json_response['weather'][0]['description']
    weather_temperature = json_response["main"]["temp"]
    print(f"Current weather in Berlin: {weather_type} - {weather_type_desc} - {weather_temperature}º")
else:
    print('Response Failed')
```
## Exercises
1. Print the weather only if the status code is 200. If there is an error, print the error message
2. Change the degrees to celsius (metric scale). [See API Docs]("https://openweathermap.org/current")
3. Get the weather for the current location (by geographic coordinates). [See API Docs]("https://openweathermap.org/current") <br/>
An easy way to get the coordinates is in Google Maps. Right click on a point of the map to see them.
4. A Startup about Climate Change Data Analytics just hired you. Your first task is to get a list of 10 events in Germany happening this week and display the weather forecast. For your reference, [see Ticketmaster API Docs]("https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/") and [OpenWeatherMaps Forecast API Docs]("https://openweathermap.org/forecast16")