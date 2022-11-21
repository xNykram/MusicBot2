from pydantic import BaseModel


class Logs(BaseModel):
    id: int
    server_id: int
    server_name: str
    command_type: str
    music_id: str
    command_response: str
    success: bool
    triggered_by: str
    created_at: str
