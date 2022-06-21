from fastapi import FastAPI

TAREFAS = [
        {
            "id": 1,
            "titulo": "Arrumar a cama",
            "descricao": "Arrumar a cama ao levantar de manhã e manter arrumada durante o dia",
            "estado": "Finalizado"
    }
]

app = FastAPI()


@app.get("/tarefas")
def listar():
    return TAREFAS
