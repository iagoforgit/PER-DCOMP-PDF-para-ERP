from extractor import extrair_debitos
from excel_writer import gerar_excel
from utils import criar_pastas


def main():

    criar_pastas()

    print("Lendo PDFs...")

    dados = extrair_debitos("input")

    print(f"{len(dados)} débitos encontrados.")

    gerar_excel(
        dados,
        "output/resultado.xlsx"
    )

    print("Excel gerado com sucesso!")


if __name__ == "__main__":
    main()