import requests


data = {
    "email": "ch.en.u4aie22060@ch.students.amrita.edu",
    "name": "Syed Ayan",
    "mobileNo":"9121734274",
    "githubUsername": "Shaiksha777",
    "rollNo": "ch.en.u4aie22060",
    "collegeName":"Amrita Vishwa Vidyapeetham",
    "accessCode": "SwuuKE"

}

resp = requests.post(
    "http://20.244.56.144/evaluation-service/register",
    json=data
)
print(resp.status_code, resp.json())
