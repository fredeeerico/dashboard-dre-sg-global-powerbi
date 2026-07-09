# 03 - Modelagem e Indicadores

## Estrutura analítica

O modelo foi estruturado com uma tabela principal de movimentações financeiras e dimensões para análise gerencial.

## Tabela fato

Principais campos utilizados:

- Data de Competência
- Receita em dólar
- Despesa em dólar
- País
- Empresa
- Conta
- Categoria
- Centro de custo
- Cliente/Fornecedor
- Descrição

## Dimensões

As principais dimensões analíticas foram:

- País
- Empresa
- Conta
- Categoria
- Centro de custo
- Cliente/Fornecedor
- Calendário

## Tratamento de datas

A base US possuía alto volume de datas ausentes. Para evitar perda de informação financeira, os registros foram mantidos e o modelo utilizou uma estratégia de data ajustada para permitir análise temporal no Power BI.

## Medidas DAX principais

As principais medidas do dashboard foram:

```DAX
Receita Total = SUM(Tabela[Recebido em Dollar])
```

```DAX
Despesa Total = SUM(Tabela[Pago em Dollar])
```

```DAX
Resultado = [Receita Total] - [Despesa Total]
```

## Indicadores do dashboard

- Receita Total
- Despesa Total
- Resultado
- Evolução financeira ao longo do tempo
- Comparação por país
- Principais fontes de receita
- Principais despesas

## Design analítico

A tela foi construída com foco executivo:

- KPIs em destaque na parte superior
- Filtros simples no topo
- Gráfico temporal no centro
- Rankings de receita e despesa na parte inferior
- Comparação entre países para leitura gerencial
