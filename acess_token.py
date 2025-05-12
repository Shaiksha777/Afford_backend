import requests

url = "http://20.244.56.144/evaluation-service/auth"
data = {
    "email": "ch.en.u4aie22060@ch.students.amrita.edu",
    "name": "syed ayan",
    "rollNo": "ch.en.u4aie22060",
    "accessCode": "SwuuKE",
    "clientID": "2d2b1a23-b84d-4e44-b9fb-11cde296e5f3",
    "clientSecret": "cJDcQvuaAUbkmzSM"
}

resp = requests.post(url, json=data)
print(resp.status_code)
print(resp.json())
