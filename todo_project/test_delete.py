import requests

url = "http://127.0.0.1:8000/tasks/6/"  # Změň ID na existující úkol

response = requests.delete(url)

print(f"Status Code: {response.status_code}")

if response.status_code == 204:
    print("Úkol byl úspěšně smazán.")
elif response.status_code == 404:
    print("Úkol neexistuje.")
else:
    print("Něco se pokazilo:", response.text)