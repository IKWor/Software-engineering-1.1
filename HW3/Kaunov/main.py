from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/translate/")
def translate(item: Item):
    return translator(item.text)[0]
