# 02 - Metodologia e ETL

O projeto seguiu uma abordagem estruturada de BI, com etapas inspiradas em CRISP-DM e adaptadas para um fluxo de ETL financeiro.

## 1. Entendimento do negócio

A necessidade principal era criar uma leitura consolidada da DRE para apoiar decisões gerenciais.

A empresa possuía operações no Brasil e nos Estados Unidos, mas os dados estavam separados e com baixa padronização para análise executiva.

## 2. Entendimento dos dados

Foram analisadas duas bases financeiras:

- DRE BR
- DRE US

Principais problemas identificados:

- Estrutura diferente entre as bases
- Valores nulos
- Problemas de encoding
- Inconsistências de data
- Dificuldade de carregamento da base US no Power BI
- Necessidade de padronização de campos

## 3. Preparação dos dados

A preparação envolveu:

- Remoção de duplicidades
- Remoção de linhas em branco
- Preenchimento de valores nulos
- Padronização de dimensões
- Criação da coluna País
- Criação de índices de controle
- Conversão de valores para dólar
- Unificação das bases BR e US

## 4. Tratamento crítico da base US

A base US apresentou problemas de leitura no Power BI, incluindo erro de formato e inconsistências estruturais.

Para resolver o problema, foi realizado pré-tratamento com Python antes da modelagem no Power BI.

Essa decisão permitiu manter os registros relevantes e reduzir falhas no carregamento.

## 5. Base oficial

Após o tratamento, foi criada uma base consolidada oficial:

```text
@DRE BR e US - DNC TRATADA
```

No repositório, ela está disponível em:

```text
data/raw/dre-br-us-dnc-tratada.xlsb
```

## 6. Modelagem e visualização

Com a base consolidada, o projeto avançou para:

- Criação de tabela fato
- Criação de dimensões analíticas
- Construção de tabela calendário
- Criação de medidas DAX
- Desenvolvimento do dashboard executivo
