import requests
from datetime import datetime

# Login Details For the pixe
TOKEN= "Token"
USERNAME= "Username"
GRAPHID = "Graph Name"
pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config ={
    "id": "graph1",
    "name": "Code Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.today()
post_config ={
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?"),
}

response =requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)


today = datetime.today()
date = today.strftime("%Y%m%d")
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"
put_data ={
    "quantity": "10.5"
}
# response =requests.put(url=put_endpoint, json=put_data, headers=headers)
# print(response.text)

today = datetime.today()
date = today.strftime("%Y%m%d")
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"
