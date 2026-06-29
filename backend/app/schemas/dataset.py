from pydantic import BaseModel


class DatasetCreate(BaseModel):
    name: str
    owner: str
    layer: str
    description: str