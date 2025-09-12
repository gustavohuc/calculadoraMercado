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