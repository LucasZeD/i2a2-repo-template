"""Configuração central do projeto.

Lê variáveis de ambiente (e o arquivo .env, se existir) e as expõe como um
objeto `Settings` imutável. Nenhum segredo deve ficar escrito no código.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    llm_provider: str
    llm_model: str
    llm_api_key: str | None
    log_level: str

    @classmethod
    def from_env(cls) -> Settings:
        return cls(
            llm_provider=os.getenv("LLM_PROVIDER", "openai"),
            llm_model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
            llm_api_key=os.getenv("LLM_API_KEY") or None,
            log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Carrega o .env (sem sobrescrever variáveis já definidas) e retorna as configurações."""
    load_dotenv(override=False)
    return Settings.from_env()
