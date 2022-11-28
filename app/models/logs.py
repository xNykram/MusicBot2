from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db.base_class import Base


class Logs(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, auto_increment=True, unique=True)
    server_id = Column(Integer)
    server_name = Column(String)
    command_type = Column(String)
    music_id = Column(String)
    command_response = Column(String)
    success = Column(Boolean)
    triggered_by = Column(String)
    created_at = Column(DateTime)
