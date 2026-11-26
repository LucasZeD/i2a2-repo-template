from nome_do_projeto.config import Settings


def test_defaults(monkeypatch):
    for var in ("LLM_PROVIDER", "LLM_MODEL", "LLM_API_KEY", "LOG_LEVEL"):
        monkeypatch.delenv(var, raising=False)

    settings = Settings.from_env()

    assert settings.llm_provider == "openai"
    assert settings.llm_api_key is None
    assert settings.log_level == "INFO"


def test_reads_environment(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "anthropic")
    monkeypatch.setenv("LLM_API_KEY", "chave-de-teste")
    monkeypatch.setenv("LOG_LEVEL", "debug")

    settings = Settings.from_env()

    assert settings.llm_provider == "anthropic"
    assert settings.llm_api_key == "chave-de-teste"
    assert settings.log_level == "DEBUG"
