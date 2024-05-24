import requests
# SunRise or SunSet

response = requests.get(url=' https://api.sunrise-sunset.org/json?lat=50.064651&lag=19.944981&formatted=0')
response.raise_for_status()
data = response.json()
result = [data['results']['sunrise'].split('T'), data['results']['sunset'].split('T')]
sunrice = result[0][1].split('+')[0]
sunset = result[1][1].split('+')[0]
