# 📊 [Nome-Do-Projeto] (ex: Visitor-Data-Engine)

[![Python Version](https://shields.io)](https://python.org)
[![Pandas](https://shields.io)](https://pydata.org)
[![Plotly](https://shields.io)](https://plotly.com)
[![Streamlit](https://shields.io)](https://streamlit.io)

Plataforma empresarial de Engenharia de Dados desenvolvida para extração, higienização, engenharia de recursos e análise preditiva de dados de visitação. O projeto utiliza uma abordagem de programação funcional aplicada a dados, estruturando transformações imutáveis através de pipelines modulares até a geração de relatórios e métricas de negócios.

---

## 🏗️ Arquitetura do Projeto (Padrão de Mercado)

A solução foi desenhada seguindo os princípios de alta coesão e baixo acoplamento. Cada etapa do processo de dados possui responsabilidade única dentro da pasta `src/`:

```text
project/
│
├── data/                       # Camadas de armazenamento dos dados
│   ├── raw/                    # CSVs brutos originais
│   ├── processed/              # Dados higienizados após limpeza inicial
│   └── output/                 # Datasets finais com todas as features aplicadas
│
├── src/                        # Código-fonte principal do ecossistema
│   ├── extract/                # Ingestão de dados
│   │   └── extract.py
│   │
│   ├── transform/              # Engenharia de Recursos e Transformação
│   │   ├── cleaning.py         # Sua função 'tratar_texto', 'tratar_nulos', etc.
│   │   ├── features.py         # Orquestração geral das transformações
│   │   ├── feature_customer.py # Sua função 'feature_cliente' (idade, região, perfil)
│   │   ├── feature_time.py     # Classificação de horários ('Hora_visita', turnos)
│   │   ├── feature_abc.py      # Lógica de classificação da curva ABC
│   │   └── feature_churn.py    # Indicadores e métricas de evasão e fidelidade
│   │
│   ├── analytics/              # Inteligência de Negócios e Dashboards
│   │   ├── metrics.py          # KPIs matemáticos e agregações
│   │   └── charts.py           # Motores dos gráficos do Plotly
│   │
│   ├── pipeline/               # Gestão do fluxo de dados (.pipe)
│   │   └── pipeline.py
│   │
│   ├── load/                   # Exportação e persistência dos dados
│   │   └── load.py
│   │
│   └── config/                 # Arquivos de configuração do sistema
│       └── paths.py            # Gerenciamento de caminhos relativos de arquivos
│
├── main.py                     # Script que executa o pipeline completo
├── requirements.txt            # Dependências das bibliotecas (Pandas, Plotly, etc.)
└── README.md                   # Documentação técnica do projeto

---

## 🔁 Fluxo de Execução do Dado (ETL)

O ciclo de vida do dado dentro da aplicação segue uma jornada linear e previsível através da orquestração do `main.py`:

```mermaid
graph TD
    A[(data/raw)] -->|extract.py| B(cleaning.py)
    B -->|data/processed| C(feature_store.py)
    C -->|feature_customer / feature_time / ...| D(load.py)
    D -->|data/output| E(analytics / metrics & charts)
```

1. **Extract (`extract.py`)**: Consome os dados brutos e os entrega de forma estruturada.
2. **Cleaning (`cleaning.py`)**: Normaliza nomenclaturas de colunas para *Title_Case*, remove caracteres especiais e trata valores nulos com termos de controle padrão.
3. **Features (`feature_*.py`)**: Aplica lógica vetorial (via `np.select` e `np.where`) para segmentar idades, horários em formato de visualização textual (como períodos de turnos e faixas `Extra`), demografia e análises preditivas de churn.
4. **Load (`load.py`)**: Escreve o dado sanitizado e enriquecido nas respectivas pastas de saída.
5. **Analytics (`metrics.py` & `charts.py`)**: Transforma dados brutos processados em insights visuais de alta fidelidade prontos para o consumo executivo.

---

## 🚀 Como Executar a Aplicação

### 1. Preparação do Ambiente
```bash
# Clone o repositório
git clone https://github.com
cd seu-repositorio

# Criação e ativação do ambiente virtual (Venv)
python -m venv .venv
source .venv/bin/activate  # No Linux/Mac
.venv\Scripts\activate     # No Windows

# Instalação das dependências de mercado
pip install -r requirements.txt
```

### 2. Executando o Pipeline Completo
Para acionar o gatilho de ponta a ponta do ecossistema de dados, basta rodar o arquivo principal na raiz do projeto:
```bash
python main.py
```
*Este comando lerá a camada `raw`, executará os scripts de limpeza, calculará as features categorizadas de clientes/tempo e salvará os resultados analíticos processados na pasta `output`.*

---

## 🛡️ Práticas de Engenharia Adotadas

* **Imutabilidade:** O DataFrame original nunca é alterado; as funções geram cópias modificadas de forma sequencial utilizando encadeamentos de `.pipe()`.
* **Segurança de Tipos:** Conversões explícitas usando `.astype()` e proteções contra falhas de strings nulas (`errors='coerce'`) garantem que o pipeline nunca quebre por variações de dados.
* **Caminhos Dinâmicos:** Utilização do `config/paths.py` com a biblioteca nativa `pathlib`, garantindo que o projeto funcione perfeitamente em qualquer sistema operacional (Windows, Linux, Mac) sem quebras de barras de diretórios.

---
Desenvolvido por **Fabiano Gomes Aranha** 🚀
# visitas-data-engineering

