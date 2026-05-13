from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_courses():
    response = client.get("/courses")

    assert response.status_code == 200