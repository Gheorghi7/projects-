import datetime

import requests
import webbrowser

time = datetime.datetime.now().strftime("%Y""%m""%d")
USERNAME = "gheorghi"
TOKEN = "dfhsdkjfh76892"
# quan = input('enter the number of working hours today: ')

end_point = 'https://pixe.la/v1/users'
graph_end_point = f"{end_point}/{USERNAME}/graphs"
graph_1 = f"{end_point}/{USERNAME}/graphs/graph1"
update_end_point = f"{graph_1}/{time}"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_params = {
    "id": "graph1",
    "name": "Test graph",
    "unit": "kilogram",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
value_param = {
    "date": str(time),
    "quantity": "10"
}

response = requests.post(url=graph_1,params=value_param, headers=headers)

print(response.text)
print(response.status_code)
webbrowser.open(url=f"{graph_1}.html")
