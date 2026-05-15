from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_course():
    course_data = {
        "code": "SADV101",
        "name": "Advanced Testing",
        "semester": 2,
        "ects": 6,
        "lecturer": "Prof. Test"
    }

   
    response = client.post("/courses", json=course_data)

    assert response.status_code == 201

    result = response.json()

    assert "id" in result
    assert result["code"] == "SADV101"
    assert result["name"] == "Advanced Testing"
    assert result["semester"] == 2
    assert result["ects"] == 6
   

def test_list_courses():
    response = client.get("/courses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)  
 