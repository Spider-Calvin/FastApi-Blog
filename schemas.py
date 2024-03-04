# schemas is for request body schemas not database
from pydantic import BaseModel

class Blog(BaseModel):
  title: str
  body: str