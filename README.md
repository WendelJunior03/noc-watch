# NOC Watch – Latency & Jitter Monitoring

**NOC Watch** é um backend em **Python** focado em **monitoramento de latência e jitter HTTP**, inspirado em cenários reais de **NOC / SRE / Telecom**.

O projeto simula a coleta contínua de métricas de qualidade de serviço (QoS), como **latência**, **jitter**, **perda** e **disponibilidade**, com histórico, agregações e detecção de degradação.

> Projeto desenvolvido com foco em **arquitetura de produção**, observabilidade e boas práticas de backend.

---

## 🚀 Funcionalidades

- Cadastro de **targets HTTP** (serviços monitorados)
- Coleta automática de **latência (ms)**
- Cálculo de **jitter** (variação entre medições)
- Histórico de medições
- Agregações por janela de tempo:
  - latência média
  - p95 de latência
  - jitter médio
  - taxa de perda
- Detecção de **degradação de serviço**
- Base para alertas e incidentes
- API documentada via **Swagger (OpenAPI)**

---

## 🧠 Conceitos aplicados (NOC / SRE)

- Monitoramento ativo HTTP
- Métricas de QoS (Latency & Jitter)
- Percentil p95
- Janela deslizante de análise
- Histerese para abertura/fechamento de incidentes
- Separação de responsabilidades (API / Worker)
- Arquitetura orientada a serviços

---

## 🛠️ Stack Tecnológica

- **Python 3.11+**
- **FastAPI** – API REST
- **Uvicorn** – ASGI server
- **PostgreSQL** – persistência de dados
- **Redis** – fila/cache
- **Celery** – processamento assíncrono
- **SQLAlchemy + Alembic** – ORM e migrations
- **Docker & Docker Compose**
- **Pytest** – testes automatizados

---

## 📂 Estrutura do Projeto

noc-watch/
├── app/
│ ├── api/ # Rotas da API
│ ├── core/ # Configurações, logging, segurança
│ ├── db/ # Models e sessão do banco
│ ├── services/ # Lógica de negócio (checks, stats)
│ ├── workers/ # Tasks Celery
│ └── main.py # Entry point da aplicação
├── tests/
├── alembic/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md

yaml
Copiar código

---

## ▶️ Como rodar o projeto (local)

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/WendelJunior03/noc-watch.git
cd noc-watch

2️⃣ Criar e ativar o ambiente virtual
bash
Copiar código
python -m venv .venv
source .venv/bin/activate

3️⃣ Instalar dependências
bash
Copiar código
pip install -r requirements.txt

4️⃣ Subir serviços de apoio (Postgres e Redis)
bash
Copiar código
docker compose up -d

5️⃣ Rodar a API
bash
Copiar código
python -m uvicorn app.main:app --reload --reload-dir app

📖 Documentação da API
Após subir o projeto:

Swagger UI
http://127.0.0.1:8000/docs

Health check
http://127.0.0.1:8000/health

📊 Métricas coletadas
Latency (ms) – tempo de resposta HTTP

Jitter (ms) – variação entre medições consecutivas

Loss (%) – falhas de resposta no período

Availability (%) – uptime do target

🧪 Testes
bash
Copiar código
pytest
🎯 Objetivo do Projeto
Este projeto foi desenvolvido com foco em:

Demonstração de conhecimento em backend Python

Aplicação de conceitos reais de monitoramento e SRE

Simulação de cenários comuns em ambientes telecom / NOC

Portfólio técnico para conversas profissionais e processos seletivos

📌 Roadmap
 CRUD completo de targets

 Coleta automática de métricas

 Engine de incidentes

 Alertas via webhook (Slack / Discord)

 Métricas Prometheus

 CI com GitHub Actions

 Deploy em ambiente cloud

👤 Autor
Wendel Junior
Desenvolvedor Backend Python
Foco em automação, monitoramento e sistemas distribuídos

GitHub: https://github.com/WendelJunior03

LinkedIn: https://www.linkedin.com/in/wendel-junior/
