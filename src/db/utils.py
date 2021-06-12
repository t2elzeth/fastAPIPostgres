from .init_db import metadata, engine


def create_all():
    metadata.create_all(engine)
