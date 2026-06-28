from pathlib import Path


def criar_pastas():

    Path("input").mkdir(exist_ok=True)

    Path("output").mkdir(exist_ok=True)

    Path("logs").mkdir(exist_ok=True)