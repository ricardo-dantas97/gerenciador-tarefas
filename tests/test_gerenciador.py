from fastapi.testclient import TestClient
from fastapi import status
from gerenciador_tarefas.gerenciador import app, TAREFAS


def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == status.HTTP_200_OK

    
def test_quando_listar_tarefas_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.headers['Content-Type'] == "application/json"


def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)


def test_quando_listar_tarefas_a_tarefa_deve_retornada_deve_possuir_id():
    TAREFAS.append(
        {
            "id": 1,
            "titulo": "Arrumar a cama",
            "descricao": "Arrumar a cama ao levantar de manhã e manter arrumada durante o dia",
            "estado": "Finalizado"
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "id" in resposta.json()[0]
    TAREFAS.clear()
