"""
Daemon de validacao da correspondencia Tabela V015 <-> Floow.

- Le docs/inbox_laskasas.jsonl (escrito por scripts/laskasas_daemon.py).
- Procura respostas da Ana no formato "N a", "N b", "N nenhum" (N = numero do caso).
- Regista as escolhas em docs/validacao/match_v015_validado.csv.
- Responde no grupo com o que foi registado e o que falta.
- Quando todos os casos estiverem respondidos, envia mensagem final e termina.

Nunca escreve no Floow. Apenas atualiza o CSV local e envia mensagens ao grupo.
Requisitos: variavel de ambiente EVOLUTION_APIKEY.
Arranque: python -u scripts/validacao_daemon.py
"""
import csv
import json
import logging
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from secrets_store import get_secret  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "laskasas_whatsapp.json"
STATE_PATH = ROOT / "config" / "validacao_state.json"
INBOX_PATH = ROOT / "docs" / "inbox_laskasas.jsonl"
VAL_DIR = ROOT / "docs" / "validacao"
AMB_PATH = VAL_DIR / "ambiguos_restantes.csv"
MATCH_PATH = VAL_DIR / "match_v015_validado.csv"
BASES_PATH = VAL_DIR / "bases_nomes.json"
LOG_PATH = ROOT / "logs" / "validacao_daemon.log"
POLL_SECONDS = 120
ANA_NAME = "Ana Monteiro"
LETTERS = ["a", "b", "c", "d", "e"]

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
_handlers = [logging.FileHandler(LOG_PATH, encoding="utf-8")]
if sys.stdout is not None:  # sem consola (arranque oculto) sys.stdout e None
    _handlers.append(logging.StreamHandler(sys.stdout))
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", handlers=_handlers)
log = logging.getLogger("validacao")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def send_text(cfg, key, text):
    payload = json.dumps({"number": cfg["group_jid"], "text": text}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"{cfg['evolution_url']}/message/sendText/{cfg['instance']}",
        data=payload,
        method="POST",
        headers={"apikey": key, "Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_state():
    with open(STATE_PATH, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1)


def load_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def save_csv(path, rows):
    fields = list(rows[0].keys())
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, path)


def parse_answers(text):
    """Devolve lista de (numero, resposta). Aceita '16 a', '16 - b', '“16 B”', '5 nenhum'."""
    found = []
    for m in re.finditer(r"(?<!\d)(\d{1,2})\s*[-:)\.]?\s*(a|b|c|d|e|nenhum)\b(?!\s*(?:a|e)\s*\d)(?!\s*\d)", text, flags=re.IGNORECASE):
        found.append((int(m.group(1)), m.group(2).lower()))
    return found


def apply_answer(n, ans, amb, rows, byid):
    """Aplica uma resposta. Devolve (ok, descricao)."""
    if n < 1 or n > len(amb):
        return False, f"{n}: fora do intervalo 1-{len(amb)}"
    item = amb[n - 1]
    target = None
    for r in rows:
        if r["nome_v015"] == item["nome_v015"] and r["dims_v015"] == item["dims_v015"] and r["estado"] == "VARIOS":
            target = r
            break
    if target is None:
        return False, f"{n}: caso ja tratado ou nao encontrado"
    if ans == "nenhum":
        target["estado"] = "SEM_MATCH_VALIDADO"
        target["floow_ids"] = ""
        target["floow_nome"] = ""
        return True, f"{n} {item['nome_v015']} -> nenhum"
    ids = item["floow_ids"].split(";")
    idx = LETTERS.index(ans)
    if idx >= len(ids):
        return False, f"{n}: opcao '{ans}' nao existe"
    chosen = ids[idx]
    target["estado"] = "VALIDADO_ANA"
    target["floow_ids"] = chosen
    target["floow_nome"] = byid.get(chosen, "")
    return True, f"{n} {item['nome_v015']} -> {ans} = {target['floow_nome']}"


def main():
    cfg = load_config()
    key = get_secret(cfg["apikey_env"])

    amb = load_csv(AMB_PATH)
    with open(BASES_PATH, "r", encoding="utf-8-sig") as f:
        byid = {str(b["id"]): b["name"] for b in json.load(f)}
    state = load_state()
    log.info("Daemon de validacao iniciado. Casos: %d. Ja respondidos: %d.", len(amb), len(state["answered"]))

    while not state.get("done"):
        try:
            with open(INBOX_PATH, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            new_lines = lines[state["inbox_lines"]:]
            state["inbox_lines"] = len(lines)
            if new_lines:
                rows = load_csv(MATCH_PATH)
                changed = []
                for raw in new_lines:
                    try:
                        msg = json.loads(raw)
                    except ValueError:
                        continue
                    if msg.get("from") != ANA_NAME:
                        continue
                    for n, ans in parse_answers(msg.get("text", "")):
                        if n in state["answered"]:
                            continue
                        ok, desc = apply_answer(n, ans, amb, rows, byid)
                        if ok:
                            state["answered"].append(n)
                            changed.append(desc)
                            log.info("Registado: %s", desc)
                        else:
                            log.warning("Ignorado: %s | texto: %s", desc, msg.get("text", ""))
                if changed:
                    save_csv(MATCH_PATH, rows)
                    faltam = len(amb) - len(state["answered"])
                    if faltam == 0:
                        state["done"] = True
                        texto = ("[Pricelist Laskasas] Obrigado Ana, recebi todas as respostas (43 casos). "
                                 "Vou usar as escolhas para ligar os artigos.")
                    else:
                        texto = ("[Pricelist Laskasas] Registei " + str(len(changed)) +
                                 " resposta(s). Faltam " + str(faltam) + " caso(s).")
                    try:
                        send_text(cfg, key, texto)
                    except Exception as e:
                        log.error("Erro ao enviar confirmacao: %s", e)
            save_state(state)
        except Exception as e:  # o daemon nao pode morrer por um erro pontual
            log.error("Erro no ciclo: %s", e)
        time.sleep(POLL_SECONDS)

    log.info("Validacao concluida. Daemon a terminar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
