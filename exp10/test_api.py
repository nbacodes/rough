from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict():
    res = client.post("/predict", json={"feature1": 5, "feature2": 10})
    assert res.status_code == 200
    assert res.json()["prediction"] == 15
