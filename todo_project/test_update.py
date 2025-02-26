import requests

url = "http://127.0.0.1:8000/tasks/5/"  # Změň ID na existující úkol

data = {
    "title": "Updated Task Title",
}

response = requests.put(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())