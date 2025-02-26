import requests

BASE_URL = "http://127.0.0.1:8000/api/leetcode/"

#rotace pole
response = requests.post(BASE_URL + "rotate-array/", json={"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3})
print("Rotate Array:", response.json())

#nejdelší k-tý prvek
response = requests.post(BASE_URL + "kth-largest/", json={"nums": [3, 2, 1, 5, 6, 4], "k": 2})
print("K-th Largest:", response.json())

#nejdelší zvyšující se cesta
response = requests.post(BASE_URL + "longest-increasing-path/", json={"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]})
print("Longest Increasing Path:", response.json())
