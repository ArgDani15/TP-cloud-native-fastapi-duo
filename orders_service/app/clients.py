import os, requests

USERS_BASE_URL = os.getenv("USERS_BASE_URL", "http://users-api:8000")

def user_exists(user_id: int) -> bool:
 url = f"{USERS_BASE_URL}/users/{user_id}"
 r = requests.get(url, timeout=3)
 return r.status_code == 200
