import requests
from datetime import datetime
pixela_endpoint="https://pixe.la/v1/users"
TOKEN="dfjkndvjkdsfcn"
USER_NAME="tttaenzy"
GRAPH_ID="graph1"

today=datetime.now()
GRAPH_DATE=today.strftime(("%Y%m%d"))


user_parameter={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response=requests.post(url=pixela_endpoint,json=user_parameter)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_parameter={
    "id":GRAPH_ID,
    "name":"Cycling-tracker",
    "unit":"km",
    "type":"float",
    "color":"shibafu"
}
headers={
    "X-USER-TOKEN":TOKEN
}
response2=requests.post(url=graph_endpoint,json=graph_parameter,headers=headers)
# print(response2.text)

update_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

yesterday=datetime(year=2023,month=12,day=9).strftime("%Y%m%d")

update_graph_parameter={
    "date":yesterday,
    "quantity":"7.8"
    # "optionalData": {
    #     "from":"camp5",
    #     "to":"camp3",
    #     "withFriends":"yes",
    #     "withListeningMusic":"yes",
    #     "time":"7:30am"
    # }
}
response3=requests.post(url=update_endpoint,json=update_graph_parameter,headers=headers)
# print(response3.text)

# ------------update pixel in the graph------------------
pixelUpdate_endpoint= f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday}"
pixelUpdate_parameter={
    "quantity":"3.8"
}
pixelUpdate_response=requests.put(url=pixelUpdate_endpoint, json=pixelUpdate_parameter, headers=headers)
# print(pixelUpdate_response.text)

# -------------------delete pixel in the graph-------------
#----for example deleting yesterday pixel in the graph

deletePixel_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday}"
delete_response=requests.delete(url=deletePixel_endpoint,headers=headers)
print(delete_response.text)
