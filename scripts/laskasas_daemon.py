"""
Servico de fundo do projeto Pricelist Laskasas (funciona em Windows e macOS).

O que faz, em loop:
- Le as mensagens do grupo "Pricelist Laskasas" (group_jid em config/laskasas_whatsapp.json).
- Regista em docs/inbox_laskasas.jsonl cada mensagem nova de participantes externos.
- Avisa o Rui (supervisor_phone) quando ha mensagem nova de fora.
- NAO responde sozinho nem envia conteudo gerado: as respostas sao feitas pelo agente.
- Nunca fala com contactos individuais nem com outros grupos.

Requisitos: variavel de ambiente EVOLUTION_APIKEY.
Arranque manual:  python scripts/laskasas_daemon.py
"""
import json
import logging
import os
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from secrets_store import get_secret  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "laskasas_whatsapp.json"
STATE_PATH = ROOT / "config" / "laskasas_daemon_state.json"
INBOX_PATH = ROOT / "docs" / "inbox_laskasas.jsonl"
LOG_PATH = ROOT / "logs" / "laskasas_daemon.log"
POLL_SECONDS = 60
STATE_LIMIT = 1000

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
INBOX_PATH.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    handlers=[logging.FileHandler(LOG_PATH, encoding="utf-8"), logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger("laskasas")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def api(cfg, key, method, path, payload=None):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{cfg['evolution_url']}{path}",
        data=data,
        method=method,
        headers={"apikey": key, "Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_seen():
    if STATE_PATH.exists():
        try:
            return list(json.loads(STATE_PATH.read_text(encoding="utf-8")))
        except (ValueError, OSError):
            pass
    return []


def save_seen(ids):
    STATE_PATH.write_text(json.dumps(ids[-STATE_LIMIT:]), encoding="utf-8")


def message_text(m):
    msg = m.get("message") or {}
    ext = msg.get("extendedTextMessage") or {}
    return msg.get("conversation") or ext.get("text") or ""


def run():
    cfg = load_config()
    key = get_secret(cfg["apikey_env"])
    group = cfg.get("group_jid")
    if not group or not group.endswith("@g.us"):
        log.error("group_jid invalido. A terminar.")
        return 1

    seen = load_seen()
    seen_set = set(seen)
    log.info("Servico iniciado. Grupo %s. Mensagens ja vistas: %d.", group, len(seen_set))

    while True:
        try:
            res = api(cfg, key, "POST", f"/chat/findMessages/{cfg['instance']}",
                      {"where": {"key": {"remoteJid": group}}, "limit": 50})
            records = res.get("messages", {}).get("records", []) if isinstance(res, dict) else []
            for m in sorted(records, key=lambda x: x.get("messageTimestamp", 0)):
                mid = str(m.get("key", {}).get("id", ""))
                if not mid or mid in seen_set:
                    continue
                seen_set.add(mid)
                seen.append(mid)
                if m.get("key", {}).get("fromMe"):
                    continue
                text = message_text(m)
                if not text:
                    continue
                who = m.get("pushName") or m.get("key", {}).get("participant") or "?"
                entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "id": mid, "from": who, "text": text}
                with open(INBOX_PATH, "a", encoding="utf-8") as f:
                    f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                log.info("Nova mensagem de %s", who)
                api(cfg, key, "POST", f"/message/sendText/{cfg['instance']}", {
                    "number": cfg["supervisor_phone"],
                    "text": f"[{cfg['project_name']}] Nova mensagem de {who}:\n{text}\n(a aguardar resposta do agente)",
                })
            save_seen(seen)
        except Exception as e:  # o servico nao pode morrer por um erro de rede
            log.error("Erro no ciclo: %s", e)
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    sys.exit(run())
