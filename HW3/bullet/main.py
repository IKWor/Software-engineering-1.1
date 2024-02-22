from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


app = FastAPI()
detector = pipeline(model="facebook/detr-resnet-50")

class Item(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/get_detector/")
def getDetecor():
    return detector("https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg")

@app.post("/detector/")
def detect(item: Item):
    return detector(item.text) 
