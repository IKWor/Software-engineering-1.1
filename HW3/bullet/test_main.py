from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
def test_detector_photo():
    with TestClient(app) as client:
        url = "/get_detector/"
        response = client.get(url)
        assert response.status_code == 200
  
