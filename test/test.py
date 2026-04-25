from fastapi.testclient import TestClient
from src.main import app, db
from unittest.mock import patch

client = TestClient(app)


def setup_function():
    db.clear()


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_funcaoteste():
    with patch("src.main.random.randint", return_value=42):
        response = client.get("/teste")

    assert response.status_code == 200
    assert response.json() == {
        "teste": True,
        "numeroAleatorio": 42
    }


def test_create_item():
    response = client.post(
        "/items/1",
        json={"nome": "Teste", "preco": 10.0}
    )

    assert response.status_code == 200
    assert response.json()["item"]["nome"] == "Teste"


def test_update_item():
    client.post("/items/1", json={"nome": "Antigo", "preco": 5.0})

    response = client.put(
        "/items/1",
        json={"nome": "Novo", "preco": 15.0}
    )

    assert response.status_code == 200
    assert response.json()["item"]["nome"] == "Novo"


def test_delete_item():
    client.post("/items/1", json={"nome": "Teste", "preco": 10.0})

    response = client.delete("/items/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Item deletado"
