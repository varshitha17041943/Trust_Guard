from pydantic import BaseModel

class InputSchema(BaseModel):
    url: str

class OutputSchema(BaseModel):
    status: str
