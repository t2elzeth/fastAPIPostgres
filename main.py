import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

metadata = sqlalchemy.MetaData()

database = databases.Database(DATABASE_URL)

users = sqlalchemy.Table(
    "authorization_user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("is_superuser", sqlalchemy.Boolean)
)

engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def connect():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class User(BaseModel):
    id: int
    email: str
    is_superuser: bool


@app.get('/users/{pk}', response_model=User)
async def get_one(pk: int):
    query = users.select().where(users.c.id == pk)
    user = await database.fetch_one(query)
    return {**user}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, use_colors=True)

# @app.post('/register/', response_model=Register)
# async def create(r: RegisterIn = Depends()):
#     query = register.insert().values(
#         name=r.name,
#         date_created=datetime.utcnow()
#     )
#     record_id = await database.execute(query)
#     query = register.select().where(register.c.id == record_id)
#     row = await database.fetch_one(query)
#     return {**row}
#
# @app.get('/register/{id}', response_model=Register)
# async def get_one(id: int):
#     query = register.select().where(register.c.id == id)
#     user = await database.fetch_one(query)
#     return {**user}
#
# @app.get('/register/', response_model=List[Register])
# async def get_all():
#     query = register.select()
#     all_get = await database.fetch_all(query)
#     return all_get
#
# @app.put('/register/{id}', response_model=Register)
# async def update(id: int, r: RegisterIn = Depends()):
#
#     query = register.update().where(register.c.id == id).values(
#         name=r.name,
#         date_created=datetime.utcnow(),
#     )
#     record_id = await database.execute(query)
#     query = register.select().where(register.c.id == record_id)
#     row = await database.fetch_one(query)
#     return {**row}
#
# @app.delete("/register/{id}", response_model=Register)
# async def delete(id: int):
#     query = register.delete().where(register.c.id == id)
#     return await database.execute(query)
