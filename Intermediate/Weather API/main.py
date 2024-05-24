import requests
from twilio.rest import Client

account_sid = 'AC2cf79d127104c54a7a1d411a61f6998d'
auth_token = '4cee1c73bad4e31bd82f312768d0ba0a'
API_KEY = '63944bab0c901bff031a349a943d1525'

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={50.064651}&lon={19.944981}&appid={API_KEY}")
response.raise_for_status()
weather_data = response.json()

will_rain = False

for i in range(len(weather_data['list'])):
    condition_code = weather_data['list'][i]['weather'][0]['id']
    if 300 < condition_code < 600:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body='It`s going to rain today, dont forget take your umbrella',from_="+19182129481", to="+48574751211")

    print(message.status)
