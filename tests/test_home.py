from application import application 

with application.test_client() as client:
    response = client.get("/")
    assert b"<h1>Hello, World!</h1>" in response.data

with application.test_client() as client:
    response = client.get("/")
    assert "<h1>Hello, World!</h1>" in response.text

with application.test_client() as client:
    response = client.get("/")
    assert response.status_code == 200
    
