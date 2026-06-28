# PER-DCOMP-PDF-para-ERP
Automatizar a leitura de PER/DCOMP em PDF, extrair apenas as informações relevantes, validar os dados e gerar um arquivo Excel estruturado pronto para importação em ERPs como SAP, Domínio ou outros sistemas fiscais.

## Funcionalidades

- Leitura automática de múltiplos PDFs
- Extração de campos específicos
- Tratamento e padronização dos dados
- Validação das informações
- Geração automática de planilha Excel
- Registro de logs e tratamento de erros

## Fluxo

```text
PDFs
   ↓
Leitura
   ↓
Extração
   ↓
Tratamento
   ↓
Validação
   ↓
Excel
```

## Tecnologias

- Python
- Pandas
- OpenPyXL
- PDFPlumber / PyMuPDF
- Regex
- Logging

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

Coloque os PDFs na pasta `input/` e o arquivo gerado será salvo em `output/`.

## Melhorias futuras

- Interface gráfica
- Barra de progresso
- Integração com Power Automate
- Upload para SharePoint

## Aviso

Este projeto utiliza apenas documentos de exemplo e não contém informações confidenciais ou arquivos da empresa.

---

**Iago Azevedo**  
Desenvolvedor RPA | Python | Automação de Processos

