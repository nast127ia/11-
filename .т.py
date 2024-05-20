import requests

data = {"title": "Новий пост", "content": "Це контент нового посту"}
response = requests.post("http://localhost:8000/posts", json=data)
assert response.status_code == 201
expected_response = {
    "message": "Пост успішно створено",
    "post": {"id": max(post["id"] for post in response.json()["post"]) + 1, "title": "Новий пост", "content": "Це контент нового посту"},
}
assert response.json() == expected_response
