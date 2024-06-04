from pydantic import BaseModel


class Data(BaseModel):
    phone: str
    address: str


class WriteResponseSchema(BaseModel):
    status: str
    

class CheckResponseSchema(BaseModel):
    address: str