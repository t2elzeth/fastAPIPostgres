import databases
import sqlalchemy as sa

DATABASE_URL = "postgresql://t2elzeth:postgres@localhost/db"

metadata = sa.MetaData()

database = databases.Database(DATABASE_URL)

engine = sa.create_engine(DATABASE_URL)
