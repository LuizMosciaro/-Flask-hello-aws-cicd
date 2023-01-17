import pytest
from application import application 

@pytest.fixture()
def app():
    app = application
    return app

def test_request_bytes(app):
    with app.test_client() as client:
        response = client.get("/")
        assert b"<h1>Hello, World!</h1>" in response.data

def test_request_text(app):
    with app.test_client() as client:
        response = client.get("/")
        assert "<h1>Hello, World!</h1>" in response.text

def test_request_status_code(app):
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
    
