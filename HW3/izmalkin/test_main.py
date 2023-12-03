from fastapi.testclient import TestClient # импортируем тестовый клиент
from main import app, Item # импортируем наше приложение и класс Item


client = TestClient(app) # создаем тестовый клиент

def test_root():
    """
    функция для тестирования корневого пути
    """
    response = client.get("/") # делаем запрос к корневому пути
    assert response.status_code == 200 # проверяем, что статус-код 200
    assert response.json() == "Question Answering Application" # проверяем, что в ответе json с ключом message и значением Question Answering Application

def test_predict():
    """
    функция для тестирования пути /predict/
    """
    item = Item(question="What is my position?", context="Hello there, my name is Alex and I work as a machine learning engineer")
    response = client.post("/predict/", json=item.model_dump())
    assert response.status_code == 200
    assert response.json() == "machine learning engineer"

