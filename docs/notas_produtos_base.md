# Notas: produtos base no Floow (Pricelist Laskasas)

Estado: recolha de informaÃ§Ã£o (sÃ³ leitura). Nenhuma alteraÃ§Ã£o feita no Floow.
Objetivo: definir como colocar os preÃ§os nos produtos base, para que o wizard de geraÃ§Ã£o de SKUs atribua o preÃ§o Ã s variantes.

## PrincÃ­pio de trabalho
- Trabalhamos com os **produtos base** (`base=1`), nÃ£o com as variantes (`base=0`).
- As variantes sÃ£o geradas pelo wizard/skugenerator a partir da base e dos atributos.

## ObservaÃ§Ãµes atÃ© agora (2026-11-04)

### Produto base de exemplo
- id 63411, "Aparador JUY MZ 240X52X85" (categoria 24, `base=1`, `product_type=finished_product`).
- `bom_approved: 0`, `usar_bom_por_atributo: false`.
- `pv_1`, `pv_2`, `pv_3`, `pmc`, `lcp`: 0 / null. **O preÃ§o nÃ£o estÃ¡ nestes campos.**

### Onde estÃ¡ o preÃ§o
- `attribute_values.prices_combination`: lista de pares `{name, value}`.
- Exemplo com 12 entradas: `G1..G4 - Ferro`, `G1..G4 - Inox`, `G1..G4 - Inox Pintado`.
- Ex.: `G1 - Ferro = 2526`, `G4 - Inox Pintado = 3980`.
- HipÃ³tese (a confirmar com a Ana): `G1..G4` = grupo de tecido/acabamento da tabela; `Ferro / Inox / Inox Pintado` = acabamento de metal.

### Atributos do base (`base_attributes`)
Cada base tem atributos com `id`, `name`, `position`, `is_predominant_color` e `values` (com `id`, `attribute_id`, `name`, `value` (cÃ³digo), `unique_reference`, `is_active`).
- Exemplo: Marca (Moozy, cÃ³digo ZY), Tipo (Produto Acabado, PA), FamÃ­lia (MobiliÃ¡rio, MO), Sub-FamÃ­lia (Aparador, AP), Acab (valores como Carvalho Natural Mate, Lacado Branco Mateâ€¦, `is_predominant_color: true`).

### Atributos MRP relevantes (`/api/v1/mrp_attributes`)
- Tecido (id 11), Acabamento Tecido, Orla MetÃ¡lica, Acabamento dos PÃ©s, Acabamento de Tampo, etc.
- Alguns atributos tÃªm `technical: 1` (ex.: Marca, Tipo, FamÃ­lia, Sub-FamÃ­lia, Tampo, Cantoâ€¦), outros `technical: 0`.
- `product_code_structure` define a codificaÃ§Ã£o do SKU (posiÃ§Ã£o, nÂº de caracteres, `formula`, `variation`).

### Endpoints a explorar (ainda nÃ£o testados)
- `GET /api/v1/products/{id}` â†’ detalhe e `attribute_values` (funciona).
- `GET /api/v1/listproducts?only_base=1` â†’ lista de bases (funciona; ~3.600 bases).
- `GET /api/v1/products/derived-paged/{baseId}` e `GET /api/v1/products/derived/{baseId}` â†’ variantes de uma base (a confirmar).
- `POST /api/v1/skugenerator/estimate`, `/queue`, `/progress` â†’ motor de geraÃ§Ã£o (a confirmar formato e se gera variantes com preÃ§o).
- `GET /api/v1/mrp_attributes_values?mrp_attribute_id=...` â†’ devolveu vazio atÃ© agora (formato de filtro a confirmar).
- `GET /api/v1/attribute_value_bom/product/{productId}` â†’ pode dar a ligaÃ§Ã£o atributoâ†’valor no base (a confirmar).

## Respostas da Ana Monteiro (2026-11-05)
- **G1â€“G4 nÃ£o sÃ£o grupos de tecido.** SÃ£o os grupos de acabamento das folhas de madeira e dos lacados.
- Esta resposta corrige a hipÃ³tese anterior. A matriz `prices_combination` Ã©, portanto, acabamento de folha/lacado Ã— acabamento de metal (Ferro, Inox, Inox Pintado), e nÃ£o tecido Ã— acabamento.
- Pendente: categorias de tecido (perguntado em 2026-11-05).

## DecisÃµes do Rui
- **O preÃ§o de venda vai no `pv_1`** do produto base (indicaÃ§Ã£o do Rui, 2026-11-05).
- Ponto a validar: `pv_1` Ã© um valor Ãºnico por base, mas a tabela tem uma matriz (grupo G Ã— acabamento de metal, atÃ© 12 preÃ§os por base). Com um Ãºnico `pv_1` por base, a matriz tem de ser resolvida de outra forma (ex.: um base por combinaÃ§Ã£o, ou o `prices_combination` continuar a ser a fonte e o `pv_1` ser sÃ³ o preÃ§o de referÃªncia). Confirmar antes de escrever no Floow.

## Perguntas em aberto
1. Como o wizard lÃª os preÃ§os: a partir de `prices_combination` do base, ou de outra estrutura?
2. Os nomes `G1..G4` e `Ferro/Inox/Inox Pintado` correspondem a que atributos do Floow? (ex.: Tecido / Acabamento Tecido / Orla MetÃ¡lica)
3. Como se escreve `prices_combination` (endpoint de update do produto base) e quem tem permissÃ£o?
4. As variantes existentes herdam o preÃ§o do base ou tÃªm de ser regeneradas?
5. Quantas bases (de ~3.600) tÃªm `prices_combination` preenchido?

## PrÃ³ximos passos (propostos)
1. Confirmar com a Ana a correspondÃªncia G1..G4 e acabamentos de metal (pergunta por WhatsApp, sem tabela ainda).
2. Ler (sÃ³ leitura) os endpoints de variantes e do skugenerator para perceber o fluxo do wizard.
3. Mapear o preÃ§o de um conjunto de bases num Excel de validaÃ§Ã£o (algumas centenas).
4. Validar com a Ana e sÃ³ depois propor a escrita no Floow, com aprovaÃ§Ã£o tua.

- Categorias de tecido: C1 a C6 (Ana Monteiro, 2026-11-05). Pedida lista de tecidos por categoria em Excel/PDF.

- Ana (2026-11-05): as categorias C estão associadas aos preços dos tecidos. Há muitas tabelas; vai enviar os tecidos mais usados (da box). Perguntado se um tecido pertence sempre à mesma categoria ou pode variar conforme o artigo.

- Ana (2026-11-05): cada tecido tem sempre a mesma categoria C, independentemente do artigo. Só muda de categoria se o preço do tecido subir.

- Ana (2026-11-05): confirmado que PVP FE = Ferro e PVP IN = Inox (resposta 'Sim').

- Ana (2026-11-05): os colchões (ex.: 'USO CAMA', com G1–G3) são só informação de medida da cama e são vendidos à parte. Não são artigos com preço. Quando a peça tem metal, aparece a combinação do acabamento G com Ferro (FE) ou Inox (IN). Regra proposta para confirmação: sem metal = só preço G; com metal = G + FE/IN.

- Ana (2026-11-05): 'Peças com metal e madeira: G e F(e)/I(n)'. 'Se tiver estofo também tens de considerar o acabamento C'. 'Peças só de folha e lacados: preço categoria os C?' (ambíguo, confirmação pedida: G ou C?).

## Regras de preço confirmadas pela Ana (2026-11-05)
- Só folha e lacado (sem metal e sem estofo): preço pela categoria **G** (confirmado: 'G').
- Com metal e madeira: **G + FE (Ferro) ou IN (Inox)**.
- Com estofo: acrescenta a categoria **C** (tecido).
- Com metal, madeira e estofo: **F + C + G** (F = Ferro/FE, I = Inox/IN).
- Colchões (ex.: 'USO CAMA'): só informação de medida, vendidos à parte. Não são artigos com preço.
- Existe também uma configuração com **mármores (M)** e **cerâmicas**: a confirmar (pergunta feita).
- Ana (2026-11-05): mármore e cerâmica são 'outro acabamento' (não metal). Confirmação pedida: peça com mármore/cerâmica = G + mármore (ou cerâmica) em vez de G + Ferro/Inox?
- Ana (2026-11-05): mármore/cerâmica 'é mais complexo'. Pode ser 'em metal e mármore'. Exemplo indicado: mesa consola lusa (não encontrado no texto extraído).
- Consolas JILL (PDF p.~10, linhas 228-263): 'JILL CONSOLA 180 REVESTIDA A M1' (ext. madeira, detalhe metálico, G1 2.384 FE / 2.737 IN) vs 'REVESTIDA A M1 INTERIOR' (ext. madeira, interior mármore, G1 1.327 FE / 1.606 IN). Versão com mármore interior aparece MAIS BARATA: anomalia a verificar.
- Pergunta feita: M1/M2 são tipos de mármore? 'INTERIOR' = só interior em mármore?
- Correção enviada à Ana: a 'mesa consola Lusa' não está no texto extraído do PDF V015 (pesquisa por 'lusa' sem resultados). Pedido o nome exato ou a página. A referência à consola JILL na mensagem anterior foi um engano.
- Ana (2026-11-05): 'A jil é outro tipo de exemplo' (JILL é outro exemplo, não o Lusa). 'Os M1 e M2 são as categorias do preço de mármore'. 'A versão interior é folha no exterior e mármore no interior'. 'Página 12' = consolas JILL 140 (M1, M1 INTERIOR, M2, M2 INTERIOR) e LYSSA CONSOLA 140 (só PVP).
- Dados: JILL 140 M1 (ext. folha+metal) G1 2.188 FE / 2.468 IN; M1 INTERIOR G1 1.309 FE / 1.586 IN; M2 INTERIOR G1 1.627 FE / 1.904 IN; M2 G1 2.949 FE / 3.141 IN.
- Pergunta feita: na versão INTERIOR, o FE/IN ainda se aplicam ou o preço é só G + categoria de mármore (M1/M2)?
- Mesa consola Lusa: ainda não encontrada (a página 12 não a tem).
- Ana (2026-11-05): FE/IN 'ainda se aplicam' na versão INTERIOR. 'O preço depende da conjugação dos 3 materiais' (G folha + FE/IN metal + M1/M2 mármore). 'Está dividido em M1 e M2'. 'Dentro do M1 ou do M2, os valores para G e FE/IN'.
- Conclusão: cada linha da tabela = combinação (G, FE/IN, M1/M2). A tabela já traz os preços combinados; não há fórmula a aplicar nesses casos.
- Pergunta feita: nas peças com estofo, a categoria C soma-se a G+FE/IN ou tem linha própria com a combinação completa?
- Ana (2026-11-05): 'Em estofo podemos ter peças só de estofo, Cat C'. 'Se tiver estofo e madeiras o valor será C com G'. Exemplo: cama Bonnie.
- PDF p.159-160: BONNIE CAMA COM ACABAMENTO G1/G2/G3 (linhas C1–C6 por medida 160x200 e 180x200). O G vem no nome do artigo. Pergunta feita: o C já inclui o G do nome?
- Nota: a linha 'Colchão' aparece como medida; confirmar se é preço da cama completa.
- Ana (2026-11-05): 'Se só tiver estofo e metal será C mais FE/IN, exemplo pouf Charlie'. Confirmado no PDF: CHARLIE SOFÁ (2 e 3 lugares, chaise) COM RODAPÉ METÁLICO = C1–C6 com FE/IN (p.93-94).
- CONTRADIÇÃO: CHARLIE SOFÁ COM RODAPÉ EM MADEIRA (p.93) = só C1–C6 (sem G). Regra dita pela Ana 'estofo e madeira = C com G' não se aplica aqui. Pergunta feita: estofo com madeira no rodapé não leva G?
- Ana respondeu 'Certo' à pergunta da Bonnie (G do nome incluído no C?). Ambíguo: confirmar.
- Nota: Ana escreveu 'pouf Charlie'; no catálogo são sofás CHARLIE.
- Ana (2026-11-05): 'No rodapé não se aplica' (G não entra no rodapé de madeira). Resolve a contradição do Charlie: rodapé em madeira = só C; rodapé metálico = C + FE/IN.
- Bonnie: pergunta de confirmação feita (o G1/G2/G3 do nome já está incluído no preço C, ou tem de ser somado?). A resposta 'Certo' anterior ficou por confirmar.
- Ana (2026-11-05 20:18): 'No preço C já tem incluso o valor que está na descriminação da cama'. Confirmado: na Bonnie, o G do nome (G1/G2/G3) já está incluído no preço C. Preço da cama = linha C1–C6 da medida.
- Pergunta feita: nas medidas 160x200 e 180x200 da Bonnie, o colchão está incluído no preço ou é vendido à parte? (a linha 'Colchão' é a medida).
- Ana (2026-11-05 20:24): 'Em todas as camas o colchão e estrado é vendido à parte'. Logo, preço da cama = só estrutura (linha C ou G da medida); linhas 'Colchão' são só medida.
- Pergunta feita: página da mesa consola Lusa (ainda não encontrada no texto extraído).
- Ana (2026-11-05 20:29): 'Lysaa página 12' = LYSSA CONSOLA 140 (PDF p.12). Só preço PVP por G1–G3, sem FE/IN. Descrição: 'Estrutura em Ferro Pintado' e 'Detalhe em Inox' (metal definido no artigo).
- Pergunta feita: nestas peças o metal já vem definido no artigo, sem escolha Ferro/Inox?
- Ana (2026-11-06 10:22): "Exato, a estrutura e sempre em ferro e o preco ja inclui o metal, o preco muda com o acabamento C..." (mensagem truncada na captura; confirmar o final). Confirma que a Lyssa tem metal fixo: nao ha escolha FE/IN, o preco e o da linha G e muda com o acabamento C.
- Regra de preco para pecas com metal fixo no artigo (Lyssa): preco = linha da medida/G, sem FE/IN. Pendente: confirmar o que significa "muda com o acabamento C" (C e o tecido/estofo?).
- Ana (2026-11-06 11:43): "Desculpa, queria dizer G". RESOLVIDO: na Lyssa (metal fixo) o preco muda com o acabamento G (nao C). Regra: preco = linha G da medida, sem FE/IN.
- Perguntas enviadas ao grupo 2026-11-06 (key 3EB0C3F5035DE6AF3CEFF0): (1) acabamento C da Lyssa -> respondida (G); (2) lista de tecidos C1-C6 -> pendente; (3) Inox Pintado e acabamento de metal a parte? -> pendente.
- Leitura via API (2026-11-06, so GET): amostra aleatoria de 400 bases (40 paginas, seed 42): 247 com prices_combination (~62%), 153 sem, 0 erros. Estimativa para as ~3.629 bases: ~2.250 com matriz (margem de erro da amostra a confirmar).
- pv_1 do base: 0 em 400 de 400 bases da amostra. O preco de venda NAO esta no pv_1 dos bases.
- Variantes (base=0): cada variante tem pv_1 proprio (ex.: 75086 = 3191; 39 variantes do 63411, varios valores). O pv_1 varia com o metal dos pes/puxador (Ferro Texturado, Inox Polido, Inox Escovado...). Nao e herdado do base nem calculado a partir da matriz G x metal. Origem por confirmar.
- ERRO CORRIGIDO (2026-11-06): o produto 63411 "Aparador JUY MZ" e da marca MOOZY (Marca=Moozy), nao Laskasas. A amostra de 400 bases misturava marcas: refazer so com Marca=Laskasas.
- PDFs recebidos da Ana (2026-11-06 11:47), guardados em scratchpad\anexos_ana: (a) Circular 28/2026 MARCACAO DAS CATEGORIAS DE TECIDOS: TIPO 1 ate 30 EUR; TIPO 2 31-60; TIPO 3 61-95; TIPO 4 96-140; TIPO 5 141-200; TIPO 6 201-260 (por metro, PVP). Artigo com 2 tecidos de categorias diferentes: prevalece a mais alta. Acima de 260: pedir preco ao Dto Orcamentacao. (b) Circular 74.1 Equivalencias Books Laskasas. (c) Circular 89.5 Equivalencias Tecidos Box Laskasas (V5).
- Pergunta enviada 2026-11-06 (key 3EB0F68447B7C196E37E21): Tipo 1-6 = categorias C1-C6? e Inox Pintado = acabamento de metal a parte? (pendentes).
- Amostra CORRIGIDA (so Laskasas, 599 bases de 60 paginas aleatorias): 472 Laskasas; 344 (73%) com prices_combination; 128 sem. Distribuicao: 272 com 1 entrada, 16 com 2, 13 com 3, outras com 4-140 entradas. Estimativa: ~2.900 bases Laskasas no total, ~2.100 com matriz (a confirmar com contagem completa).
- Amostra antiga (400 bases, todas as marcas) fica invalidada para conclusoes sobre a Laskasas.
- Ana (2026-11-06 12:07): "1- sao". CONFIRMADO: Tipo 1-6 da circular 28/2026 = categorias C1-C6.
- Pergunta sobre Inox Pintado: DESCARTADA (vinha do Aparador JUY, que e Moozy). Ana: "Nao percebo a pergunta 2".
- Resposta enviada a Ana (2026-11-06): pergunta 2 cancelada; pedido de tabela de equivalencias em Excel (fornecedor, ref fornecedor, ref Laskasas, categoria C1-C6).
- ORIGEM DO pv_1 DAS VARIANTES (leitura 2026-11-06):
  * Tapete LINES (base 76594): matriz Slim 140x200=379, 160x240=519, 200x290=784, 250x350=1184, D250=664. As variantes tem pv_1 IGUAL ao valor da matriz pela medida (379, 519, 784, 1184, 664). Confirmado: pv_1 = valor da matriz (acabamento x medida).
  * Almofada LILLE (base 94496): matriz 50x50 s/Vivo=50, c/Vivo=72, 50x30 s/Vivo=45, c/Vivo=67. Variantes com pv_1 52 e 47 e 76: NAO batem certo com a matriz. Ainda por explicar.
  * Sofa TAIS (base 95287): matriz C1-C4 + TC por ferro/inox. Variantes pv_1 = 2850 (Ferro, Vienna Deep Blue/Khaki/Anthracite) e 2986 (Inox Polido, Vienna). Nenhum valor e igual a matriz (2634, 2809, 4074, 5544, 2441). Provavelmente matriz + categoria do tecido (Vienna = categoria a confirmar com a tabela de equivalencias). Ainda por explicar.
  * Conclusao parcial: para artigos SEM tecido, pv_1 da variante = matriz (acabamento x medida). Para artigos COM tecido, o pv_1 depende tambem da categoria do tecido (C1-C6). Falta a tabela de equivalencias (pedida a Ana em Excel).
- Ana (2026-11-06 12:45): "Nao tenho essa tabela em Excel, somente em pdf". Equivalencias lidas visualmente dos PDFs (renderizados): 124 referencias Laskasas -> categoria (C1-C6, Couro). Ficheiro: scratchpad\equivalencias_laskasas.csv.
- Teste sofa TAIS (base 95287), variantes com tecido de categoria 1: pv_1 depende do METAL e tambem do TECIDO dentro da mesma categoria (ex.: Ferro: Vienna Beige/Cream/Green = 2634; Vienna Anthracite/Deep Blue/Khaki = 2850). Inox Polido = 2760; Inox Polido Copper Mate = 2411. Categoria do tecido nao explica o preco sozinha.
- Tecidos sem categoria na tabela: Vienna Light Grey, Moscow Orange, Tunis Ash (verificar).
- CONCLUSAO PARCIAL: pv_1 da variante = f(metal, tecido), nao so f(categoria). Para os tapetes (sem tecido) pv_1 = matriz. Falta descobrir a tabela de preco por tecido (PVP do tecido, ver circular 28/2026 e tabela_v015).
- Pedido enviado a Ana (2026-11-06): (1) tabela PVP por tecido; (2) porque Vienna Beige/Cream/Green (2634) difere de Vienna Anthracite/Deep Blue/Khaki (2850) no sofa TAIS Ferro; (3) categoria de Vienna Light Grey, Moscow Orange, Tunis Ash; (4) significado de TC na matriz TAIS. Key 3EB0
- CONFIRMADO (2026-11-06, pelo Rui em nome da Ana): V015 (Tabela Online 2026) = lista completa dos artigos que se vendem; todos os artigos da tabela sao vendaveis.
