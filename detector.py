from transformers import pipeline
detector = pipeline(model="facebook/detr-resnet-50")
detector("https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg")