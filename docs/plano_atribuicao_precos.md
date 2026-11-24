# Plano: atribuição automática de preços (Laskasas) no Floow

Data: 2026-11-06. Estado: plano de trabalho. Nada foi escrito no Floow.

## 1. Objetivo

Quando o Floow gera um artigo (variante) a partir de um artigo base e de atributos, esse artigo deve sair **já com preço**, calculado a partir da tabela de preços (Tabela Online 2026, V015). Aplica-se só aos artigos que se vendem. Além disso, os artigos já gerados devem ser corrigidos.

Não é um cálculo de preço por metro. A tabela já traz o preço de cada artigo por combinação de acabamentos.

## 2. Como o Floow organiza os dados (verificado na documentação e na API)

| Conceito | Onde está | Notas |
|---|---|---|
| Artigo base (`base=1`) | `GET /api/v1/products/{id}` | Ex.: 63411 (Moozy), 76594 (Tapete LINES Laskasas), 95287 (Sofá TAÍS) |
| Variante (`base=0`) | `GET /api/v1/products/derived/{baseId}` | Tem `pv_1` próprio, `combined_attributes` (Marca, Familia, Tipo, Tecido, Pés, Acabamento, Medida...) |
| Preço de venda | `pv_1` (também `pv_2`, `pv_3`) | Escrevível por `PATCH /api/v1/products/{id}` (documentado) |
| Matriz de preços do base | `attribute_values.prices_combination` | Lista `{name, value}`. Ex.: "C1 - Ferro"=2634 |
| Geração de variantes | `POST /api/v1/skugenerator` (síncrono, até ~30) e `/queue` (assíncrono) | Aceita campo `price` (preço base customizado) na criação |
| Atributos | `GET /api/v1/mrp_attributes/{id}` | Tecido = id 11. Os valores não vêm nesse endpoint |

Notas verificadas:
- Base 63411 (Moozy): `pv_1` = 0. Preço só em `prices_combination`.
- Na amostra de 599 bases (60 páginas aleatórias): 472 são Laskasas, das quais 344 (73%) têm matriz. A maioria tem só 1 entrada.
- A amostra inclui artigos que não se vendem: "Memos", "Artigo reparação automóvel", "Esmalte...", "Catalisador 1370i", "Diluente Poliuretano". Têm matriz com 1 entrada. Por isso é preciso um filtro de "artigo que se vende".

## 3. Resultados da análise de preços (só leitura)

- **Tapetes LINES (base 76594):** `pv_1` de cada variante = valor da matriz para o acabamento e a medida (379, 519, 784, 1184, 664). Regra confirmada, sem tecido.
- **Almofadas LILLE (base 94496):** `pv_1` (52, 47, 76) não bate com a matriz (50, 72, 45, 67). Regra não explicada.
- **Sofá TAÍS (base 95287):** matriz C1–C4, TC × Ferro/Inox. Variantes de tecidos da categoria 1 têm preços diferentes conforme o tecido:
  - Ferro: Vienna Beige/Cream/Green = 2634; Vienna Anthracite/Deep Blue/Khaki = 2850.
  - Inox Polido = 2760; Inox Polido Copper Mate = 2411.
  - Conclusão: o preço depende do tecido e do metal, não só da categoria do tecido. Regra não explicada.

## 4. Dados de tecidos (equivalências)

- Fonte: circulares 74.1/2026 (Books), 89.5/2026 (Box) e 28/2026 (categorias). Lidas visualmente (PDF renderizado).
- Ficheiro: `scratchpad\equivalencias_laskasas.csv` (124 linhas: ref. fornecedor → ref. Laskasas → categoria).
- Categorias: 1, 2, 3, 4, 5, 6 e COURO (Saddle Terra/Black, preço por metro fixo, PVP 258,07 €).
- Circular 28/2026: Tipo 1 até 30 €, Tipo 2 31–60 €, Tipo 3 61–95 €, Tipo 4 96–140 €, Tipo 5 141–200 €, Tipo 6 201–260 € (preço/metro). Artigo com dois tecidos de categorias diferentes: prevalece a mais alta. Acima de 260 €: pedir preço ao Dto Orçamentação.
- Confirmado pela Ana: Tipo 1–6 = categorias C1–C6.
- Tecidos do Floow sem categoria na tabela: Vienna Light Grey, Moscow Orange, Tunis Ash.

## 5. Regras de preço conhecidas (Ana, 2026-11-05/06)

- Preço de estrutura de cama = linha C ou G da medida. Colchão e estrado vendidos à parte (não têm preço).
- Peça só com folha/lacado: preço pela categoria G.
- Peça com metal e madeira: G + FE (Ferro) ou IN (Inox).
- Peça com estofo: acrescenta a categoria C (tecido).
- Peça com metal, madeira e estofo: F + C + G.
- Rodapé de madeira em estofo: só C (G não entra).
- Lyssa: metal fixo no artigo, preço muda com G (confirmado 2026-11-06). Não há escolha FE/IN.
- Mármore M1/M2: a peça é a combinação G + FE/IN + M1/M2. A tabela já traz os preços combinados.

## 6. Lógica proposta (a validar)

**Passo A — Identificar artigos que se vendem.** Um base é "vendável" se:
1. Marca = Laskasas; e
2. Tipo = Produto Acabado; e
3. existe correspondência com um artigo da Tabela V015 (chave: nome normalizado + família).

Artigos sem correspondência ficam sem preço e vão para uma lista de exceções. **Pendente de confirmação pela Ana:** a Tabela V015 é a lista completa dos artigos que se vendem?

**Passo B — Ligar base ↔ tabela.** Guardar no artigo base o identificador do artigo na tabela (ex.: no campo `external_id` ou num atributo "Código Tabela"). A tabela V015 vira um JSON estruturado: artigo, família, matriz (acabamento × metal × medida) e preço.

**Passo C — Calcular o preço da variante.** Para cada variante gerada, ler `combined_attributes` e calcular a chave:
- Medida (tapetes, almofadas) → coluna da matriz pela medida.
- Acabamento G (folha/lacado) → linha G.
- Metal (Pés/Puxador) → Ferro / Inox.
- Tecido → categoria C1–C6 (tabela de equivalências).

O preço = `matriz[chave]`. Se a chave não existir, o artigo não recebe preço e entra na lista de exceções.

**Passo D — Atribuir na geração.** Na chamada ao skugenerator, enviar `price` calculado. Para artigos já gerados, `PATCH /api/v1/products/{id}` com `pv_1`.

**Passo E — Validar.** Relatório com: artigos vendáveis, com preço, sem preço, exceções (tecido sem categoria, combinação não encontrada), e diferenças face à matriz.

## 7. Bloqueios e perguntas

1. **Preço por tecido (sofá TAÍS, almofadas):** a regra não está explicada. Pergunta à Ana já enviada (porque Vienna Beige ≠ Vienna Anthracite no mesmo Ferro).
2. **Tecidos sem categoria:** Vienna Light Grey, Moscow Orange, Tunis Ash. Pergunta enviada.
3. **Artigos vendáveis:** confirmar se a V015 é a lista de vendáveis, e como distinguir na Floow os artigos que não se vendem (Tipo, Família, `publish_online`, ou outro campo). **A perguntar à Ana.**
4. **TC na matriz do TAÍS:** significado a confirmar.

## 8. Prompt para desenvolver a lógica dentro do Floow

> Objetivo: ao gerar variantes de artigos base Laskasas (`Marca = Laskasas`, `Tipo = Produto Acabado`), atribuir automaticamente o preço de venda (`pv_1`) a partir da Tabela de Preços Online 2026 (V015).
>
> Entradas:
> 1. `tabela_v015.json`: lista de artigos com nome, família, matriz de preços (acabamento G/C/M, metal FE/IN, medida) e preço. Fonte: `docs/tabela_v015_texto.txt` (estruturar à mão ou com script).
> 2. `equivalencias_tecidos.csv`: referência de fornecedor → referência Laskasas → categoria (C1–C6, COURO). Fonte: circulares 74.1/2026, 89.5/2026.
> 3. Regras: (ver secção 5 de `docs/plano_atribuicao_precos.md`).
>
> Tarefas:
> 1. Criar uma tabela de correspondência base ↔ artigo da V015 (chave: nome normalizado + família). Guardar o identificador no artigo base. Listar as bases sem correspondência.
> 2. Filtrar os artigos vendáveis: `Marca = Laskasas` e `Tipo = Produto Acabado` e com correspondência. Os restantes não recebem preço.
> 3. Ao gerar uma variante (skugenerator ou fila), ler `combined_attributes` e calcular a chave de preço: medida, acabamento G/C, metal (Ferro/Inox), categoria do tecido. Enviar o preço calculado no campo `price`.
> 4. Para as variantes já existentes, atualizar `pv_1` por `PATCH /api/v1/products/{id}`. Começar por um teste com 10 artigos (tapetes LINES e um sofá) antes de correr em massa.
> 5. Gerar relatório: vendáveis, com preço, sem preço, exceções (tecido sem categoria, chave não encontrada, diferença face à matriz).
>
> Restrições:
> - Não alterar `pv_1` de artigos fora do âmbito (Marca ≠ Laskasas ou não vendáveis).
> - Não escrever sem aprovação do responsável (Rui). Primeiro modo de simulação (dry-run) que mostra o preço que seria atribuído.
> - Tratar as exceções em lista, não com um preço por omissão.
>
> Resultado esperado: função de cálculo de preço reutilizável, relatório de simulação e lista de exceções.

## 9. Próximos passos

1. Confirmar com a Ana: a V015 é a lista de vendáveis? Como distinguir na Floow os artigos que não se vendem?
2. Estruturar a V015 em JSON (artigo, família, matriz).
3. Criar a tabela de correspondência base ↔ V015 (dry-run, sem escrita).
4. Testar a regra em tapetes (já confirmada) e depois em sofás, depois do preço por tecido ser esclarecido.
5. Só depois escrever no Floow, com aprovação.

## 10. Confirmações (2026-11-06, respondido pelo Rui em nome da Ana)
- 1. A "Tabela de preços Online 2026" (V015) é a lista completa dos artigos que se vendem. Confirmado.
- 2. Todos os artigos da tabela são vendáveis. Confirmado.
- Consequência: o Passo A simplifica-se. Vendável = existe na V015. Os artigos Laskasas da Floow que não estão na V015 não recebem preço (ex.: Memos, Esmalte, Diluente).

## 11. Correspondência V015 ↔ Floow (dry-run, 2026-11-06, sem escrita)
- Nomes não coincidem: Floow usa "Consola JILL 180X40X85" (tipo + modelo + medida); a V015 usa "JILL CONSOLA 180 REVESTIDA A M1 INTERIOR" (acabamento no nome). Chave usada: tipo + modelo + medida.
- V015 parseada: 861 blocos de artigo (47 sem nome legível). Floow: 3.304 bases únicas listadas (falta 1 página de 10).
- Resultado com chave tipo+modelo+medida: 108 únicos, 94 com vários candidatos, 389 sem correspondência, 223 sem chave. Ficheiro: scratchpad\match_v015_chave.csv.
- Próximo passo: rever os 94 ambíguos e os 389 sem correspondência (ajustar sinónimos de tipo, modelo e medida) antes de qualquer escrita.
- Variantes de acabamento da V015 (M1, M1 INTERIOR, M2, FE/IN) devem corresponder a atributos da base na Floow, não a bases separadas. A confirmar com dados.

## 12. Validação com a Ana (2026-11-06)
- Enviados ao grupo: ambiguos_validar.csv (94 linhas, VARIOS) e matching_validar.csv (861 linhas), com instruções. Ana deve indicar, para cada ambíguo, o id Floow correto ou 'nenhum'; para SEM_MATCH/SEM_CHAVE, o nome Floow se existir.
- Sem escrita no Floow até validação.

## 13. Atualização (2026-11-06 17:10–17:30)
- Ana: 'Porque tens várias medidas para a mesma peça'. A tabela indica as dimensões de cada bloco; usei-as na correspondência (modelo + tipo + medida, tolerância 3 cm, ordem das dimensões ignorada).
- Resultado: 233 únicos, 43 ambíguos (só casos onde a medida não chega, sobretudo floreiras), 305 sem correspondência, 280 sem chave. Ficheiro: scratchpad\match_v015_final.csv.
- Enviado à Ana o bloco 1 de 3 dos 43 ambíguos (letras a/b/c). Sem resposta até às 17:30.

## 14. Teste de preços V015 vs Floow (2026-11-07, só leitura)
- Parser V015 reforçado: 861 blocos, 2 sem nome. Preços exportados em `docs/validacao/v015_artigos.json`.
- Associação v2 (`docs/validacao/associacao_v2.csv`): 317 únicos, 43 únicos só pelo nome, 6+14 com vários candidatos, 324 sem correspondência, 112 sem chave. As 43 escolhas da Ana preservadas (17 validadas, 26 "nenhum").
- Comparação de preços em 334 artigos ligados:
  - 310 não têm matriz `prices_combination` na Floow. A tabela de preços ainda não está carregada no Floow para a maioria.
  - 24 têm matriz, mas as categorias não coincidem: a V015 usa C1–C6 (estofos) ou G1–G3 (madeira/lacado) conforme o artigo; na Floow aparecem como G1–G6 com outros valores. Ex.: Espelho IRIS V015 C1=1812 vs Floow G1=694.
  - Conclusão: não há ainda preço na Floow que se possa comparar. A escrita de preços é necessária, e a regra de categoria (G ou C) tem de ser por tipo de artigo.
- Pendente antes de escrever: regra de categoria por tipo de artigo (estofo, madeira, espelho, pouf) e preço por tecido (perguntas à Ana sem resposta).

- 2026-11-07 17:10: Ana: 'O sofá TAÍS não faz parte da tabela atual, qual versão estás a usar?'. Resposta enviada: Tabela Online 2026 (V015, Tabela_LASKASAS_V015.2026.pdf, última atualização 2026-04-16). Os preços do TAÍS vêm da Floow, não da tabela. Pedido de confirmação se há versão mais recente.

- 2026-11-07 17:32: Ana: 'Tabela certa é a 15.2' (eu uso V015.2026). 'Viena e Tunis C' (categoria a confirmar: número). Pedido enviado: PDF da 15.2 e número da categoria.

## 15. Tabela correta: 15.2 (2026-11-07)
- Ficheiro guardado: docs\Tabela_LASKASAS_V015.2.2026.pdf (enviado pela Ana, 17:43). Texto: docs\tabela_15_2_texto.txt.
- A V015 antiga tinha preços desatualizados (a 15.2 sobe cerca de 3 a 5% nas consolas). Preços reconstruídos a partir da 15.2: docs\validacao\tabela_15_2_artigos.json (865 blocos) e associacao_15_2.csv.
- TAÍS e Vienna/Tunis não estão na tabela de preços (são tecidos). A confirmar: categoria de Vienna e Tunis (Ana: 'Viena e Tunis C,' sem número).

- 2026-11-07 18:21: Ana: 'Ja te enviei a tabela na resposta acima' (15.2 guardada em docs). 'C 1' = Viena e Tunis sao C1. Registado em docs\validacao\equivalencias_tecidos_v2.csv. Falta: Moscow Orange.

## 16. Teste de precos com a Ana (2026-11-09)
- Acabamentos (pp. 245-246 da 15.2, lidas em imagem): G1 = BGM, BRM (branco mate), MM, PM, VPM; G2 = CF, CN, EUM, NM (Nogueira mate); G3 = BGB, BRB, MB, PB, VPB, EFP, NB (Nogueira brilho). Metais: INOX (polido, escovado...) e FERRO (pintado texturado preto/branco mate).
- Resultados: ISIS 240 detalhe metalico G2 FE 3045 / IN 3184 (falta metal); BONNIE Essential 160x200 G1 C1 2399 (sem prateleira; com prateleira 1583, a confirmar); ESTER 50 G2 PVP FE 2693; ESTORIL Viena C1 com ponteiras metalicas 448; KELLY 220 tampo ceramico G2 4990.

## 17. Teste 2 de precos com a Ana (2026-11-09)
- Resultados enviados: JEANE 220 tampo M1 G2 6334; ISIS 200 MFC Cleaf extensivel 1674; EOS 1 gaveta normal 1272; DESMOND 140 tampo ceramico G3 2200; ROD espelho ferro 786; EDDY pouf C2 756; AMOUR c/ ponteiras C3 (58) 627; LONDON 212 C2 2573; SELENE estofo C1: colchao 160 -> cama 192 = 1500, colchao 180 -> cama 202 = 1503 (aguarda confirmacao); GOLD media D50 G3 876; DESMOND aparador 206 laminado tampo ceramico 3021.
- Nota: ROD, AMOUR, EOS, ISIS MFC e DESMOND laminado sao precos fixos ou sem categoria (confirmados pela Ana).

## 18. Regras confirmadas pela Ana (2026-11-09 12:50)
1. Consola EOS normal: preço fixo, independente do acabamento. Sim.
2. Pouf EDDY em C2: só a categoria C, sem somar G. Sim.
3. Cadeira AMOUR com ponteiras metálicas em C3: o metal já vem incluído, sem escolha FE/IN. Sim.
4. Espelho ROD: G1 é o acabamento da moldura; em Inox o preço é 998 €, em Ferro 786 €. Sim.
5. Mesa JEANE tampo M1 G2: a linha G2 do tampo M1, sem somar outra categoria. Sim.
6. Floreira GOLD Ø50 G3: G3 é o acabamento da madeira. Sim.
7. Consola DESMOND 140 com tampo cerâmico G3: a versão cerâmica tem só a linha G3. Sim.
8. Mesa ISIS 200 MFC Cleaf extensível: preço fixo, sem G nem C. Sim.
Regras de testes 1 e 2: ver secções 16 e 17.

## 19. Teste 3 com acabamentos reais (2026-11-09 17:00)
- Respostas: Nogueira = Mate (G2); lacado branco = Mate (G1); travertino = M2; Nogueira efeito = laminado (fixo).
- Resultados: ITHACA c/ gaveta CF 1115; BAIONA 180 NB 2062; LADY 8 gav NM + Inox esc. dourado 2949; LADY cabeceira ceramico G1 Ferro 798; CHARLIE 2 lug C1 rodape inox 3190; FLETCHER gaveta peq NM + Xangai C1 1781; GOLD 120 M2 rodape madeira G2 2504; DILI tampo ceramico IN 1473; JAYNE c/ bracos C1 ferro 778; NERA laminado 175. Aguarda confirmacao da Ana.

## 20. Validacao de duvida: Espelho IRIS 120x6x200 (2026-11-09 17:06)
- Ana: 'sim, e sempre em tecido' (categoria C = tecido). 'E vendido a esse preco no C3' (o salto C2 897 -> C3 1718 e preco real, nao erro). 'Nao leva' metal.
- Regra: espelho IRIS = so tabela C do tecido, sem FE/IN.

## 21. Artigos Floow fora da tabela 15.2 (Ana, 2026-11-09 17:11)
- Almofada LILLE: NAO se vende. Sem preço.
- Tapete LINES: vende-se, mas e artigo de fornecedor, nao esta na tabela Laskasas. Sem preço pela tabela 15.2.
- Sofa TAIS: descontinuado. Sem preço.
- Regra: artigos Floow sem correspondência na tabela 15.2 nao recebem preço automático.

## 22. Permissão do Rui (2026-11-09)
- O Rui autorizou a responder a pedidos de preço de qualquer pessoa no grupo (não só da Ana). Responder apenas com preços da tabela 15.2 e regras confirmadas nas secções 16–19 e 20.

## 23. Auditoria da tabela 15.2 (2026-11-09)
- Parser v3 (docs\validacao\tabela_15_2_artigos_v3.json): uma variante por cabecalho CAT/PVP. 873 variantes. Verificacoes: ordem G/C ok; sem valores estranhos.
- Alertas (docs\validacao\qa_tabela_15_2.csv): 21 nome+medida repetidos (nomes herdados de blocos anteriores em sub-variantes, ex.: NELLY CADEIRAO 83x88x89, JAYNE 57x50x89), 2 sem nome, 1 FE>IN (KAIROS G2, Ana: esta de acordo).
- Ana validou: AMOUR 589 (sem ponteiras) e 627 (com ponteiras); NELLY CADEIRA 56x59x85 C3 719; SIMONE C3 794; AMBROSE C3 956; KAIROS OK. JAYNE banco de bar 51x51x105 C1: 978 Ferro / 1005 Inox, falta metal.
- Regra: nao responder a artigos com alerta (nome+medida repetidos) sem validacao.

## 24. Verificacao final da tabela 15.2 (2026-11-09 17:40)
- Ana: BANCO JAYNE 51x51x105 C1 -> "pode ser qualquer metal": Ferro 978 EUR ou Inox 1005 EUR, conforme o metal escolhido pelo cliente.
- Completude: 2889 linhas de preco no texto = 2889 linhas lidas pela v3 (2717 com categoria + 172 valores isolados). Nenhuma linha de preco em falta.
- Extras (nao sao preco do artigo): Sistema Elevatorio Manual 295 EUR/lugar; Sistema Elevatorio Automatico 425 EUR/lugar; Furacao extra 70 EUR/unidade. So indicar se o cliente pedir.
- Ordem de precos G e C: sem violacoes na v3.
- Alertas (21 nome+medida repetidos, 2 sem nome): NAO responder automaticamente. Ex.: NELLY CADEIRAO 83x88x89 e JAYNE 57x50x89 sao sub-variantes com nome herdado.
- Validados pela Ana: AMOUR 589 (sem ponteiras) e 627 (com ponteiras); NELLY CADEIRA 56x59x85 C3 719; SIMONE C3 794; AMBROSE C3 956; KAIROS G2 Ferro 2775 / Inox 2708 (conforme a tabela).
- Erro encontrado e corrigido: nome herdado em sub-variantes (parser v2). Substituido pelo v3 (uma variante por cabecalho CAT/PVP).

## 25. Correcao de nomes e medidas (2026-11-11)
- Ana: PETER 38x44x97 (nao 42x43x87); ITHACA cabeceira 60x45x48 (nao 60x40x35); PRESTIGE 120x25x6 (nao 150x40x150); banco sem nome 42x43x102 = ESTORIL (pags 76-77); 57x50x104 = AMBROSE (pag 78).
- Causa: parser rejeitava nomes com PONTEIRAS e EXCLUSIVO, herdando o nome do artigo anterior. Corrigido em tabela_15_2_artigos_v3.json. Alertas: 3 (LAGOS duplicado identico; KAIROS validado).
- Pendente: PETER metal; ITHACA (4 versoes); PRESTIGE acabamento.
