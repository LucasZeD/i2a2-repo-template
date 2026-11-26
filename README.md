# i2a2-repo-template

Repositório template para projetos do **I2A2 Brasil** (Institut d'Intelligence Artificielle Appliquée).

Ele segue a estrutura de projeto Python proposta no curso: um pacote em
layout `src/`, com configuração por variáveis de ambiente, testes e documentação separados.

> Para usar: clique em **Use this template** no GitHub, crie seu repositório e siga os
> [Primeiros passos](#primeiros-passos).

---

## Estrutura

```
nome-do-projeto/
├── pyproject.toml
├── README.md
├── LICENSE
├── .env.example
├── .gitignore
├── src/nome_do_projeto/
│   ├── __init__.py
│   ├── llm/
│   ├── agents/
│   ├── tools/
│   ├── skills/
│   └── config.py
├── tests/
│   └── test_config.py
└── docs/
    └── README.md
```

## O que vai em cada arquivo

### Raiz do projeto

| Arquivo | O que contém |
|---|---|
| `pyproject.toml` | Metadados do pacote (nome, versão, autor, licença), versão mínima do Python, **dependências** de execução (`dependencies`) e de desenvolvimento (`[project.optional-dependencies].dev`), além da configuração das ferramentas (`pytest`, `ruff`). Sempre que adicionar uma biblioteca (ex.: `openai`, `anthropic`, `pandas`), declare-a aqui. |
| `README.md` | Este documento: o que é o projeto, como instalar, configurar, rodar e testar. Atualize-o com a descrição do **seu** projeto ao usar o template. |
| `LICENSE` | Texto da licença **MIT**. Troque o nome/ano no copyright se necessário. |
| `.env.example` | **Modelo** das variáveis de ambiente que o projeto espera, com valores fictícios e comentários. É commitado para que qualquer pessoa saiba o que configurar. Nunca coloque segredos reais aqui. |
| `.env` *(não versionado)* | Cópia do `.env.example` com os valores reais (chaves de API etc.). Fica só na sua máquina — está no `.gitignore`. |
| `.gitignore` | Arquivos que o Git deve ignorar: `.env`, ambientes virtuais (`.venv/`), caches do Python e das ferramentas, artefatos de build e arquivos de IDE/SO. |

### `src/nome_do_projeto/` — código do pacote

O layout `src/` evita que os testes importem o código "por acidente" a partir da pasta atual: o
pacote precisa estar instalado (`pip install -e .`), exatamente como em produção.

| Caminho | O que contém |
|---|---|
| `__init__.py` | Marca a pasta como pacote Python e expõe `__version__`. Pode reexportar as classes/funções principais para facilitar imports. |
| `config.py` | Configuração central. Carrega o `.env` com `python-dotenv` e expõe um objeto imutável `Settings` (provedor e modelo de LLM, chave de API, nível de log) via `get_settings()`. Todo o resto do código lê configuração **daqui**, nunca direto de `os.environ`. Ao criar uma nova variável, adicione-a em `Settings`, no `.env.example` e em um teste. |
| `llm/` | Integração com os modelos de linguagem: clientes/adaptadores para OpenAI, Anthropic, Gemini, Ollama etc. A ideia é isolar os detalhes de cada SDK atrás de uma interface simples (ex.: `generate(prompt) -> str`), para trocar de provedor mudando só a configuração. |
| `agents/` | Os agentes propriamente ditos. Cada agente combina um LLM, um prompt de sistema e um conjunto de tools/skills para cumprir um objetivo (ex.: classificar documentos, extrair informações de arquivos, responder perguntas sobre uma base). Um módulo por agente. |
| `tools/` | Ferramentas que os agentes podem chamar: funções **determinísticas** e bem tipadas, com docstring clara (o LLM usa a descrição para decidir quando chamá-las). Ex.: ler arquivos CSV/JSON/PDF, consultar uma API ou banco de dados, fazer cálculos. |
| `skills/` | Habilidades reutilizáveis de mais alto nível: prompts, playbooks e sequências de tools que podem ser compartilhadas entre vários agentes (ex.: "resumir um documento", "gerar relatório"). |

### `tests/`

Testes automatizados com **pytest**. Espelhe a estrutura de `src/` (ex.: `tests/tools/test_leitor_csv.py`
para `src/nome_do_projeto/tools/leitor_csv.py`). O `test_config.py` já incluso mostra como testar código
que depende de variáveis de ambiente usando `monkeypatch`. Testes não devem chamar APIs pagas —
use mocks/fakes para o LLM.

### `docs/`

Documentação do projeto e entregas dos desafios: decisões de arquitetura, diagramas, relatórios,
prints e evidências. O `docs/README.md` serve de índice.

---

## Primeiros passos

### 1. Ambiente virtual (um por projeto)

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 2. Instalar o pacote em modo editável + dependências de desenvolvimento

```bash
pip install -e ".[dev]"
```

### 3. Configurar os segredos (fora do código)

```bash
cp .env.example .env   # Windows: copy .env.example .env
```

Edite o `.env` e preencha `LLM_API_KEY` e demais valores. No código:

```python
from nome_do_projeto.config import get_settings

settings = get_settings()
print(settings.llm_provider, settings.llm_model)
```

### 4. Rodar testes e lint

```bash
pytest
ruff check .
ruff format .
```

---

## Boas práticas do curso

1. **Um ambiente virtual por projeto** — `.venv/` na raiz, nunca commitado.
2. **Segredos fora do código** — tudo no `.env`, que está no `.gitignore`; só o `.env.example` vai para o Git.
3. **Git desde o primeiro commit** — commits pequenos e com mensagens descritivas.
4. **Repositório no GitHub** — os desafios pedem o link do repositório.
5. **Licença MIT** — já incluída em `LICENSE`.

## Usando este template

Depois de criar seu repositório a partir dele:

- [ ] Em `pyproject.toml`, troque `name = "nome-do-projeto"`, `description` e `authors`.
- [ ] Renomeie a pasta `src/nome_do_projeto/` para o nome do seu pacote (snake_case, ex.: `accounting_agent`) e atualize `packages` no `pyproject.toml` e os imports em `tests/`.
- [ ] Ajuste o copyright em `LICENSE`.
- [ ] Reescreva o topo deste README com a descrição do seu projeto.
- [ ] Adicione ao `pyproject.toml` as bibliotecas do provedor de LLM que for usar.

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE).
