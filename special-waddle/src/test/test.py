from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_root():
    result =  await root()
    yield result
    assert result == {"mensagem": "Hello", "mundo": "World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch("random.randint", return_value=42):
        result = await funcaoteste()
        yield result

    assert result == {"teste": True, "numeroAleatorio": 42}

@pytest.mark.asyncio
async def test_create_item():
    item_teste = Item(name="Teste", preco=10.0)
    result = await create_item(item_teste)
    assert create_item == result

@pytest.mark.asyncio
async def test_update_item_negativo():
    result = await update_item(-5)   
    assert not result

@pytest.mark.asyncio
async def test_update_item_positivo():
    result = await update_item(10)
    assert result   

@pytest.mark.asyncio
async def teste_delete_item_negativo():
    result = await delete_item(-5)
    assert not result

@pytest.mark.asyncio
async def teste_delete_item_positivo():
    result = await delete_item(10)
    assert result

@pytest.mark.asyncio   
async def test_delete_item_negativo():
    result = await delete_item(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_item_positivo():
    result = await delete_item(10)
    assert result
    
