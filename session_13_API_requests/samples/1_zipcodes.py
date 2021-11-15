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