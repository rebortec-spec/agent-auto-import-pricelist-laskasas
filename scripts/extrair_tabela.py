"""
Extrai a tabela de preços (PDF Tabela_LASKASAS_V015.2026) para um Excel de validação.

Estrutura reconhecida no PDF:
- Cada artigo: nome em maiúsculas antes de "Dimensões:", dimensões, colecção e cabeçalho "CAT ...".
- Família G (acabamentos de folha/lacado): "CAT PVP FE PVP IN" -> linhas "G1 <FE> <IN>".
- Família C (categorias de tecido/pele): "CAT PVP" -> linhas "C1 <PVP>".
- Algumas linhas G têm só um preço (cabeçalho "CAT PVP").

Saída: docs/validacao_precos_v015.xlsx (folha "Validacao") e docs/validacao_precos_v015.csv.
Uso: python scripts/extrair_tabela.py
"""
import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "Tabela_LASKASAS_V015.2026.pdf"
TXT = ROOT / "docs" / "tabela_v015_texto.txt"
OUT_XLSX = ROOT / "docs" / "validacao_precos_v015.xlsx"
OUT_CSV = ROOT / "docs" / "validacao_precos_v015.csv"

PRICE_RE = re.compile(r"(\d{1,3}(?:[  ]\d{3})*|\d+)\s*€")
CODE_RE = re.compile(r"^(G\d+|C\d+)\s+(.*)$")
SKIP_NAME = ("ÚLTIMA", "PVP", "CAT ", "COLECÇÃO", "=====")


def to_int(s):
    return int(re.sub(r"[  ]", "", s))


def ensure_text():
    if not TXT.exists():
        sys.exit(f"Ficheiro de texto em falta: {TXT}. Extrair o PDF primeiro.")


def parse():
    lines = [l.strip() for l in TXT.read_text(encoding="utf-8").splitlines()]
    rows = []
    page = 0
    nome = dims = colecao = variante = None
    header = None  # "FE_IN" ou "PVP"
    for i, line in enumerate(lines):
        m = re.match(r"===== PAGINA (\d+) =====", line)
        if m:
            page = int(m.group(1))
            continue
        if line.startswith("Dimensões:"):
            # Artigo = linha em maiúsculas mais próxima acima, ignorando linhas de preço e cabeçalhos.
            # Variante = linha imediatamente acima das dimensões, se não for o próprio nome (ex.: "150x200 cm Colchão").
            nome = None
            variante = ""
            for back in range(i - 1, max(i - 15, 0), -1):
                cand = lines[back]
                if not cand or any(s in cand for s in SKIP_NAME) or CODE_RE.match(cand):
                    continue
                if cand.startswith(("Dimensões", "COLECÇÃO", "Altura", "Furação")):
                    continue
                if cand.isupper():
                    nome = cand
                    break
                if not variante:
                    variante = cand
            if nome is None:
                nome = variante
                variante = ""
            dims = lines[i + 1] if i + 1 < len(lines) else ""
            colecao = ""
            header = None
            continue
        if line.startswith("COLECÇÃO"):
            colecao = line
            continue
        if line.startswith("CAT PVP FE PVP IN"):
            header = "FE_IN"
            continue
        if line == "CAT PVP":
            header = "PVP"
            continue
        cm = CODE_RE.match(line)
        if cm and header and nome:
            code, rest = cm.group(1), cm.group(2)
            prices = [to_int(p) for p in PRICE_RE.findall(rest)]
            if not prices:
                continue
            fam = "G" if code.startswith("G") else "C"
            fe = in_ = pvp = None
            if header == "FE_IN" and len(prices) >= 2:
                fe, in_ = prices[0], prices[1]
            elif header == "FE_IN" and len(prices) == 1:
                fe = prices[0]
            else:
                pvp = prices[0]
            rows.append({
                "Pagina": page,
                "Artigo": nome,
                "Variante": variante or "",
                "Dimensoes": dims,
                "Colecao": colecao,
                "Familia": fam,
                "Categoria": code,
                "PVP_FE": fe,
                "PVP_IN": in_,
                "PVP": pvp,
            })
    return rows


def write_csv(rows):
    with open(OUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(rows)


def write_xlsx(rows):
    try:
        from openpyxl import Workbook
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "openpyxl"])
        from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Validacao"
    headers = list(rows[0].keys())
    ws.append(headers)
    for r in rows:
        ws.append([r[h] for h in headers])
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    for col in ws.columns:
        width = max(len(str(c.value)) if c.value is not None else 0 for c in col)
        ws.column_dimensions[col[0].column_letter].width = min(max(width + 2, 10), 60)
    wb.save(OUT_XLSX)


def main():
    ensure_text()
    rows = parse()
    if not rows:
        sys.exit("Nenhuma linha de preço reconhecida. Rever a estrutura do texto.")
    write_csv(rows)
    write_xlsx(rows)
    artigos = len({(r["Artigo"], r["Pagina"]) for r in rows})
    print(f"Linhas de preço: {len(rows)} | artigos distintos: {artigos}")
    print(f"G: {sum(1 for r in rows if r['Familia'] == 'G')} | C: {sum(1 for r in rows if r['Familia'] == 'C')}")
    print(f"XLSX: {OUT_XLSX}")


if __name__ == "__main__":
    main()
