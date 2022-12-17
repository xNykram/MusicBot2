from typing import Generator
from app.db.sessions import SessionLocal


def get_db() -> Generator:
    try:
        data_base = SessionLocal()
        yield data_base
    finally:
        data_base.close()
