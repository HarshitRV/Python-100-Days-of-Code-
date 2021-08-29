import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "logan911"
TOKEN = "efewergbbrxxbrwhnbctrx"

parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "workout911",
    "name":"Workout Graph",
    "unit":"hour",
    "type":"float",
    "color":"ichou"
}

headers =  {
    "X-USER-TOKEN":TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
print(response.text)
