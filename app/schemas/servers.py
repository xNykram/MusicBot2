from pydantic import BaseModel


class Logs(BaseModel):
    id: int
    server_id: int
    server_name: str
    amount_of_users: int
    created_at: str
