from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Словник для зберігання постів
posts = {
    1: {"id": 1, "title": "Перший пост", "content": "Це контент першого посту"},
    2: {"id": 2, "title": "Другий пост", "content": "Це контент другого посту"},
}

# Словник для статистики запитів
request_counts = {
    "/version": 0,
    "/posts": 0,
    "/stats": 0,
}

class PostSchema(BaseModel):
    title: str
    content: str

@app.get("/version")
def get_version():
    """
    Версія веб-застосунку
    """
    request_counts["/version"] += 1
    return {"version": "1.0"}

@app.get("/posts")
def get_all_posts():
    """
    Отримати всі пости
    """
    request_counts["/posts"] += 1
    return list(posts.values())

@app.post("/posts", status_code=201)
def create_post(post: PostSchema):
    """
    Створити новий пост
    """
    request_counts["/posts"] += 1
    new_id = max(posts.keys()) + 1
    posts[new_id] = {"id": new_id, **post.dict()}
    return {"message": "Пост успішно створено", "post": posts[new_id]}

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: PostSchema):
    """
    Оновити існуючий пост
    """
    request_counts["/posts"] += 1
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Пост не знайдено")
    posts[post_id].update(post.dict())
    return {"message": "Пост успішно оновлено", "post": posts[post_id]}

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    """
    Видалити пост
    """
    request_counts["/posts"] += 1
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Пост не знайдено")
    del posts[post_id]
    return {"message": "Пост успішно видалено"}

@app.get("/stats")
def get_request_stats():
    """
    Отримати статистику запитів
    """
    request_counts["/stats"] += 1
    return request_counts
