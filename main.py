from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/preco_unidade/")
async def preco_unidades(preco: float,qtd: int):
    preco_unitario = preco / qtd
    return {"preço total":preco_unitario,
            "quantidade:": qtd,
            "preço por Unidade": round(preco_unitario,3)
    }
@app.get("/preco_ovos/")
async def preco_ovos(preco: float,qtd: int):
    preco_duzia = (preco / qtd)*12
    preco_por_ovo = preco / qtd
    cifrao = "R$"

    return {"Preço Total" : cifrao+ str(preco),
            "Quantidade de Ovos:": qtd,
            "Preço por Ovo": cifrao+ str(round(preco_por_ovo,3)),
            "Preço da bandeja": cifrao+ str(round(preco_duzia,3))
    }
@app.get("/preco_papel_hig/")
async def preco_papel_hig(preco: float,qtd: int, metros:int):

    preco_pacote = preco
    preco_metro = preco/(metros * qtd)
    preco_rolo = preco/qtd
    cifrao = "R$"

    return {"Preço Total" : cifrao+ str(preco),
            "Quantidade de rolos": qtd,
            "Preço por Pacote": cifrao+ str(round(preco_pacote ,3)),
            "Preço por metro": cifrao+ str(round(preco_metro,3)),
            "Preço por rolo": cifrao+ str(round(preco_rolo,3))
    }
@app.get("/preco_desconto/")
async def preco_desconto(preco_original: float,preco_com_desconto: float ):
    valor_desconto= preco_original - preco_com_desconto
    porcentagem_desconto = (valor_desconto/preco_original)*100
    return{
        "Valor Total": preco_original,
        "Porcentagem de desconto": str(round(porcentagem_desconto,2))+"%"
    }


@app.get("/comparar_produtos/")
async def comparar_produtos(preco1: float, qtd1: float, preco2: float, qtd2: float):
    preco_unitario1 = preco1 / qtd1
    preco_unitario2 = preco2 / qtd2

    mais_barato = "Produto 1" if preco_unitario1 < preco_unitario2 else "Produto 2"

    return {
        "Produto 1 (preço unitário)": round(preco_unitario1, 3),
        "Produto 2 (preço unitário)": round(preco_unitario2, 3),
        "Mais vantajoso": mais_barato
    }