# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

response_get = requests.get(url="https://api.sheety.co/b86cf954ccd28198f30fa922eef4ee6a/flightDeals/prices")
result = response_get.json()['prices']
array = {
    'iataCode': "TESTING"
}
response_post = requests.post(url="https://api.sheety.co/b86cf954ccd28198f30fa922eef4ee6a/flightDeals/prices",
                                  data=array)
print(response_post.text)