from pathlib import Path
import csv
import json
import re
from collections import defaultdict
from pyxlsb import open_workbook

ROOT = Path(__file__).resolve().parents[1]
RAW_XLSB = ROOT / "data" / "raw" / "dre-br-us-dnc-tratada.xlsb"
OUT_CSV = ROOT / "data" / "processed" / "dre-consolidado-tratado.csv"
OUT_JSON = ROOT / "data" / "processed" / "resumo-indicadores.json"

SOURCE_COLUMNS = [
    "Data da Copetencia",  # nome original no arquivo tratado
    "Recebido em Dollar",
    "Pago em Dollar",
    "País",
    "Empresa",
    "Conta",
    "Categoria",
    "Centro de custo",
    "Cliente/Fornecedor",
    "Descrição",
    "Índice tabelas separadas",
    "Índice tabelas juntas",
    "Valor recebido",
    "Valor pago",
]

OUTPUT_COLUMNS = [
    "Data da Competencia",
    "Recebido em Dollar",
    "Pago em Dollar",
    "País",
    "Empresa",
    "Conta",
    "Categoria",
    "Centro de custo",
    "Cliente/Fornecedor",
    "Descrição",
    "Índice tabelas separadas",
    "Índice tabelas juntas",
    "Valor recebido",
    "Valor pago",
]


def safe_float(value):
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def export_xlsb_to_csv():
    records = []
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    with open_workbook(str(RAW_XLSB)) as wb:
        sheet_name = wb.sheets[0]
        with wb.get_sheet(sheet_name) as sheet:
            rows = sheet.rows()
            header = [cell.v for cell in next(rows)]
            index = {name: i for i, name in enumerate(header) if name is not None}

            with OUT_CSV.open("w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(OUTPUT_COLUMNS)

                for row in rows:
                    values = [cell.v for cell in row]
                    if not values or all(value is None for value in values):
                        continue

                    output_row = []
                    for column in SOURCE_COLUMNS:
                        i = index.get(column)
                        output_row.append(values[i] if i is not None and i < len(values) and values[i] is not None else "")

                    writer.writerow(output_row)
                    records.append(output_row)

    return records


def build_summary(records):
    col = {name: i for i, name in enumerate(OUTPUT_COLUMNS)}

    receita_total = 0.0
    despesa_total = 0.0
    datas_ausentes = 0
    por_pais = defaultdict(lambda: {
        "registros": 0,
        "receita_total_usd": 0.0,
        "despesa_total_usd": 0.0,
        "resultado_usd": 0.0,
        "datas_ausentes": 0,
    })
    por_ano = defaultdict(lambda: {
        "registros": 0,
        "receita_total_usd": 0.0,
        "despesa_total_usd": 0.0,
        "resultado_usd": 0.0,
    })
    receitas_categoria = defaultdict(float)
    despesas_categoria = defaultdict(float)

    for row in records:
        receita = safe_float(row[col["Recebido em Dollar"]])
        despesa = safe_float(row[col["Pago em Dollar"]])
        pais = row[col["País"]] or "Não informado"
        categoria = row[col["Categoria"]] or "Não informado"
        data = str(row[col["Data da Competencia"]] or "").strip()

        receita_total += receita
        despesa_total += despesa
        receitas_categoria[categoria] += receita
        despesas_categoria[categoria] += despesa

        por_pais[pais]["registros"] += 1
        por_pais[pais]["receita_total_usd"] += receita
        por_pais[pais]["despesa_total_usd"] += despesa
        por_pais[pais]["resultado_usd"] += receita - despesa

        if not data:
            datas_ausentes += 1
            por_pais[pais]["datas_ausentes"] += 1

        match = re.search(r"(20\d{2})$", data)
        if match:
            ano = match.group(1)
            por_ano[ano]["registros"] += 1
            por_ano[ano]["receita_total_usd"] += receita
            por_ano[ano]["despesa_total_usd"] += despesa
            por_ano[ano]["resultado_usd"] += receita - despesa

    summary = {
        "projeto": "Criação de Dashboard para Leitura de DRE - SG Global Group",
        "registros_consolidados": len(records),
        "receita_total_usd": receita_total,
        "despesa_total_usd": despesa_total,
        "resultado_usd": receita_total - despesa_total,
        "datas_ausentes": datas_ausentes,
        "percentual_datas_ausentes": datas_ausentes / len(records) if records else 0,
        "por_pais": dict(por_pais),
        "por_ano": dict(sorted(por_ano.items())),
        "top_receitas": [
            {"categoria": categoria, "valor_usd": valor}
            for categoria, valor in sorted(receitas_categoria.items(), key=lambda item: item[1], reverse=True)[:10]
        ],
        "top_despesas": [
            {"categoria": categoria, "valor_usd": valor}
            for categoria, valor in sorted(despesas_categoria.items(), key=lambda item: item[1], reverse=True)[:10]
        ],
    }

    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    records = export_xlsb_to_csv()
    summary = build_summary(records)

    print("Base processada com sucesso.")
    print(f"Registros: {summary['registros_consolidados']:,}")
    print(f"Receita total: US$ {summary['receita_total_usd']:,.2f}")
    print(f"Despesa total: US$ {summary['despesa_total_usd']:,.2f}")
    print(f"Resultado: US$ {summary['resultado_usd']:,.2f}")
