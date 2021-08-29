import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "wolverine911"
TOKEN = os.environ.get("pixelaToken")
GRAPH_ID = "studygraph911"

# POST
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
    "id": "studygraph911",
    "name":"Coding Graph",
    "unit":"hour",
    "type":"float",
    "color":"ichou"
}

graph_headers =  {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config,graph_headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/studygraph911"

post_params = {
    "date":"20210828",
    "quantity":"5",
}

header = {
    "X-USER-TOKEN":TOKEN
}

response_post = requests.post(url=post_endpoint,json=post_params,headers=header)
print(response_post.text)

# PUT
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210828"
put_params = {
    "quantity":"7",
}
# response_put = requests.put(url=put_endpoint,json=put_params,headers=header)
# print(response_put.text)

#DELETE
del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210828"
# response_del = requests.delete(url=del_endpoint,headers=header)
# print(response_del.text)