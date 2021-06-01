import databases
import sqlalchemy as sa

DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

metadata = sa.MetaData()

database = databases.Database(DATABASE_URL)

engine = sa.create_engine(DATABASE_URL)

# Tables
users = sa.Table(
    "authorization_user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("email", sa.String),
    sa.Column("is_superuser", sa.Boolean)
)

blogs = sa.Table(
    'blogs',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String),
    sa.Column('body', sa.String)
)
