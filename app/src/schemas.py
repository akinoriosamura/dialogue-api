from pydantic import BaseModel

# request
class Text(BaseModel):
    text: str

# response
class Dialogue(BaseModel):
    dialogue: str