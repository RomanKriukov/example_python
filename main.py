from fastapi import FastAPI
from schemas import Users, UsersId

app = FastAPI()

users: list[UsersId] = []


@app.get("/users")
def get_users():
    if len(users) > 0:
        return users
    else:
        return {"data": "not found yet"}


@app.post("/users")
def create_user(user: Users):
    new_user = UsersId(
        id=len(users) + 1,
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age
    )
    users.append(new_user)
    return new_user


@app.get("/users/{id}")
def get_user_by_id(id: int):
    if len(users) >= id:
        for user in users:
            if user.id == id:
                return user
    else:
        return {"answer": f"user with {id=} is not exist"}
