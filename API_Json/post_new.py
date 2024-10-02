import requests

header= {
    "Accept":"text/plain",
    "Content-Type":"application/json"
}
request_payload= {
  "id": 10,
  "title": "string",
  "dueDate": "2024-08-06T11:29:32.765Z",
  "completed": True
}
response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=header, json=request_payload)

print(response.status_code)
print(response.json())
assert response.status_code == 200

#How to fetch data from response body:
data = response.json()
print(data["id"])
#assert data["id"] == 16   #gives error
assert data["id"] == 10   #Gives no error