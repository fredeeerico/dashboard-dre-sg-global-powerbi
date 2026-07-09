# 01 - Guia de Execução

## Como abrir o dashboard

1. Abra o Power BI Desktop.
2. Carregue o arquivo:

```text
dashboard/dashboard-dre-sg-global.pbix
```

3. Caso o Power BI solicite atualização da fonte de dados, aponte para a base oficial:

```text
data/raw/dre-br-us-dnc-tratada.xlsb
```

## Como consultar a base processada

A base consolidada exportada para CSV está em:

```text
data/processed/dre-consolidado-tratado.csv
```

Ela serve para auditoria, leitura rápida e reuso em outros ambientes.

## Como reprocessar os dados

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o script:

```bash
python src/prepare_dataset.py
```

O script gera novamente:

```text
data/processed/dre-consolidado-tratado.csv
data/processed/resumo-indicadores.json
```

## Arquivos principais

| Caminho | Finalidade |
|---|---|
| `dashboard/dashboard-dre-sg-global.pbix` | Dashboard em Power BI. |
| `data/raw/dre-br-us-dnc-tratada.xlsb` | Base oficial consolidada. |
| `data/raw/dre-br-dnc-base.csv` | Base original do Brasil. |
| `data/raw/dre-us-dnc-base.csv` | Base original dos Estados Unidos. |
| `data/processed/dre-consolidado-tratado.csv` | Base tratada exportada para CSV. |
| `data/processed/resumo-indicadores.json` | Resumo dos principais indicadores. |
