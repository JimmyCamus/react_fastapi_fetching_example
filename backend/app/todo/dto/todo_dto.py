from pydantic import BaseModel


class TodoDto(BaseModel):
    title: str
    description: str
    is_active: bool
