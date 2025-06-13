from pydantic import BaseModel


class Base(BaseModel):
    pass


class Users(Base):
    first_name: str
    last_name: str
    age: int


class UsersId(Users):
    id: int
