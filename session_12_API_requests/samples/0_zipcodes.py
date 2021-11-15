import requests
url = 'https://api.zippopotam.us/us/33162'
response = requests.get(url)
print(response.status_code)
if response:
    print('Response OK')
else:
    print('Response Failed')