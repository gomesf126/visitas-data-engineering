# 📊 Visitor Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75)](https://plotly.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)](https://streamlit.io/)

## 🚀 Sobre o Projeto

O projeto consiste em uma plataforma analítica de Engenharia de Dados e Business Intelligence desenvolvida para processamento, transformação e visualização de dados de visitação.

A solução foi construída utilizando:

* Python
* Pandas
* Plotly
* Streamlit
* Pipeline ETL modular
* Engenharia de Features
* Dashboards interativos

O objetivo principal é transformar dados brutos de visitantes em insights visuais e métricas analíticas para suporte à tomada de decisão.

---

# 🏗️ Arquitetura do Projeto

```text
project/
│
├── data/
│   ├── raw/                    # Dados brutos
│   ├── processed/              # Dados tratados
│   └── output/                 # Dados enriquecidos
│
├── src/
│   ├── extract/
│   │   └── extrair.py
│   │
│   ├── transform/
│   │   ├── limpeza.py
│   │   ├── features.py
│   │   ├── feature_cliente.py
│   │   ├── feature_tempo.py
│   │   ├── feature_abc.py
│   │   └── feature_churn.py
│   │
│   ├── analytics/
│   │   ├── metricas.py
│   │   └── charts.py
│   │
│   ├── pipeline/
│   │   └── pipeline.py
│   │
│   ├── load/
│   │   └── load.py
│   │
│   └── config/
│       └── paths.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# 🔄 Fluxo ETL

```text
Extract
   ↓
Cleaning
   ↓
Feature Engineering
   ↓
Analytics
   ↓
Dashboard
```

---

# 📌 Funcionalidades

## ✅ Pipeline de Dados

* Extração automatizada de dados
* Limpeza e padronização
* Tratamento de valores nulos
* Vetorização com NumPy
* Criação de features analíticas
* Separação modular das responsabilidades

---

## ✅ Dashboard Interativo

Dashboard desenvolvido com Streamlit contendo:

* Filtros dinâmicos por Ano e Mês
* Atualização automática da hora do sistema
* Cards analíticos
* Gráficos interativos com Plotly
* Layout responsivo
* Atualização automática via `streamlit_autorefresh`

---

# 📊 Indicadores do Dashboard

## Cards Analíticos

* 👥 Total de Visitantes Únicos
* 📅 Total de Visitas
* 📆 Data Atual
* ⏰ Hora Atual

---

## Gráficos Analíticos

### 📈 Fluxo Diário de Visitantes

Análise temporal do fluxo diário de visitantes.

### 🧑 Distribuição por Gênero

Visualização percentual dos visitantes por gênero.

### 🎂 Visitantes por Idade

Distribuição analítica de visitantes por faixa etária.

### 🕒 Horário de Pico

Análise dos horários com maior fluxo de visitantes.

---

# 🧠 Engenharia de Features

O projeto utiliza separação de features por domínio:

| Arquivo            | Responsabilidade                      |
| ------------------ | ------------------------------------- |
| feature_cliente.py | Regras relacionadas aos visitantes    |
| feature_tempo.py   | Datas, horários, meses e sazonalidade |
| feature_abc.py     | Curva ABC                             |
| feature_churn.py   | Recência e inatividade                |

---

# ⚡ Tecnologias Utilizadas

| Tecnologia | Finalidade                |
| ---------- | ------------------------- |
| Python     | Backend e processamento   |
| Pandas     | Manipulação de dados      |
| NumPy      | Vetorização e performance |
| Plotly     | Visualização interativa   |
| Streamlit  | Dashboard web             |
| Pathlib    | Gerenciamento de caminhos |

---

# 📦 Instalação

## 1. Clonar Repositório

```bash
git clone https://github.com/seu-repositorio
```

---

## 2. Criar Ambiente Virtual

### Linux / Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Executar Projeto

## Executar Pipeline

```bash
python main.py
```

---

## Executar Dashboard

```bash
streamlit run app.py
```

---

# 📊 Estrutura Analítica

O projeto segue princípios profissionais de:

* Alta coesão
* Baixo acoplamento
* Pipeline modular
* Responsabilidade única
* Separação entre ETL e visualização
* Reutilização de funções
* Escalabilidade analítica

---

# 📈 Próximas Melhorias

* Dashboard em tempo real
* Deploy na nuvem
* Integração com banco de dados
* API de dados
* Machine Learning
* Predição de fluxo de visitantes
* Heatmaps analíticos
* Análise de sazonalidade

---

# 👨‍💻 Autor

Desenvolvido por **Fabiano Gomes Aranha** 🚀
