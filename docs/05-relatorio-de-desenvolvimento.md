# 05 - Relatório de Desenvolvimento

## Contexto

Projeto prático da DNC com foco em análise financeira e construção de dashboard para leitura de DRE.

## Papel desempenhado

Frederico Augusto de Paula Amorim atuou como líder do projeto e executou integralmente a entrega final.

## Decisões técnicas relevantes

### 1. Separação entre base bruta e base tratada

As bases BR e US foram preservadas como origem dos dados, enquanto uma base consolidada foi criada para garantir estabilidade no Power BI.

### 2. Pré-tratamento da base US com Python

A base US apresentou inconsistências que dificultavam o carregamento no Power BI. A solução foi realizar tratamento externo com Python antes de carregar a base no modelo.

### 3. Manutenção de registros com data ausente

Em vez de excluir registros sem data, a decisão foi mantê-los para evitar perda de informação financeira.

### 4. Criação de indicadores executivos

O dashboard priorizou poucos indicadores principais:

- Receita Total
- Despesa Total
- Resultado
- Evolução no tempo
- Performance por país
- Top receitas e despesas

## Organização visual

A interface foi construída com hierarquia clara:

1. Filtros no topo
2. KPIs principais na faixa superior
3. Evolução financeira no centro
4. Rankings e comparação por país na base

## Paleta visual

- Azul escuro: autoridade e base institucional
- Laranja: destaque para Resultado
- Cinza: informações de suporte

## Progresso do projeto

- [x] Entendimento do problema de negócio
- [x] Leitura das bases BR e US
- [x] Identificação de inconsistências
- [x] Tratamento da base BR
- [x] Tratamento crítico da base US com Python
- [x] Criação da base oficial consolidada
- [x] Modelagem no Power BI
- [x] Criação das medidas DAX
- [x] Construção do dashboard
- [x] Organização do repositório para GitHub

## Próximos passos possíveis

- Publicar o dashboard no Power BI Service
- Criar página de detalhamento por categoria
- Criar alertas para variações de despesa
- Documentar medidas DAX diretamente no repositório
- Criar versão com dados reduzidos ou amostrados para distribuição pública
