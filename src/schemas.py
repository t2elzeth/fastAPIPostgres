from pydantic import BaseModel


class CreateUser(BaseModel):
    email: str
    password: str


class ShowUser(BaseModel):
    id: int
    first_name: str = None
    last_name: str = None
    email: str
