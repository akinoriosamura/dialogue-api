from fastapi import FastAPI

from src import schemas
from src.nlp.dialogue_manager import DialogueManager


app = FastAPI()
dm = DialogueManager()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/dialogue', response_model=schemas.Dialogue)
async def online_prediction(data: schemas.Text):
    print("data: ", data)
    target_t = dm.get_reply(data.text)
    print("output: ", target_t)
    return {"dialogue": target_t}
