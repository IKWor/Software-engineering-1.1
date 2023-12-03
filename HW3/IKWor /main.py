from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


app = FastAPI()
classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")

class Item(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/get_classifier/")
def getСlassifier():
    return classifier("I love this!")

@app.post("/classifier/")
def detect(item: Item):
    return classifier(item.text)
