from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_classifier_text():
    with TestClient(app) as client:
        url = "/get_classifier/"
        response = client.get(url)
        assert response.status_code == 200
