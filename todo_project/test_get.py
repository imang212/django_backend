import requests

task_id = 1
url = f"http://127.0.0.1:8000/tasks/{task_id}/"
response = requests.get(url)

print(response.json())