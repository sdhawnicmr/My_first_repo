import requests

response = requests.get("https://reqres.in/api/users?page=2")

print(response.status_code)
print(response.text)
dict_data = response.json() #JavaScript Object Notaion
print(dict_data['data'])