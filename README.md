# 💳 Credit Decision Engine

Motor de decisão de crédito baseado em arquitetura de microsserviços para ingestão, validação e análise de propostas financeiras.

> **Status do Projeto:** 🚧 Em desenvolvimento ativo (Módulo `proposal-service` implementado com testes automatizados).

---

## 🏗️ Arquitetura do Projeto

O sistema foi desenhado para separar a recepção e persistência das propostas do motor de regras/análise de crédito:

```text
credit-decision-engine/
└── proposal-service/          # Microsserviço responsável pelo ciclo de vida das propostas
    ├── app/
    │   ├── core/              # Configurações de banco de dados (produção e testes)
    │   ├── models/            # Modelos ORM (SQLAlchemy)
    │   ├── schemas/           # Validação de contratos e entrada/saída (Pydantic)
    │   └── routers/           # Endpoints REST (FastAPI)
    ├── tests/
    │   ├── mocks/             # Payloads e cenários parametrizados de propostas
    │   ├── conftest.py        # Fixtures de isolamento de banco e TestClient
    │   └── test_propostas.py  # Suíte de testes de integração
    └── main.py                # Ponto de entrada da aplicação
```

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* **Framework Web:** FastAPI
* **Banco de Dados & ORM:** PostgreSQL + SQLAlchemy
* **Validação de Dados:** Pydantic
* **Testes Automatizados:** Pytest + HTTPX (via `TestClient`)

---

## ✨ Funcionalidades (`proposal-service`)

- [x] Cadastro de novas propostas de crédito (`POST /propostas`) com validação de duplicidade (`409 Conflict`).
- [x] Listagem de propostas cadastradas (`GET /propostas`).
- [x] Consulta detalhada de proposta por ID (`GET /propostas/{id}`) com tratamento de recurso não encontrado (`404 Not Found`).
- [x] Isolamento completo de ambiente de testes com banco dedicado (`credit_decision_engine_test`) e sobrescrita de dependências (`dependency_overrides`).
- [ ] Integração com fila/mensageria para análise assíncrona de score de crédito *(Próximo passo)*.

---

## ⚙️ Como Executar Localmente

### 1. Pré-requisitos
* Python 3.12 ou superior
* PostgreSQL instalado e rodando localmente

### 2. Instalação
Clone o repositório e acesse a pasta do serviço:

```bash
git clone https://github.com
cd credit-decision-engine/proposal-service
```

Crie e ative o ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 3. Configuração do Banco de Dados
Crie dois bancos no seu PostgreSQL:
* `credit_decision_engine` (Desenvolvimento/Produção)
* `credit_decision_engine_test` (Exclusivo para execução dos testes automatizados)

Configure as variáveis de ambiente (ou arquivo `.env`) com as credenciais do seu PostgreSQL:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/credit_decision_engine
TEST_DATABASE_URL=postgresql://usuario:senha@localhost:5432/credit_decision_engine_test
```

### 4. Subindo a API
```bash
uvicorn main:app --reload
```
Acesse a documentação interativa (Swagger UI) em: **`http://localhost:8000/docs`**

---

## 🧪 Executando os Testes Automatizados

O projeto utiliza **`pytest`** com **`app.dependency_overrides`** do FastAPI para redirecionar as requisições para o banco `credit_decision_engine_test` e limpar as tabelas automaticamente (`TRUNCATE`) entre cada execução, garantindo testes idempotentes e isolados.

Para rodar a suíte de testes:

```bash
pytest -v
```

---

## 📌 Endpoints Principais

| Método | Rota | Descrição | Status de Sucesso |
| :--- | :--- | :--- | :--- |
| `POST` | `/propostas` | Cria uma nova proposta de crédito | `201 Created` |
| `GET` | `/propostas` | Lista todas as propostas cadastradas | `200 OK` |
| `GET` | `/propostas/{id}` | Busca uma proposta específica pelo ID | `200 OK` |

---

## 👨‍💻 Autor

Desenvolvido por **Karina** ([@kguiga](https://github.com)).
