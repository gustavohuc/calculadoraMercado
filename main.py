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