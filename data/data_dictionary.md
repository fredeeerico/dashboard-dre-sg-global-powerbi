# Dicionário de Dados

Base principal: `data/processed/dre-consolidado-tratado.csv`

A base consolidada foi gerada a partir do arquivo oficial tratado `data/raw/dre-br-us-dnc-tratada.xlsb`.

| Campo | Descrição | Uso analítico |
|---|---|---|
| Data da Competencia | Data de competência financeira. Algumas linhas da base US estavam sem data. | Análise temporal e relacionamento com calendário. |
| Recebido em Dollar | Valor recebido padronizado em dólar. | Cálculo da Receita Total. |
| Pago em Dollar | Valor pago padronizado em dólar. | Cálculo da Despesa Total. |
| País | Origem da operação: BR ou US. | Comparação entre países. |
| Empresa | Empresa/unidade relacionada à movimentação. | Filtro e segmentação operacional. |
| Conta | Conta financeira associada. | Análise contábil/financeira. |
| Categoria | Categoria da movimentação. | Top receitas, top despesas e filtro de DRE. |
| Centro de custo | Centro de custo associado. | Análise gerencial de despesas. |
| Cliente/Fornecedor | Cliente ou fornecedor identificado na base. | Rastreamento analítico. |
| Descrição | Descrição da movimentação. | Consulta detalhada. |
| Índice tabelas separadas | Índice original de controle. | Auditoria do tratamento. |
| Índice tabelas juntas | Índice após consolidação. | Auditoria do append das bases. |
| Valor recebido | Valor recebido no padrão original. | Referência de validação. |
| Valor pago | Valor pago no padrão original. | Referência de validação. |

## Observações de qualidade dos dados

- A base consolidada possui mais de 50 mil registros.
- A base US exigiu tratamento adicional por inconsistências estruturais e problemas de leitura no Power BI.
- Houve alto volume de datas ausentes na base US.
- A decisão de manter registros sem data evitou perda de informação financeira.
- Para viabilizar análise temporal, o projeto trabalhou com uma coluna de data ajustada e tabela calendário no Power BI.
