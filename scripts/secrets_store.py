"""
Gestao de chaves/passwords do projeto (Windows, Linux e macOS).

As chaves NUNCA ficam no repositorio. Ordem de procura:
  1. Variavel de ambiente com o nome da chave.
  2. Cofre do sistema (pacote `keyring`: Credential Manager / Keychain / Secret Service).
  3. Ficheiro local do utilizador (~/.config/pricelist_laskasas/secrets.json, permissoes 600),
     usado em servidores Linux sem cofre grafico.
  4. Se nao existir e houver terminal: pede ao utilizador e guarda (3 ou 2).
     Sem terminal: falha com mensagem a pedir `python scripts/setup.py`.

Uso:
    from secrets_store import get_secret
    key = get_secret("EVOLUTION_APIKEY")
"""
import getpass
import json
import os
import stat
import sys
from pathlib import Path

SERVICE = "pricelist_laskasas"

# Chaves que o projeto precisa: nome -> descricao mostrada ao utilizador.
REQUIRED = {
    "EVOLUTION_APIKEY": "Chave da Evolution API (WhatsApp)",
}


def _secrets_file() -> Path:
    base = os.environ.get("XDG_CONFIG_HOME")
    if not base:
        base = os.path.join(os.environ.get("APPDATA") or Path.home() / ".config")
    return Path(base) / SERVICE / "secrets.json"


def _keyring():
    try:
        import keyring
        from keyring.errors import KeyringError  # noqa: F401
        backend = keyring.get_keyring()
        # backend "fail" = sem cofre utilizavel (ex.: Linux headless)
        if backend.__class__.__module__.startswith("keyring.backends.fail"):
            return None
        return keyring
    except Exception:
        return None


def _read_file() -> dict:
    p = _secrets_file()
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def set_secret(name: str, value: str) -> str:
    """Guarda a chave. Devolve onde ficou ('keyring' ou caminho do ficheiro)."""
    kr = _keyring()
    if kr:
        try:
            kr.set_password(SERVICE, name, value)
            return "keyring"
        except Exception:
            pass
    p = _secrets_file()
    p.parent.mkdir(parents=True, exist_ok=True)
    data = _read_file()
    data[name] = value
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")
    try:
        os.chmod(p, stat.S_IRUSR | stat.S_IWUSR)  # 600 (em Windows e ignorado)
    except Exception:
        pass
    return str(p)


def get_secret(name: str, prompt: bool = True) -> str:
    val = os.environ.get(name)
    if val:
        return val
    kr = _keyring()
    if kr:
        try:
            val = kr.get_password(SERVICE, name)
            if val:
                return val
        except Exception:
            pass
    val = _read_file().get(name)
    if val:
        return val
    if prompt and sys.stdin and sys.stdin.isatty():
        desc = REQUIRED.get(name, name)
        val = getpass.getpass(f"Falta a chave {name} ({desc}). Cola-a aqui (nao aparece no ecra): ").strip()
        if val:
            where = set_secret(name, val)
            print(f"Chave {name} guardada em: {where}")
            return val
    sys.exit(f"Falta a chave {name}. Corre:  python scripts/setup.py")
