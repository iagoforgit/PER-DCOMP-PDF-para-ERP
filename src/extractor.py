from pathlib import Path
import re
import pdfplumber


def extrair_debitos(pasta_input: str):
    """
    Lê todos os PDFs da pasta e retorna uma lista de débitos encontrados.

    Retorno:
    [
        {
            "codigo": "001",
            "tipo": "CP Patronal",
            "total": "10.957,05"
        }
    ]
    """

    resultados = []

    pasta = Path(pasta_input)

    padrao = re.compile(
        r'(\d{3})\.\s+Débito\s+(.*?)\s+.*?Total\s+([\d\.,]+)',
        re.DOTALL
    )

    for pdf in pasta.glob("*.pdf"):

        texto = ""

        with pdfplumber.open(pdf) as arquivo:
            for pagina in arquivo.pages:
                conteudo = pagina.extract_text()

                if conteudo:
                    texto += conteudo + "\n"

        for codigo, tipo, total in padrao.findall(texto):

            resultados.append({
                "codigo": codigo,
                "tipo": tipo.strip(),
                "total": total,
                "arquivo": pdf.name
            })

    return resultados