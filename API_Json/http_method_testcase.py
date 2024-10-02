import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data)
        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        return response

client = APIClient("https://jsonplaceholder.typicode.com/")
response = client.get("posts/1")  # Fetch post with ID 1
print(response.status_code)
print(response.json())

print("----------------")
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
print("-----------------------")

data = {
    "id": 1,
    "title": "foo",
    "body": "bar updated",
    "userId": 1
}

response = client.put("posts/1", data=data)  # Update post with ID 1
print(response.status_code)
print(response.json())


response = client.post("posts", data=data)  # Create a new post
print(response.status_code)
print(response.json())

print("-----------------------")
response = client.delete("posts/1")  # Delete post with ID 1
print(response.status_code)

