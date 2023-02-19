from pydantic import BaseModel


class ErrorResponse(BaseModel):
    type: str
    data: str
