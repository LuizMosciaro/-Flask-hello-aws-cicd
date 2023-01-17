import pytest
import application as Application

@pytest.fixture()
def app():
    app = Application.application
    return app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_request_bytes(client):
    response = client.get("/")
    assert b"<h1>Hello, World!</h1>" in response.data

def test_request_text(client):
    response = client.get("/")
    assert "<h1>Hello, World!</h1>" in response.text

def test_request_status_code(client):
    response = client.get("/")
    assert response.status_code == 200
    