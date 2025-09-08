from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/preco_unidade/")
def preco_unidades(preco: float,qtd: int):
    preco_unitario = preco / qtd
    return {"preço total":preco_unitario,
            "quantidade:": qtd,
            "preço por Unidade": round(preco_unitario,3)
    }