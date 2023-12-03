from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForQuestionAnswering

import warnings


app = FastAPI()
class Item(BaseModel):
    question: str
    context: str

model = ORTModelForQuestionAnswering.from_pretrained("optimum/roberta-base-squad2")
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")

onnx_qa = pipeline("question-answering", model=model, tokenizer=tokenizer)

@app.get("/")
def root():
    return "Question Answering Application"

@app.post("/predict/")
def predict(item: Item):
    """
    Question and Answering application requires
    dictionary with two keys. One of them is 'context'
    where you need to provide any text and another one is
    'question' where you need to raise a question relevant
    to the context.
    See the example below:
    curl -X 'POST' \
    'http://127.0.0.1:8000/predict/' \
    -H 'Content-Type: application/json' \
    -d '{
    "question": "What is my position?",
    "context": "Hello there, my name is Alex and I work as machine learning engineer"
    }'

    """
    pred = onnx_qa(item.question, item.context)
    return pred['answer']