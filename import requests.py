import requests

response = requests.get("http://localhost:8000/version")
assert response.status_code == 200
assert response.json() == {"version": "1.0"}
