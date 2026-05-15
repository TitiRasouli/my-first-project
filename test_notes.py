from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_create_note():

    note_data = {
        "title": "Pytest Note",
        "content": "Testing FastAPI",
        "category": "work",
        "tags": ["work", "pytest"]
    }

    response = client.post("/notes", json=note_data)
    
    print(response.json())

    assert response.status_code == 201

    result = response.json()

    assert "id" in result
    assert result["title"] == "Pytest Note"
    assert result["category"] == "work"
def test_list_notes():

    response = client.get("/notes")

    assert response.status_code == 200

    assert isinstance(response.json(), list)
def test_create_note_missing_field():

    invalid_note = {
        "title": "Incomplete"
    }

    response = client.post("/notes", json=invalid_note)

    assert response.status_code == 422
