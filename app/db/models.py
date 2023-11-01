from sqlalchemy import Column, Integer, String, DateTime

from app.db.base_class import Base


class Logs(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    command_name = Column(String)
    message = Column(String)
    hashed_url = Column(String)
    created_at = Column(DateTime)