import databases
import sqlalchemy as sa

DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

metadata = sa.MetaData()
sa.select
database = databases.Database(DATABASE_URL)

engine = sa.create_engine(DATABASE_URL)

# Tables
users = sa.Table(
    "authorization_user",
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('first_name', sa.String, nullable=True),
    sa.Column('last_name', sa.String, nullable=True),
    sa.Column('email', sa.String, unique=True),
    sa.Column('password', sa.String),
    sa.Column('is_active', sa.Boolean),
    sa.Column('is_staff', sa.Boolean),
    sa.Column('is_superuser', sa.Boolean),
    sa.Column('last_active', sa.DateTime)
)

blogs = sa.Table(
    'blogs',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String),
    sa.Column('body', sa.String)
)
