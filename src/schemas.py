from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    is_superuser: bool
