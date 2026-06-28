from pathlib import Path
from openpyxl import Workbook


def gerar_excel(dados, caminho_saida):

    wb = Workbook()

    ws = wb.active

    ws.title = "Resultado"

    ws.append([
        "Código",
        "Tipo do Débito",
        "Valor Total",
        "Arquivo"
    ])

    for item in dados:

        ws.append([
            item["codigo"],
            item["tipo"],
            item["total"],
            item["arquivo"]
        ])

    Path(caminho_saida).parent.mkdir(exist_ok=True)

    wb.save(caminho_saida)