import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# todo: move env vars to Settings class
engine = create_engine(
    "postgresql://{}:{}@{}/{}".format(
        os.environ.get("PG_LOGIN"),
        os.environ.get("PG_PWD"),
        os.environ.get("PG_HOST"),
        os.environ.get("PG_DB"),
    ),
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
