from pydantic import BaseModel


class Log(BaseModel):
    unit: str
    timestamp: str

