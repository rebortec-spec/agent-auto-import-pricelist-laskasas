"""
Instalacao do projeto numa maquina nova (Windows, Linux ou macOS).

    python scripts/setup.py            # instala dependencias, pede as chaves em falta e cria a config local
    python scripts/setup.py --check    # so verifica o que falta

Pede ao utilizador cada chave em falta e guarda-a na maquina (cofre do sistema ou ficheiro 600).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

CONFIG = ROOT / "config" / "laskasas_whatsapp.json"
EXAMPLE = ROOT / "config" / "laskasas_whatsapp.example.json"


def install_deps():
    req = ROOT / "requirements.txt"
    if req.exists():
        print("A instalar dependencias...")
        subprocess.call([sys.executable, "-m", "pip", "install", "-r", str(req)])


def ensure_config(check_only):
    if CONFIG.exists():
        print(f"Config local OK: {CONFIG.name}")
        return
    if check_only:
        print(f"FALTA config/{CONFIG.name} (copia de {EXAMPLE.name})")
        return
    cfg = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    print("Config local em falta. Preenche (Enter mantem o valor entre parenteses):")
    for k in ("evolution_url", "instance", "group_jid", "group_name", "contact_name", "supervisor_phone"):
        v = input(f"  {k} [{cfg.get(k, '')}]: ").strip()
        if v:
            cfg[k] = v
    CONFIG.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Criado {CONFIG}")


def ensure_secrets(check_only):
    import getpass
    from secrets_store import REQUIRED, get_secret, set_secret
    missing = False
    for name, desc in REQUIRED.items():
        if _has(name):
            print(f"Chave {name}: OK")
            continue
        missing = True
        if check_only:
            print(f"Chave {name}: EM FALTA ({desc})")
            continue
        val = getpass.getpass(f"Chave {name} ({desc}): ").strip()
        if val:
            print(f"  guardada em: {set_secret(name, val)}")
    return not missing


def _has(name):
    import os
    from secrets_store import _keyring, _read_file, SERVICE
    if os.environ.get(name):
        return True
    kr = _keyring()
    if kr:
        try:
            if kr.get_password(SERVICE, name):
                return True
        except Exception:
            pass
    return bool(_read_file().get(name))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if not a.check:
        install_deps()
    ensure_config(a.check)
    ensure_secrets(a.check)
    for d in ("logs", "docs"):
        (ROOT / d).mkdir(exist_ok=True)
    print("Concluido." if not a.check else "Verificacao terminada.")


if __name__ == "__main__":
    main()
