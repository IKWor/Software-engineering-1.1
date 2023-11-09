import io
import streamlit as st
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image


def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None

def load_model():
    return DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

def load_processor():
    return DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

def res(results, model):
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        st.write(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
        )


st.title('Распознование объектов на фото')
img = load_image()
if img is not None: 
    processor = load_processor()
    model = load_model()

    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)


    target_sizes = torch.tensor([img.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    result = st.button('Распознать изображение')

    if result:
        res(results, model)
