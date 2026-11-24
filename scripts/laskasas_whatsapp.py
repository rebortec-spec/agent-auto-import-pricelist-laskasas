"""
WhatsApp do projeto Pricelist Laskasas (Evolution API).

Regras do projeto:
- So fala com o grupo definido em config/laskasas_whatsapp.json (group_jid, sufixo @g.us).
- Nunca envia para contactos individuais (o Bruno nao pertence a este projeto).
- Envio so com --confirm, depois de o Rui aprovar o texto.
- Toda a mensagem enviada ao grupo e espelhada para o Rui.
- A chave da API vem do cofre da maquina (ver secrets_store.py / setup.py); nunca fica no repositorio.

Uso:
  python scripts/laskasas_whatsapp.py status
  python scripts/laskasas_whatsapp.py read [--limit 20]
  python scripts/laskasas_whatsapp.py send "texto" --confirm
"""
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from secrets_store import get_secret  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "laskasas_whatsapp.json"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def api(cfg, method, path, payload=None):
    key = get_secret(cfg["apikey_env"])
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{cfg['evolution_url']}{path}",
        data=data,
        method=method,
        headers={"apikey": key, "Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def require_group(cfg):
    jid = cfg.get("group_jid")
    if not jid or not jid.endswith("@g.us"):
        sys.exit("group_jid nao esta definido (tem de terminar em @g.us). Confirmar o grupo antes de continuar.")
    return jid


def fetch_group_messages(cfg, limit):
    jid = require_group(cfg)
    res = api(cfg, "POST", f"/chat/findMessages/{cfg['instance']}",
              {"where": {"key": {"remoteJid": jid}}, "limit": limit})
    records = res.get("messages", {}).get("records", []) if isinstance(res, dict) else []
    return sorted(records, key=lambda m: m.get("messageTimestamp", 0))


def message_text(m):
    msg = m.get("message") or {}
    ext = msg.get("extendedTextMessage") or {}
    return msg.get("conversation") or ext.get("text") or ""


def cmd_read(cfg, limit):
    for m in fetch_group_messages(cfg, limit):
        k = m.get("key", {})
        who = "EU" if k.get("fromMe") else (m.get("pushName") or k.get("participant") or "?")
        print(f"[{who}] {message_text(m)}")


def cmd_send(cfg, text, confirm):
    require_group(cfg)
    if not confirm:
        sys.exit("Envio bloqueado: falta --confirm (o Rui tem de aprovar o texto).")
    if not text.strip():
        sys.exit("Texto vazio.")
    api(cfg, "POST", f"/message/sendText/{cfg['instance']}", {"number": cfg["group_jid"], "text": text})
    api(cfg, "POST", f"/message/sendText/{cfg['instance']}",
        {"number": cfg["supervisor_phone"], "text": f"[ESPELHO - {cfg['project_name']}]\n{text}"})
    print("Enviado ao grupo e espelhado para o Rui.")


def main():
    p = argparse.ArgumentParser(description="WhatsApp do projeto Pricelist Laskasas")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    r = sub.add_parser("read")
    r.add_argument("--limit", type=int, default=20)
    s = sub.add_parser("send")
    s.add_argument("text")
    s.add_argument("--confirm", action="store_true")
    a = p.parse_args()

    cfg = load_config()
    if a.cmd == "status":
        print(json.dumps(api(cfg, "GET", f"/instance/connectionState/{cfg['instance']}"), ensure_ascii=False, indent=2))
    elif a.cmd == "read":
        cmd_read(cfg, a.limit)
    elif a.cmd == "send":
        cmd_send(cfg, a.text, a.confirm)


if __name__ == "__main__":
    main()
