# Ecommerce User Behavior API

API REST em **FastAPI** que expõe métricas e agregações de comportamento de usuários de e-commerce. Os dados vêm de uma base **PostgreSQL** (configurada para uso com **Supabase**, via Session pooler), lida com **psycopg2**.

## Como o projeto foi implementado

### Arquitetura em camadas

O código segue uma separação clássica **rota → serviço → repositório → banco**:

1. **`src/main.py`** — Instância `FastAPI`, rotas públicas de sanity check (`/` e `/health`) e inclusão do router principal.
2. **`src/api/router.py`** — Agrupa os routers de domínio (`users`, `metrics`).
3. **`src/api/routes/`** — Endpoints HTTP; cada rota valida parâmetros de query e injeta autenticação por dependência.
4. **`src/api/dependencies.py`** — `get_api_key`: exige o header `X-Api-Key` igual à variável `API_KEY` configurada no ambiente.
5. **`src/services/`** — Regras de negócio e mapeamento de parâmetros da API para funções de repositório:
   - `user_service`: `group_by` (string) → função que consulta agrupamentos na tabela `aggregations` e monta listas de objetos com `total_users`.
   - `metrics_service`: `metric` (string) → função que calcula totais/médias (ponderadas quando aplicável), churn, NPS, etc.
6. **`src/repositories/`** — SQL bruto: cada função abre conexão, executa uma query e devolve tuplas. `user_repository` e `metrics_repository` consultam predominantemente a tabela **`aggregations`**.
7. **`src/core/config.py`** — Carrega `.env` local (sem sobrescrever variáveis já definidas), expõe `Settings` (credenciais Supabase/DB, `API_KEY`, `DATABASE_EXPOSE_ERRORS`, SSL, etc.).
8. **`src/core/database.py`** — `get_connection()` monta `psycopg2.connect` com SSL, timeout e, quando possível, resolução **IPv4** (`hostaddr`) para evitar problemas de DNS/IPv6 com o pooler.

### Tratamento de erros HTTP

**`src/api/route_helpers.execute_or_http_error`** centraliza a conversão de exceções: `ValueError` → 400; falha de configuração do banco → 503; erros de conexão PostgreSQL → 503; erros de SQL/DB genéricos → 500 (com opção de expor detalhes se `DATABASE_EXPOSE_ERRORS` estiver ativo).

### Ponto de entrada do servidor

**`run.py`** importa `uvicorn` dinamicamente e sobe `src.main:app` com `reload=True` para desenvolvimento.

### Dependências

Definidas em `requirements.txt`: `fastapi`, `uvicorn`, `psycopg2-binary`, `python-dotenv` (o carregamento efetivo do `.env` está implementado manualmente em `config.py`).

---

## Configuração

Crie um arquivo `.env` na raiz do projeto (ou exporte as variáveis no ambiente). Principais variáveis:

| Variável | Descrição |
|----------|-----------|
| `SUPABASE_POOLER_HOST` | Host do Session pooler (alias aceito: `SUPABASE_DB_HOST`) |
| `SUPABASE_DB_NAME` | Nome do banco |
| `SUPABASE_DB_USER` | Usuário |
| `SUPABASE_DB_PASSWORD` | Senha |
| `SUPABASE_DB_PORT` | Porta (ex.: 5432 para Session pooler) |
| `DB_SSLMODE` | Modo SSL (padrão `require`) |
| `API_KEY` | Chave esperada no header `X-Api-Key` |
| `DATABASE_EXPOSE_ERRORS` | Se `true`/`1`/`yes`, detalhes de erro de banco podem aparecer nas respostas HTTP |

---

## Como executar

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

A documentação interativa do FastAPI fica em `/docs` (Swagger) e `/redoc`, quando o servidor estiver no ar.

---

## Endpoints (resumo)

| Método | Caminho | Autenticação | Descrição |
|--------|---------|--------------|-----------|
| GET | `/` | Não | Status do serviço |
| GET | `/health` | Não | Health check |
| GET | `/users` | `X-Api-Key` | Query `group_by`: dimensão de agrupamento (país, gênero, etc.) |
| GET | `/metrics` | `X-Api-Key` | Query `metric`: métrica agregada (padrão `total_users`) |

---

## Estrutura do repositório (`tree -L 3`, sem `__pycache__` nem `venv`)

```
.
|-- README.md
|-- requirements.txt
|-- run.py
`-- src
    |-- api
    |   |-- dependencies.py
    |   |-- route_helpers.py
    |   |-- router.py
    |   `-- routes
    |-- core
    |   |-- config.py
    |   `-- database.py
    |-- main.py
    |-- models
    |-- repositories
    |   |-- __init__.py
    |   |-- metrics_repository.py
    |   `-- user_repository.py
    `-- services
        |-- metrics_service.py
        `-- user_service.py

8 directories, 14 files
```

Para gerar a mesma árvore localmente:

```bash
tree -L 3 -I '__pycache__|venv'
```
