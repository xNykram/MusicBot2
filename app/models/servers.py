from sqlalchemy import Column, Integer, String, DateTime
from app.db.base_class import Base


class Servers(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, auto_increment=True, unique=True)
    server_id = Column(Integer)
    server_name = Column(String)
    amount_of_users = Column(Integer)
    created_at = Column(DateTime)
