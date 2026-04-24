from src.main import *
from unittest.mock import patch

def test_root():
    assert test() == {"Hello": "World"}

def test_funcaoteste():
    with patch("random.randint", return_value=42):
        result = funcaoteste()
    assert result == {"teste": True, "numeroAleatorio": 42}


def test_create_item():
    item_teste = Item(nome="Teste", preco=10.0)
    assert create_item == create_item()

def test_update_item_negative():
    assert not update_item(-5)

def test_update_item_positivo():
    assert update_item(10)

def teste_delete_item_negativo():
    assert not delete_item(-5)

def teste_delete_item_positivo():
    assert delete_item(10)
    
