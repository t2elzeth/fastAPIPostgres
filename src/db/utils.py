from .init_db import engine, metadata


def create_all():
    metadata.create_all(engine)
