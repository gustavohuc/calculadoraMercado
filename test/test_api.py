from src.main import *
from fastapi.testclient import TestClient
import pytest


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_preco_unidade():
    response =  client.get("/preco_unidade/",params={"preco":10,"qtd":2})
    data = response.json()
    assert response.status_code == 200
    assert data["quantidade"] == 2
    assert data["preço por Unidade"] == 5.0
    assert data["preço total"] == 5.0


def test_preco_ovos():
    response = client.get("/preco_ovos",params={"preco":24,"qtd":12})
    data = response.json()
    assert response.status_code == 200
    assert data["Preço Total"] == "R$24.0"
    assert data["Quantidade de Ovos"] == 12
    assert data["Preço por Ovo"] == "R$2.0"
    assert data["Preço da bandeja"] == "R$24.0"


def test_preco_papel_hig():
    response = client.get("/preco_papel_hig/", params={"preco": 20, "qtd": 4, "metros": 30})
    data = response.json()
    assert response.status_code == 200
    assert data["Preço Total"] == "R$20.0"
    assert data["Quantidade de rolos"] == 4
    assert data["Preço por Pacote"] == "R$20.0"
    assert data["Preço por metro"] == "R$0.167"
    assert data["Preço por rolo"] == "R$5.0"


def test_preco_desconto():
    response = client.get("/preco_desconto/", params={"preco_original": 100, "preco_com_desconto": 80})
    data = response.json()
    assert response.status_code == 200
    assert data["Valor Total"] == 100
    assert data["Porcentagem de desconto"] == "20.0%"


def test_comparar_produtos():
    response = client.get("/comparar_produtos/", params={"preco1": 10, "qtd1": 2, "preco2": 20, "qtd2": 4})
    data = response.json()
    assert response.status_code == 200
    assert data["Produto 1 (preço unitário)"] == 5.0
    assert data["Produto 2 (preço unitário)"] == 5.0
    assert data["Mais vantajoso"] == "Produto 2"