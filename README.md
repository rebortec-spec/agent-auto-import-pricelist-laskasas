# Agent auto-import pricelist Laskasas

Agente que valida a Tabela de Precos Laskasas (v15.2) e prepara a atribuicao automatica de precos no Floow, em conversa com a Ana via WhatsApp (Evolution API). Plano e regras: `docs/plano_atribuicao_precos.md`.

Funciona em Windows, Linux e macOS (Python 3.9+).

## Instalar numa maquina nova

```
git clone https://github.com/rebortec-spec/agent-auto-import-pricelist-laskasas.git
cd agent-auto-import-pricelist-laskasas
python scripts/setup.py
```

O `setup.py` instala as dependencias, **pede ao utilizador** a config local (grupo, supervisor, URL) e as chaves em falta, e guarda-as na maquina:

| Onde | Quando |
|---|---|
| Variavel de ambiente `EVOLUTION_APIKEY` | se existir, tem prioridade |
| Cofre do sistema (Credential Manager / Keychain / Secret Service) | via `keyring` |
| `~/.config/pricelist_laskasas/secrets.json` (modo 600) | servidores Linux sem cofre |

Nenhuma chave, contacto ou mensagem real vai para o git (ver `.gitignore`). `python scripts/setup.py --check` mostra o que falta. Se um script correr sem chave e houver terminal, pede-a na hora.

## Servicos

```
python scripts/laskasas_daemon.py     # le o grupo, regista em docs/inbox_laskasas.jsonl, avisa o supervisor
python scripts/laskasas_whatsapp.py status | read | send "texto" --confirm
```

Sempre ativo:
- **Linux**: unit systemd (`ExecStart=/usr/bin/python3 <repo>/scripts/laskasas_daemon.py`, `Restart=always`).
- **Windows**: Agendador de Tarefas, "Ao iniciar sessao", `pythonw.exe scripts\laskasas_daemon.py`, repetir/reiniciar em falha.

## Regras
- So fala com o grupo configurado; nunca com contactos individuais.
- Mensagens ao grupo so com `--confirm` depois de aprovadas pelo responsavel e espelhadas para ele.
- Nada e escrito no Floow sem aprovacao.
- O PDF da tabela (`Tabela_LASKASAS_V015.2.2026.pdf`, 80 MB) nao esta no git; pedir ao responsavel e colocar em `docs/`.
