# Manual do Utilizador — Rebortec Floow (Edição Completa para NotebookLM)

Documento oficial e exaustivo de utilização do **Rebortec Floow** (ou simplesmente **Floow**). Este manual foi desenhado especificamente para utilizadores operacionais e como fonte única de verdade para indexação e consulta no **NotebookLM**.

> **Identidade do Produto:** O software chama-se **Rebortec Floow**. Não lhe chame "BPM" (a pasta interna e o menu histórico "Eventos" são apenas resquícios de nomenclatura de código).  
> **Suporte Técnico:** Envie email para `suporte@rebortec.com` ou clique no ícone de ponto de interrogação (**?**) no canto superior direito do cabeçalho.  
> **Manuais Integrados na Aplicação:**
> - Projetos de Decoração: **Projetos → Manual** (`/decoration-projects/manual`)
> - Pedidos de Cotação (CDP): **Pedidos de cotação → Manual** (`/cdp/ajuda`)
> - Aprovisionamento (Procurement): **Aprovisionamento → Manual** (`/procurement/ajuda`)

---

## Índice Geral

1. [Visão Geral, Arquitetura e Relação com o Artsoft ERP](#1-visão-geral-arquitetura-e-relação-com-o-artsoft-erp)
2. [Autenticação, Sessão e Acessos](#2-autenticação-sessão-e-acessos)
3. [Interface Principal e Navegação](#3-interface-principal-e-navegação)
4. [Gestão de Terceiros (Clientes e Fornecedores)](#4-gestão-de-terceiros-clientes-e-fornecedores)
5. [Catálogo de Artigos e Engenharia de Produto](#5-catálogo-de-artigos-e-engenharia-de-produto)
   - 5.1 Conceito de Artigo Base, Atributos e Artigos Filhos
   - 5.2 Catálogo de Atributos e Valores (MRP)
   - 5.3 Configuração de Atributos na Ficha Base
   - 5.4 Mini-BOMs por Valor de Atributo
   - 5.5 Grupos de Combinação de Mini-BOM
   - 5.6 Lista de Materiais Principal (BOM)
   - 5.7 Gestão de Filhos e Regeneração de BOM
   - 5.8 Assistente de Criação de Variantes (Wizard)
   - 5.9 Gestão de Mídia, Desenhos Técnicos e Replicação
   - 5.10 Fichas Técnicas, Folhas de Cálculo e Histórico de Atividade
6. [BOM Paramétrica (fx Paramétrica)](#6-bom-paramétrica-fx-paramétrica)
   - 6.1 Conceito e Filosofia de Não-Rutura (Opt-In)
   - 6.2 Estrutura do Modelo: Parâmetros e Nós
   - 6.3 Tipos de Origem de Dados (Fixed, Variable, Formula, Inherited)
   - 6.4 Expressões Matemáticas, Condições e Repetições
   - 6.5 Sintaxe de Referências Relativas e Absolutas
   - 6.6 Motor Processual Avançado (`engine: "process"`)
   - 6.7 Validação de Ciclos, Dependências e Simulação em Tempo Real
   - 6.8 Geração de Snapshot Imutável para Fabrico
7. [Gestão e Planeamento da Produção](#7-gestão-e-planeamento-da-produção)
   - 7.1 Ordens de Produção e Acompanhamento Operacional
   - 7.2 Análise de Stock para Produção
   - 7.3 Gestão de Subcontratados
   - 7.4 Planeamento Visual (Calendário Gantt) e Gestão de Carga
   - 7.5 Análise de Planeado vs Real e Rentabilidade de Fabrico
   - 7.6 Visualização de Chão de Fábrica e Fábrica 3D
   - 7.7 Ecrãs de TV e Capacidade dos Postos (KPIs Minutos/Dia)
   - 7.8 Gestão de MES no Escritório
   - 7.9 Regras de Tempos de Espera (Lag Time) entre Operações
   - 7.10 Impacto das Picagens no Stock do ERP Artsoft
8. [Terminal Móvel de Chão de Fábrica (MES)](#8-terminal-móvel-de-chão-de-fábrica-mes)
   - 8.1 Ativação e Registo do Dispositivo Tablet
   - 8.2 Autenticação por PIN ou QR Code e Escolha de Contexto
   - 8.3 Modo de Ordem de Fabrico Libertada vs Picagem Ad-Hoc
   - 8.4 Ciclo de Trabalho: Iniciar, Suspender, Retomar e Terminar
   - 8.5 Trabalho em Grupo e Conclusão Coletiva
   - 8.6 Suspensão Automática de Turnos e Segurança de Ecrã
   - 8.7 Interrupções por Lag Time e Desbloqueio por Supervisor
   - 8.8 Perguntas de Embalamento (Volumes, Medidas e Peso) antes da Entrada de Stock
   - 8.9 Reabertura de Tarefas Concluídas
9. [Gestão de Assiduidade e Controlo de Ponto](#9-gestão-de-assiduidade-e-controlo-de-ponto)
10. [CRM — Gestão de Relacionamento Comercial](#10-crm--gestão-de-relacionamento-comercial)
11. [CRM Laskasas — Ferramentas Comerciais Avançadas](#11-crm-laskasas--ferramentas-comerciais-avançadas)
    - 11.1 Folha de Acompanhamento Comercial (Grelha Excel)
    - 11.2 Dashboard de Performance por Loja (PV 26)
    - 11.3 Análise Global de Vendas e Previsões (Forecast)
12. [Pedidos de Cotação de Peças Especiais (CDP)](#12-pedidos-de-cotação-de-peças-especiais-cdp)
    - 12.1 Criação do Pedido Comercial
    - 12.2 Ciclo de Viabilidade Técnica e Devolução para Correção (R1, R2...)
    - 12.3 Atribuição de Preço (Preço A, B e C)
    - 12.4 Decisão Comercial: Adjudicação ou Perda
    - 12.5 Gestão Documental e Desenhos Assinados
    - 12.6 Retificação de Medidas no Cliente e Criação do C971 no Artsoft
    - 12.7 Aplicação Móvel de Retificações no Terreno (`/cdp/app`)
    - 12.8 Relatórios e Análises Estatísticas do CDP
13. [Aprovisionamento (Procurement / RFQ a Fornecedores)](#13-aprovisionamento-procurement--rfq-a-fornecedores)
    - 13.1 Criação e Estruturação do Pedido de Cotação
    - 13.2 Seleção de Fornecedores e Envio de Convites
    - 13.3 Portal Externo do Fornecedor (`/fornecedor`)
    - 13.4 Mensagens Bidirecionais e Esclarecimento de Dúvidas
    - 13.5 Comparação de Propostas e Adjudicação Interna Sigilosa
    - 13.6 Interligação entre CDP e Aprovisionamento
14. [Projetos de Decoração](#14-projetos-de-decoração)
    - 14.1 Tipologias de Projeto
    - 14.2 Criação e Configuração da Equipa de Design
    - 14.3 Ferramenta de Desenho de Planta 2D (Wall Builder)
    - 14.4 Organização por Ambientes e Importação de Orçamentos Artsoft
    - 14.5 Regras de Anexos, Apresentação e Partilha Pública com Cliente
    - 14.6 Fecho Financeiro do Projeto
15. [Gestão de Pós-Venda](#15-gestão-de-pós-venda)
16. [Circulares Internas e Comunicados](#16-circulares-internas-e-comunicados)
17. [Logística no Escritório (Consulta e Gestão de Stock)](#17-logística-no-escritório-consulta-e-gestão-de-stock)
    - 17.1 Consulta de Posições, Destinos e Histórico de Movimentos
    - 17.2 Alocação e Desalocação de Stock Livre
    - 17.3 Mapa Visual Tridimensional do Armazém
18. [Terminal Móvel de Logística (PWA de Armazém)](#18-terminal-móvel-de-logística-pwa-de-armazém)
    - 18.1 Acesso por PIN e Seleção do Armazém de Trabalho
    - 18.2 Leitura e Descodificação de Etiquetas com Volumes
    - 18.3 Inventário Físico e Acertos de Stock
    - 18.4 Receção de Mercadoria de Fornecedores
    - 18.5 Movimentação e Deslocalização com Carrinho de Transporte
    - 18.6 Consumos Internos com Saída de Stock
    - 18.7 Consulta e Edição de Dados Logísticos do Artigo
    - 18.8 Expedição e Gestão do Mapa de Cargas
19. [Estrutura de Armazéns e Localizações](#19-estrutura-de-armazéns-e-localizações)
20. [Faturas OCR de Fornecedores](#20-faturas-ocr-de-fornecedores)
    - 20.1 Pipeline de Processamento Inteligente em 4 Fases
    - 20.2 Quarentena Inteligente e Cockpit de Reconciliação
    - 20.3 Associação de Linhas e Aprendizagem de Layout por NIF
    - 20.4 Integração e Envio Final para o Artsoft
21. [Indicadores e Inteligência de Negócio (BI)](#21-indicadores-e-inteligência-de-negócio-bi)
22. [Consultas Dinâmicas de Dados](#22-consultas-dinâmicas-de-dados)
23. [Módulos Complementares e Setoriais](#23-módulos-complementares-e-setoriais)
    - 23.1 AutoLog — Gestão de Frotas e Oficina
    - 23.2 FSPS e Logística Praddy
    - 23.3 Assistentes de Inteligência Artificial e Conectores MCP
24. [Administração do Sistema, Permissões e Sincronização](#24-administração-do-sistema-permissões-e-sincronização)
    - 24.1 Matriz de Grupos e Permissões
    - 24.2 Sincronização Periódica com o Artsoft ERP
    - 24.3 Gestão de Limites de Compras
25. [O que o Floow NÃO Faz Sozinho (Regras Críticas e Limitações)](#25-o-que-o-floow-não-faz-sozinho-regras-críticas-e-limitações)
26. [Guia de Resolução de Problemas (Troubleshooting)](#26-guia-de-resolução-de-problemas-troubleshooting)
27. [Glossário Geral de Conceitos](#27-glossário-geral-de-conceitos)
28. [Percursos Rápidos Operacionais ("Como Faço Para...")](#28-percursos-rápidos-operacionais-como-faço-para)

---

## 1. Visão Geral, Arquitetura e Relação com o Artsoft ERP

O **Rebortec Floow** é o sistema central de gestão operacional e controlo de fluxo de trabalho da Rebortec. A sua missão é coordenar todas as etapas da cadeia de valor da empresa:
- Engenharia e parametrização técnica de artigos e listas de materiais (BOM);
- Planeamento, sequenciamento e picagem em chão de fábrica (MES);
- Gestão de armazéns, receção, transferências internas e inventários (Logística);
- Circuito comercial de orçamentação e pedidos especiais à medida (CDP);
- Consultas ao mercado e RFQ de matérias-primas a fornecedores (Procurement);
- Elaboração e acompanhamento de projetos de decoração de interiores;
- Leitura automatizada e conferência de faturas de compras com inteligência artificial (OCR);
- Controlo de assiduidade de colaboradores e comunicação interna corporativa.

### Três Tipos de Interação com os Dados
1. **Leitura e Consulta do ERP Artsoft:** O Floow pesquisa saldos de stock oficiais, fichas de clientes/fornecedores e documentos existentes no Artsoft para garantir integridade.
2. **Escrita Bidirecional (Floow → Artsoft):** Operações executadas no Floow que criam documentos oficiais no ERP. Exemplos:
   - Entrada de produto acabado e baixa de consumo ao concluir operações no terminal MES;
   - Acertos de inventário registados no terminal móvel de logística;
   - Documentos de deslocalização e transferências entre armazéns;
   - Receção de mercadorias de fornecedor e baixas de consumos gerais;
   - Criação automática do documento de retificação de medidas **C971** ao adjudicar um pedido CDP;
   - Integração da fatura de fornecedor no Artsoft após validação no módulo OCR.
3. **Dados Exclusivos do Floow:** Fluxos operacionais internos que não afetam o ERP comercial até ao fecho. Exemplos:
   - Definições de BOM paramétrica, regras de cálculo e simulações;
   - Pedidos de cotação internos (CDP) e histórico de versões e revisões de desenho;
   - Projetos de decoração e ficheiros desenhados no Wall Builder 2D;
   - Negociações, mensagens e cotações no portal de fornecedores do Procurement;
   - Alocações e reservas de stock livre a encomendas de clientes;
   - Circulares informativas, registos de ponto e tarefas pessoais.

> [!IMPORTANT]
> **O Floow não substitui o Artsoft.** O Artsoft permanece como o ERP financeiro, fiscal e repositório oficial de stock. Se o Artsoft rejeitar uma transação (por exemplo, por falta de saldo no armazém de consumo), a operação no Floow pode registar o histórico interno, mas sinaliza a falha de sincronização para posterior tratamento.

---

## 2. Autenticação, Sessão e Acessos

### 2.1 Acesso ao Portal Web (Secretária)
1. Aceda ao URL oficial do Floow atribuído à sua organização.
2. Introduza o seu **email profissional** e **palavra-passe**.
3. **Autenticação em Duas Etapas (2FA):** Em ambiente de produção, o sistema envia de imediato um código de segurança numérico de uso único para o seu email. Introduza o código no ecrã de validação.
   - *Nota:* Se não receber o código, confirme a pasta de Spam ou Lixo Eletrónico. Em servidores de teste locais, o código pode ser exibido diretamente ou simulado no painel de notificações.
4. Para terminar a sessão com segurança: clique no seu nome no canto superior direito e selecione **Logout**.

### 2.2 Acessos Especiais Independentes (Sem Login Web)
Alguns terminais utilizam credenciais e interfaces específicas:
- **Terminal de Chão de Fábrica (MES):** Funciona em tablets dedicados na fábrica. A autenticação faz-se exclusivamente por **PIN de operador** ou leitura de **QR Code pessoal**.
- **Terminal Móvel de Logística (PWA):** Aplicação de telemóvel/tablet para armazém. O login faz-se por **PIN de operador** associado a permissões de logística.
- **Aplicação de Retificações no Terreno (`/cdp/app`):** Desenvolvida para técnicos com tablets móveis. Requer as credenciais normais do Floow, mas possui uma interface otimizada para toque, com suporte para fotos, mapas GPS e ditado por voz.
- **Portal de Fornecedores (`/fornecedor`):** Espaço restrito onde fornecedores externos submetem cotações. Utiliza conta própria definida aquando do convite por email.

---

## 3. Interface Principal e Navegação

### 3.1 Menu Lateral Esquerdo
A visibilidade de cada secção depende rigorosamente dos módulos contratados e das permissões atribuídas ao seu grupo de utilizadores em **Configurações → Grupos**:

| Secção | Menus Principais | Finalidade Operacional |
| :--- | :--- | :--- |
| **Início** | Painel (`/admin`), Chat MCP | Página inicial de trabalho e assistente virtual |
| **Cadastro** | Terceiros, Artigos | Fichas de entidades (clientes/fornecedores) e engenharia de produto |
| **Produção** | Ordens de Produção, Stock, Planeamento (Gantt), MES, Estado da Fábrica | Controlo operacional de fabrico, postos de trabalho e chão de fábrica |
| **Pessoas** | Assiduidade (Relatório e Gantt) | Registo de picagens de ponto e presenças de colaboradores |
| **Comercial** | CRM, CRM Laskasas, Pedidos de Cotação, Aprovisionamento, Projetos, Pós-Venda, Circulares | Gestão de vendas, orçamentação à medida, compras, design e comunicados |
| **Logística** | Consulta de Stock, Armazéns, Terminal Móvel, Faturas OCR, AutoLog | Operações de armazém, mapas 3D, conferência de faturas e frotas |
| **Análise** | Relatórios de Atividade, Indicadores (BI), Consultas Dinâmicas | Extração de dados, tabelas dinâmicas e auditoria de ações |
| **Sistema** | Configurações Gerais, Sincronização Artsoft, Grupos, MRP | Definições globais, parametrização e permissões de segurança |

### 3.2 Barra Superior (Cabeçalho)
- **Pesquisa Geral:** Caixa central para procurar rapidamente artigos, ordens, clientes e documentos.
- **Registar Ponto:** Botão de picagem rápida de entrada/saída de assiduidade. Exibe ao lado o tempo acumulado no dia de hoje.
- **Suporte (?):** Atalho para abrir cliente de email com destino a `suporte@rebortec.com`.
- **Bandeja "Para Mim Hoje":** Notificador inteligente que agrupa tarefas pendentes sob a sua responsabilidade direta (ex.: artigos CDP a aguardar a sua viabilidade técnica, correções pendentes ou artigos prontos para precificação). O botão **Ver todos** abre a listagem já filtrada.
- **Sino de Notificações:** Alertas do sistema (ex.: novas mensagens de fornecedores, prazos atingidos, conclusões de processos).
- **Megafone:** Histórico de novidades e atualizações funcionais lançadas no Floow.
- **Menu do Utilizador:** Permite aceder ao resumo das picagens de ponto do dia, gerir tarefas pessoais, configurar preferências de notificações por email e efetuar logout.

### 3.3 Tarefas Pessoais
No menu de utilizador ou no Painel Principal (`/admin`), pode criar tarefas com título, descrição e data de conclusão. O sistema assinala automaticamente com cores de destaque as tarefas que terminam hoje ou que se encontram em atraso.

---

## 4. Gestão de Terceiros (Clientes e Fornecedores)

Aceda através de **Terceiros → Novo** ou **Terceiros → Lista**.
Este menu gere as fichas de entidades sincronizadas com o Artsoft ERP.

### Separadores da Ficha de Terceiro
- **Dados Gerais:** Nome, NIF, moradas, contactos telefónicos e email principal.
- **Cliente:** Apresenta o código interno de cliente Artsoft, condições de pagamento, limites de crédito e histórico de documentos de venda.
- **Fornecedor:** Apresenta o código interno de fornecedor (`providerid`). Contém o campo vital **Email Procurement**:
  - *Regra Operacional:* No módulo de Aprovisionamento, os convites de cotação são enviados obrigatoriamente para o **Email Procurement**. Se este campo estiver vazio, o sistema herda o email principal da entidade. Se ambos estiverem em branco, o fornecedor não pode ser convidado.

### Armazém de Trabalho do Colaborador
Na ficha de edição do próprio utilizador (no módulo de Pessoas/Configurações), define-se o **Armazém de Trabalho**. Este armazém passa a ser o valor padrão assumido automaticamente no Terminal Móvel de Logística e na filtragem de consultas.

---

## 5. Catálogo de Artigos e Engenharia de Produto

Aceda através de **Artigos → Lista**, **Artigos → Novo**, **Limites de Tamanho** ou **Wizard**.

### 5.1 Conceito de Artigo Base, Atributos e Artigos Filhos
- **Artigo Base (Pai):** É o modelo ou conceito mestre de engenharia (ex.: "Sofá Lisboa"). Não é uma referência faturável por si só; não tem stock transacionável. Define a estrutura base de materiais, limites de medidas e a lista de atributos configuráveis.
- **Atributos e Valores:** Variáveis de personalização (ex.: Atributo "Tecido" com valores "Veludo Cinza", "Pele Castanha"; Atributo "Pés" com valores "Metal Preto", "Madeira Carvalho").
- **Artigo Filho (Variante/SKU):** Uma combinação real e concreta de valores (ex.: "Sofá Lisboa em Veludo Cinza com Pés em Metal Preto"). Possui um código SKU próprio, ficha técnica individual e pode ser transacionado e fabricado.

### 5.2 Catálogo de Atributos e Valores (MRP)
Antes de associar atributos a um artigo base, estes têm de estar registados no catálogo global da empresa em **Configurações → MRP**:
1. Defina o nome do atributo e eventuais traduções multilíngues.
2. Crie os respetivos valores (opções). Pode associar **Tags** aos valores para facilitar a pesquisa e filtragem no catálogo.
3. *Atenção:* O nome plural do atributo serve apenas para organização interna do catálogo e nunca entra na descrição comercial do artigo gerado.

### 5.3 Configuração de Atributos na Ficha Base
No separador **Atributos** de um artigo base já gravado:
- Adicione atributos do catálogo e selecione quais os valores permitidos para este modelo específico.
- **Ordenação:** Arraste os atributos para definir a ordem sequencial em que aparecem na descrição final do artigo e no ecrã do Wizard.
- **Cor Predominante:** Pode sinalizar qual o atributo que define a cor principal do produto (coluna **Cor pred.**).
- **Herança de Valores:** Um atributo pode herdar valores de outro atributo existente na base.
- **Bloqueio Estrutural:** *Assim que a base for utilizada na criação de artigos filhos ou tiver movimentos, já não é permitido adicionar nem remover atributos da base.* Permite-se apenas acrescentar novos valores aos atributos existentes.
- **Limites de Personalização:** Para produtos de catálogo que permitem ajuste de tamanho, preencha as medidas mínimas e máximas de comprimento, largura e altura (em centímetros) e a opção "Tem tecido".
- **Tabela de Preços nas Variações:** Grelha no fundo do separador onde se cadastram faixas ou níveis de preços associados às variantes.

### 5.4 Mini-BOMs por Valor de Atributo
Cada valor de atributo pode ter a sua própria lista de materiais específica:
1. No separador Atributos da base, clique no botão **BOM** junto ao valor pretendido.
2. Abre-se a janela de Mini-BOM onde pode inserir: **Operações**, **Componentes** e **Matérias-Primas** com as respetivas quantidades.
3. **Indicador Visual:** O botão azul com contagem (ex.: `+3`) indica que o valor já tem 3 linhas de materiais. Um botão cinzento sem contorno indica Mini-BOM vazia.
4. **Copiar e Colar Mini-BOMs:** É possível copiar toda a estrutura de materiais de um valor e colá-la noutro valor idêntico através dos ícones da barra de ferramentas.

### 5.5 Grupos de Combinação de Mini-BOM
Utiliza-se quando a escolha conjunta de dois atributos altera a estrutura de fabrico de uma forma que não corresponde à simples soma das Mini-BOMs individuais (exemplo clássico: o acabamento dos pés combinado com a opção com/sem ponteiras exige uma estrutura metálica completamente diferente).
- Crie um **Grupo de Combinação** selecionando exatamente dois atributos da base.
- Dentro do grupo, crie **Regras** combinando um valor do atributo A com um valor do atributo B.
- Associe a lista de operações e materiais específica para essa regra combinada.
- *Regra Crítica de Bloqueio:* Quando um grupo de combinação está ativo, a sua regra **substitui** as Mini-BOMs isoladas desses atributos. Se a combinação escolhida no Wizard não tiver uma regra cadastrada, a geração da BOM do filho é **bloqueada** com aviso de erro.

### 5.6 Lista de Materiais Principal (BOM)
No separador **Materiais (BOM)**:
- Contém as operações e materiais comuns a todas as versões do artigo.
- **Origem das Linhas na Ficha do Filho:**
  - `—` (Traço): Material herdado da estrutura comum do artigo base.
  - `Mini-BOM`: Material derivado da escolha de um valor de atributo individual.
  - `Combinação`: Material derivado de uma regra de combinação de mini-BOM.
  - `Manual`: Material adicionado ou alterado manualmente na ficha desse filho específico.
- **Dicionário de Consumo por Intervalos:** Na base, permite definir fórmulas onde o consumo de matérias-primas varia em degraus consoante a medida final (comprimento/largura).

### 5.7 Gestão de Filhos e Regeneração de BOM
No separador **Filhos** da base:
- Lista todos os SKUs gerados, indicando se a BOM está validada (**BOM OK**).
- **Atualizar BOM:** Permite regenerar em lote a lista de materiais de filhos standard, aplicando as alterações mais recentes feitas nas Mini-BOMs da base. Filhos com alterações manuais não são sobrescritos acidentalmente.
- **Aprovar/Desaprovar BOM em Bloco:** Ações reservadas a perfis com permissão de aprovação técnica.

### 5.8 Assistente de Criação de Variantes (Wizard)
Localizado em `Artigos → Wizard` (`/admin/product/wizard`):
1. Escolha o artigo base e assinale os valores pretendidos para cada atributo.
2. O sistema calcula e exibe em tempo real o número total de combinações que serão geradas.
3. **Limites de Processamento:**
   - **Até 30 Combinações:** O processamento corre em tempo real e os novos artigos surgem imediatamente no ecrã.
   - **Entre 31 e 500 Combinações:** A geração é automaticamente enviada para a fila de processamento em segundo plano (*background job*). O utilizador recebe um email com a confirmação e listagem dos artigos criados assim que a tarefa terminar. O estado da fila pode ser acompanhado no separador **Envios por email**.
   - **Acima de 500 Combinações:** A operação é bloqueada por segurança para evitar sobrecarga no servidor e inconsistências no ERP. O utilizador deve segmentar a seleção.

### 5.9 Gestão de Mídia, Desenhos Técnicos e Replicação
No separador **Midia** da ficha do artigo:
- **Anexos Gerais:** Documentos comerciais, manuais de montagem e PDFs.
- **Anexos Técnicos:** Ficheiros CAD, DXF, DWG e desenhos industriais.
- **Imagens para Web:** Fotografias para e-commerce e catálogo, com ferramenta de carregamento múltiplo.
- **Associar Anexos a Atributos:** Permite definir que um determinado ficheiro técnico só diz respeito a certas opções de acabamento.
- **Replicar para Filhos:** Propaga ficheiros carregados na base para todas as fichas dos filhos. Se a opção de replicação contínua estiver ativada, a remoção do anexo nos filhos exige que seja apagado na base.
- *Histórico e Auditoria:* Ficheiros removidos da ficha permanecem acessíveis no histórico de auditoria em **Atividade** para consulta de versões antigas.

### 5.10 Fichas Técnicas, Folhas de Cálculo e Histórico de Atividade
- **Fórmulas de Folha de Cálculo:** Pode integrar tabelas com fórmulas dinâmicas tipo Excel (`=A2*B2`, `=COMPRIMENTO-20`). Com a função especial `=ATRIB("NomeAtributo")`, a folha injeta o valor real configurado no artigo filho (ex.: nome da tela ou espessura da madeira).
- **Criação de Versões Formais:** No separador Atividade, além do log cronológico detalhado de quem alterou o quê (com comparação antes/depois), é possível registar marcos de versão formais (v1.0, v2.0) com datas de entrada em vigor e memorandos técnicos.

---

## 6. BOM Paramétrica (fx Paramétrica)

A BOM Paramétrica representa o expoente máximo da engenharia no Floow, permitindo configurar produtos altamente complexos e customizáveis através de lógica matemática, condicional e procedural sem recorrer a código de programação inseguro.

### 6.1 Conceito e Filosofia de Não-Rutura (Opt-In)
- **Ativação Opcional:** A camada paramétrica é ativada individualmente por produto (**Opt-In**). Um artigo sem parametrização ativa continua a funcionar no modo tradicional sem qualquer impacto.
- **Reutilização de Linhas Existentes:** A parametrização não cria uma base de dados paralela de materiais. Cada nó da árvore paramétrica referencia diretamente uma linha de BOM/Mini-BOM existente através do identificador `bom_line_id`.
- **Segurança Absoluta:** As fórmulas são analisadas exclusivamente pelo avaliador seguro do servidor (*Safe AST Evaluator*). É rigorosamente proibido o uso de `eval()` ou execução de código JavaScript não sanitizado.
- **Simulação em Memória:** Os testes de cálculo e simulações de medidas ocorrem estritamente em memória volátil, sem gravar linhas no banco de dados até à aprovação formal de fabrico.

### 6.2 Estrutura do Modelo: Parâmetros e Nós
A definição técnica organiza-se em duas secções fundamentais:
1. **Parâmetros Globais (`parameters`):** Variáveis de entrada que alimentam o configurador (ex.: `largura = 2400`, `profundidade = 900`, `lugares = 3`).
2. **Nós Estruturais (`nodes`):** Representam os componentes e operações de fabrico ligados às linhas da BOM real. Cada nó define a sua quantidade, dimensões físicas (comprimento, largura, espessura), condições de ativação e regras de repetição.

### 6.3 Tipos de Origem de Dados (Sources)
Ao configurar qualquer campo num nó paramétrico, pode escolher entre quatro origens:
- `fixed`: Valor constante e estático (ex.: `value = 1`).
- `variable`: Valor dinâmico recebido do utilizador/orçamento, com suporte para valor por defeito (`default`).
- `formula`: Expressão matemática ou lógica avaliada em tempo real.
- `inherited`: Cópia direta do valor de outro campo ou nó de referência.

### 6.4 Expressões Matemáticas, Condições e Repetições
- **Operadores Suportados:** Adição (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`), parênteses, comparações lógicas (`<`, `<=`, `>`, `>=`, `==`, `!=`) e literais booleanos (`true`, `false`).
- **Condição de Inclusão (`condition`):** Expressão booleana que decide se a peça entra ou não na produção (ex.: `parent.lugares > 2`). Se o resultado for falso, o componente e os seus filhos são excluídos do fabrico.
- **Repetição em Série (`repeat`):** Permite multiplicar a quantidade de uma peça com base numa regra (ex.: número de pés em função do comprimento). Possui um teto de segurança configurável (máximo padrão de 1000 repetições por nó) para impedir ciclos infinitos.

### 6.5 Sintaxe de Referências Relativas e Absolutas
O editor permite navegar na hierarquia do produto com extrema flexibilidade:
- **Referências Relativas:**
  - `self.campo` — Lê outro campo do próprio nó (ex.: calcular o peso com base em `self.qty * self.espessura`).
  - `parent.campo` — Lê um parâmetro do nó pai (se estiver na raiz, lê os parâmetros globais).
  - `sibling.chave.campo` — Lê um campo de uma peça irmã (ex.: o rodapé lê a largura calculada para o armário).
  - `children.chave.campo` — Lê um valor de um nó filho direto.
- **Referências Absolutas:**
  - `params.nome_parametro` — Aponta diretamente para a variável de entrada global.
  - `nodes.modulo.assento.qty` — Caminho completo pontuado na árvore de engenharia.

### 6.6 Motor Processual Avançado (`engine: "process"`)
Para cenários de marcenaria e engenharia avançada, o Floow disponibiliza o motor declarativo recursivo (`engine: "process"`):
- Permite carregar tabelas de consulta determinísticas (`lookups`), por exemplo para mapear tipos de material para espessuras reais de placa.
- **Funções Especiais do Motor:**
  - `@LOOKUP('tabela', chave)` — Procura um valor exato numa tabela técnica.
  - `@IFF(condicao, valor_se_verdadeiro, valor_se_falso)` — Decisão condicional em linha.
  - `@NOT(expressao)` — Negação lógica.
  - `@FLOAT(expressao)` — Conversão numérica segura.
  - Operadores lógicos `AND` e `OR`.
- Suporta nós do tipo `component`, `consumption` e `operation`, e permite expansão recursiva de subprocessos através de `select.type = "process"`.

### 6.7 Validação de Ciclos, Dependências e Simulação em Tempo Real
Ao editar a BOM paramétrica, o servidor executa uma análise estática completa da estrutura:
- **Deteção de Dependências Circulares:** Impede que a peça A dependa da peça B enquanto a peça B depende da peça A.
- **Painel "Depende de / Afeta":** Apresenta graficamente o mapa de impacto. Ao alterar um parâmetro, vê instantaneamente que peças sofrerão alterações na quantidade ou medidas.
- Se existirem referências a nós inexistentes, divisões por zero ou fórmulas malformadas, o sistema bloqueia a gravação e detalha a linha com erro.

### 6.8 Geração de Snapshot Imutável para Fabrico
Quando uma encomenda comercial é aprovada ou uma Ordem de Fabrico é lançada:
1. O resolvedor do Floow processa a definição paramétrica com os dados reais do pedido.
2. É gerado um **Snapshot de BOM Normal**: uma lista plana e perfeitamente padronizada contendo operações e materiais com quantidades fechadas, exatamente no formato compreendido pelo MRP e pelas Ordens de Fabrico do Artsoft.
3. Este snapshot é gravado de forma imutável (`parametric_bom_snapshots`). Alterações futuras nas regras de engenharia da base nunca alteram ordens de produção que já foram lançadas para fábrica.

---

## 7. Gestão e Planeamento da Produção

Aceda através do menu **Produção**.

### 7.1 Ordens de Produção e Acompanhamento Operacional
Em `/admin/planninglaunches`:
- Listagem operacional de todas as ordens de fabrico em aberto e histórico.
- **Indicador de Progresso:** Cada ordem exibe a **última operação picada no chão de fábrica**, a data/hora exata do registo e, no caso de componentes intermédios, o código do respetivo subartigo.

### 7.2 Análise de Stock para Produção
Em `/admin/orders-stock-analysis`:
- Cruza as necessidades de matérias-primas e componentes de todas as ordens ativas com o saldo real existente no ERP Artsoft.
- A coluna **Disponível** reflete o stock físico descontando as cativações já comprometidas.

### 7.3 Gestão de Subcontratados
Em `/admin/subcontractlaunches`:
- Gestão de operações executadas fora da fábrica (ex.: lacagem, cromagem, estofamento exterior). Permite controlar datas de saída, guias de transporte e retornos de material.

### 7.4 Planeamento Visual (Calendário Gantt) e Gestão de Carga
Em `/production-planning`:
- Calendário interativo de operações por posto de trabalho, visualizável em escala diária, semanal ou mensal.
- **Interação:** As ordens podem ser arrastadas no tempo para reordenar o fabrico. O servidor valida automaticamente as dependências sequenciais e a disponibilidade de postos.
- **Painel de Carga dos Postos de Trabalho:**
  - 🔵 **Azul (Folga):** As horas de trabalho planeadas estão abaixo da capacidade máxima do posto no dia.
  - 🟢 **Verde (Capacidade Plena):** Carga perfeitamente balanceada e igual à capacidade.
  - 🔴 **Vermelho (Sobrecarga):** As ordens alocadas excedem a capacidade de trabalho do posto nesse dia. O gestor deve arrastar tarefas para dias anteriores/posteriores ou redistribuir postos.
- **Validação de Armazéns:** O sistema de planeamento bloqueia a criação ou movimentação de ordens caso falte o armazém de destino da entrada de stock ou o armazém de proveniência de matérias-primas nos postos da operação.

### 7.5 Análise de Planeado vs Real e Rentabilidade de Fabrico
No separador **Planeado vs Real** (`/production-planning?tab=profitability`):
- Compara minuto a minuto o tempo previsto de cada operação com o tempo real decorrido nas picagens do terminal MES.
- Compara as matérias-primas orçamentadas com os consumos reais registados.
- Calcula a rentabilidade da ordem somando o custo de mão-de-obra real (tempo efetivo multiplicado pelo custo/hora do posto) ao custo real das matérias-primas consumidas.

### 7.6 Visualização de Chão de Fábrica e Fábrica 3D
- **Estado da Fábrica (`/production-planning/factory-floor`):** Painel sinótico em grelha com cartões em tempo real por posto de trabalho, exibindo que operário está ativo, que ordem está em curso e tempos de paragem.
- **Fábrica 3D (`/production-planning/factory-palm`):** Representação visual tridimensional do layout fabril com indicação luminosa de postos em laboração, parados ou com alertas.

### 7.7 Ecrãs de TV e Capacidade dos Postos (KPIs Minutos/Dia)
- **Ecrãs TV:** Em **Configurações → Ecrãs TV**, configura-se o conteúdo exibido nos monitores suspensos nos pavilhões fabris (listas de prioridades de fabrico, métricas de produtividade, alertas de segurança).
- **KPIs (Minutos/Dia):** Em **Configurações → KPIs (minutos/dia)**, define-se a capacidade padrão de trabalho útil por dia em cada posto (ex.: 480 minutos/dia para um turno normal de 8 horas).

### 7.8 Gestão de MES no Escritório
Em **Produção → MES**:
- **Configurações:** Definição de regras de cativação, séries de documentos Artsoft para entrada de produto acabado e baixas de stock, e parametrização do questionário de embalamento.
- **Picagens:** Consulta detalhada de todos os registos de chão de fábrica. Permite autorizar a **Reabertura de Tarefas** terminadas por engano. *Regra:* Autorizar a reabertura apenas remove o bloqueio de segurança; o operador original mantém-se como responsável pelo tempo da tarefa.

### 7.9 Regras de Tempos de Espera (Lag Time) entre Operações
Certos processos fabris exigem um tempo obrigatório de secagem, cura ou arrefecimento após a sua conclusão física (ex.: colagem, secagem de verniz):
- O tempo de espera é parametrizado em minutos na linha da operação da BOM (`lag_time_minutes`).
- Enquanto o tempo de espera não decorrer, a operação seguinte na mesma ordem fica bloqueada no terminal móvel (código `LAG_TIME_ACTIVE`).
- **Desbloqueio de Emergência (Bypass):** Um supervisor com permissões específicas pode forçar o arranque imediato da operação introduzindo o seu **PIN de Supervisor** e registando uma justificação formal no terminal.
- Se a operação que impôs a espera for reaberta no escritório, o bloqueio das operações seguintes é cancelado automaticamente.

### 7.10 Impacto das Picagens no Stock do ERP Artsoft
Quando o sistema está configurado para emitir documentos oficiais no ERP:
1. **Ponto de Disparo Único:** A entrada de produto acabado e a baixa de consumo dos materiais saem **no mesmo documento oficial Artsoft**, exatamente na operação configurada como "Entrada de Stock" (ou, na sua ausência, na última operação da BOM). Nenhuma operação intermédia lança movimentos de stock.
2. **Proporcionalidade:** As quantidades baixadas de matérias-primas escalam proporcionalmente à quantidade de produto acabado picada.
3. **Bloqueio por Falha de Stock:** Se o Artsoft rejeitar o documento por falta de stock físico de alguma matéria-prima no armazém de saída, a entrada de produto acabado é igualmente abortada no ERP para evitar desequilíbrios contabilísticos.
4. **Resiliência e Idempotência:** A picagem de mão-de-obra do operário no Floow fica gravada com sucesso mesmo que o Artsoft falhe. O documento rejeitado segue para a fila de retentativas (`mes_artsoft_stock_retries`). O operador **nunca deve repetir a picagem de conclusão** para tentar contornar a mensagem, pois isso duplicaria os registos.
5. **Cativação Inteligente:** Se a cativação de stock estiver ativa, o documento final converte automaticamente as cativações prévias em consumos efetivos (`<onAcc>`).

---

## 8. Terminal Móvel de Chão de Fábrica (MES)

Aplicação otimizada para tablets industriais e ecrãs táteis distribuídos pelos postos de trabalho.

### 8.1 Ativação e Registo do Dispositivo Tablet
1. Ao aceder pela primeira vez no tablet, o ecrã exibe a mensagem **Terminal pendente** com um código de identificação único do equipamento.
2. Um administrador da fábrica deve aceder ao backoffice em **Produção → MES → Configurações**, localizar o código pendente e validar o registo, associando o tablet ao posto/setor correspondente.
3. Se for necessário substituir o tablet físico, clique em **Novo registo** no ecrã para gerar um novo código de emparelhamento.

### 8.2 Autenticação por PIN ou QR Code e Escolha de Contexto
- O operador identifica-se digitando o seu **PIN pessoal** de 4 a 6 dígitos ou apontando o seu crachá com **QR Code** para a câmara do tablet.
- **Contexto Operacional:** O operador seleciona o **Setor** ou a **Operação** em que vai trabalhar (ex.: Corte, Marcenaria, Folha, Acabamento). Se o terminal estiver bloqueado a uma operação específica, o operador só pode picar ordens dessa etapa.

### 8.3 Modo de Ordem de Fabrico Libertada vs Picagem Ad-Hoc
- **Modo Ordem Libertada (Padrão de Fábrica):** Exige que a ordem tenha sido previamente libertada pelo planeamento no escritório. A leitura de um código de lançamento apenas inicia operações da ordem se esta estiver no estado "Libertada" ou "Em Curso". Se a ordem estiver retida, o terminal rejeita a leitura e exibe: *"Lançamento sem ordem de fabrico libertada"*.
- **Modo Ad-Hoc (Sem BOM):** Utilizado em fábricas ou setores que apenas pretendem registar tempos de presença e mão-de-obra sem seguir uma sequência rígida de materiais. Neste modo, a ordem das operações da BOM é ignorada, mas a entrada de stock no Artsoft só é despoletada na operação que tiver essa função expressamente atribuída.
- **Dependência de Componentes Filhos:** Numa ordem de montagem com lista de materiais rígida, as operações do produto final não arrancam enquanto as ordens de fabrico dos componentes intermédios não estiverem totalmente concluídas.

### 8.4 Ciclo de Trabalho: Iniciar, Suspender, Retomar e Terminar
- **Iniciar:** O operador faz a leitura do código de barras da folha de obra. A tarefa transita para o estado **Em Curso** e o cronómetro de mão-de-obra começa a contar.
- **Pausar / Suspender:** Se o operador tiver de interromper a tarefa (ex.: para almoço, reunião ou falta momentânea de material), clica no botão **Suspender**. O cronómetro pára e o estado passa a **Suspenso**.
- **Retomar:** O operador clica no cartão da tarefa suspensa ou volta a ler o código de barras para reativar a contagem.
- **Terminar:** Ao finalizar o fabrico das peças, clica em **Concluir**. Se não houver validações pendentes, o trabalho transita para **Terminado**.

> [!CAUTION]
> **Bloquear o Ecrã NÃO Pára o Tempo!**
> Simplesmente desligar o ecrã do tablet, fechar o browser ou sair com o botão de PIN **NÃO suspende a tarefa**. O tempo de mão-de-obra continua a acumular indefinidamente até que o operador clique formalmente em **Suspender** ou **Terminar**.

### 8.5 Trabalho em Grupo e Conclusão Coletiva
Quando um posto trabalha em lote com múltiplas peças da mesma série:
- O operador pode picar vários códigos de obra sucessivamente para criar um **Grupo de Trabalho**.
- As ações de pausa, retoma e conclusão são aplicadas a **todas as ordens do grupo em simultâneo**.
- *Regra Estrita:* Não é permitido concluir apenas uma ordem individual que pertença a um grupo em curso. O lote tem de ser terminado em conjunto.

### 8.6 Suspensão Automática de Turnos e Segurança de Ecrã
- O Floow possui um mecanismo de segurança agendado (`mes:auto-suspend`) que suspende compulsoriamente todas as tarefas ativas na fábrica a horas pré-determinadas (ex.: 12:30 para almoço e 17:30 para final de turno).
- Isto impede que tarefas esquecidas continuem a acumular centenas de horas de mão-de-obra fantasma durante a noite.
- O botão **Bloquear** no tablet tranca a interface com proteção de PIN para evitar toques acidentais, mantendo o trabalho ativo em segurança.

### 8.7 Interrupções por Lag Time e Desbloqueio por Supervisor
Se a operação lida tiver um tempo de espera decorrente da operação anterior:
- O ecrã exibe um aviso amarelo com a indicação dos minutos em falta para libertação da peça.
- Um encarregado de fábrica pode autorizar o início imediato introduzindo o seu **PIN de Supervisor** e escolhendo o motivo da exceção.

### 8.8 Perguntas de Embalamento (Volumes, Medidas e Peso) antes da Entrada de Stock
Se o parâmetro de embalamento estiver ativo nas definições do MES:
1. No exato momento em que o operador clica para concluir a última operação que gera entrada de stock, o terminal interrompe o fecho e abre uma janela modal obrigatória:
   - Número total de volumes do artigo (caixas/embalagens);
   - Comprimento, largura e altura de cada volume (em cm);
   - Peso bruto de cada volume (em kg).
2. Se estes dados já tiverem sido preenchidos previamente na engenharia do produto, o terminal não volta a perguntar.
3. Os dados podem ser gravados no artigo base ou exclusivamente na variante, e o número de volumes é sincronizado com o campo adicional correspondente no Artsoft ERP (`cduN`).

### 8.9 Reabertura de Tarefas Concluídas
Se uma ordem foi marcada como concluída por lapso e ainda necessita de acertos:
- A reabertura no terminal exige a validação presencial de um supervisor com o seu **PIN de Supervisor**.
- O Floow regista a auditoria da reabertura, mas mantém o operador original associado ao histórico de tempos.

---

## 9. Gestão de Assiduidade e Controlo de Ponto

Aceda através do menu **Assiduidade**.

### 9.1 Distinção Fundamental entre Ponto e MES
- **Picagem de Ponto (Assiduidade):** Regista a presença física do colaborador na empresa (hora de entrada e saída diária). Faz-se no botão **Registar Ponto** do cabeçalho web ou no quiosque de ponto.
- **Picagem de Operação (MES):** Regista o tempo de execução dedicado a uma tarefa ou ordem de fabrico específica no chão de fábrica.
- *São bases de dados e contagens completamente distintas.* O registo de ponto não avança tarefas de fábrica, e picar uma ordem no MES não substitui a picagem do ponto de entrada do dia.

### 9.2 Relatórios e Mapas de Ponto
- **Relatório de Ponto (`/attendance/report`):** Grelha detalhada com as entradas, saídas, intervalos e total de horas normais e suplementares trabalhadas por colaborador num determinado intervalo de datas.
- **Gantt de Ponto (`/attendance/gantt`):** Visualização cronológica em barras que permite identificar rapidamente atrasos, saídas antecipadas, ausências e sobreposições de horários.

---

## 10. CRM — Gestão de Relacionamento Comercial

Aceda através do menu **CRM** (quando ativo na instalação).
Destina-se ao controlo do funil comercial genérico e oportunidades de venda standard da empresa.

### 10.1 Pipeline (Quadro Kanban)
- Vista em colunas representando os estágios do ciclo de venda (ex.: Contacto Inicial, Qualificação, Apresentação de Proposta, Negociação, Ganho, Perdido).
- Os negócios são representados por cartões que podem ser arrastados entre colunas para atualizar o estágio em tempo real.
- Suporta filtros por comercial responsável, valor monetário e intervalo de datas previstas de fecho.

### 10.2 Leads e Oportunidades
- **Leads:** Registo de contactos e prospetos iniciais não qualificados. Um lead pode ser promovido a Oportunidade com um único clique, escolhendo-se o estágio inicial no pipeline.
- **Oportunidades:** Negócios formais em curso com valor associado, cliente, probabilidade de fecho e histórico de atividades.
- **Cotações no CRM:** Permite anexar propostas comerciais à oportunidade.
- *Nota Diferenciadora:* O CRM genérico destina-se a vendas correntes. Para peças de mobiliário à medida, desenvolvimentos técnicos especiais e estudos de viabilidade, o circuito obrigatório é o de **Pedidos de Cotação (CDP)**.

---

## 11. CRM Laskasas — Ferramentas Comerciais Avançadas

Módulo comercial altamente especializado vocacionado para redes de lojas e acompanhamento analítico diário de equipas de vendas de mobiliário.

### 11.1 Folha de Acompanhamento Comercial (Grelha Excel)
Localizada em `CRM Laskasas → Grelha Comercial` (`/crmlaskasas`):
- Interface tipo folha de cálculo interativa onde os comerciais de loja registam e monitorizam as suas propostas comerciais, orçamentos e vendas efetivas.
- Permite ordenar, filtrar e editar valores em linha com sincronização instantânea.
- Inclui categorização por loja, comercial, tipo de cliente e origem da oportunidade.

### 11.2 Dashboard de Performance por Loja (PV 26)
Localizado em `CRM Laskasas → Performance por Loja` (`/crmlaskasas/dashboard-loja` ou `/crmlaskasas/lojas/{id}/analise`):
- Ecrã analítico executivo que replica o modelo de controlo **PV 26** de vendas a retalho.
- **Seletores Superiores:** Permite alternar entre lojas individuais ou selecionar a opção **Consolidado (Todas as Lojas)**, escolhendo o ano e o mês de referência.
- **Métricas e Estrutura de Tabelas:**
  - **Performance YTD (Year-To-Date):** Percentagem de cumprimento de objetivos acumulada desde o início do ano até à data atual (destaque a verde para valores $\ge 100\%$, vermelho para valores abaixo do objetivo).
  - **Performance Trimestral:** Percentagem de concretização desagregada por trimestres (Q1, Q2, Q3, Q4).
  - **Tabela Mensal (Janeiro a Dezembro):**
    - Linha de **Objetivo de Vendas (Meta)** em destaque a preto;
    - Linhas de vendas faturadas, orçamentos em aberto e desvios;
    - Total anual acumulado na coluna final.
- Atualizado em tempo real utilizando caches inteligentes do sistema, sem gerar lentidão no ERP Artsoft.

### 11.3 Análise Global de Vendas e Previsões (Forecast)
Localizado em `CRM Laskasas → Análise Global & Forecast` (`/crmlaskasas/analise`):
- Painel executivo com cartões KPI (Volume Total Faturado, Ticket Médio por Venda, Taxa de Conversão de Orçamentos).
- Gráficos de tendências e previsões de fecho de vendas para o mês em curso com base no histórico de conversão e orçamentos pendentes de aprovação pelo cliente.

---

## 12. Pedidos de Cotação de Peças Especiais (CDP)

O módulo **CDP (Cotação e Desenvolvimento de Produto)** gere o fluxo interno rigoroso para orçamentar produtos feitos sob medida, acabamentos especiais ou modificações de peças de catálogo.

### 12.1 Criação do Pedido Comercial
Aceda a **Pedidos de cotação → Novo pedido** (`/cdp/cotacoes/new`):
- **Loja (Armazém Artsoft):** Seleção obrigatória da loja ou filial responsável pela venda. Os armazéns internos 101, 439 e 501 estão excluídos por parametrização de segurança.
- **Cliente:** Seleção da entidade compradora.
- **Artigos do Pedido:** Um único pedido pode conter múltiplos artigos independentes. Para cada artigo, introduza o nome, descrição técnica detalhada e anexe esboços, fotografias de inspiração ou ficheiros CAD.
- **Código CDP (Opcional):** Identificador interno do comercial (até 30 caracteres alfanuméricos).
- **Tipo de Cliente:** Seleção obrigatória entre **Cliente final**, **Profissional** ou **Parceiro**.
- **Valor Total de Produtos Standard (EUR):** Montante em euros das peças de catálogo normal que acompanham este pedido especial no orçamento do cliente.
- **Notificar no Preço:** Campo de colaboração essencial. Os colegas adicionados aqui:
  - Recebem notificações automáticas quando os preços forem calculados;
  - Têm permissão total para editar artigos, anexos, adjudicar ou perder o pedido exatamente como o criador original;
  - *Restrição:* Apenas o criador original do pedido pode apagar o pedido.
- **Numeração Automática:** Cada versão de artigo recebe um código único no formato:
  $$\text{COT-}\{\text{ID Criador}\}\text{-}\{\text{Sequencial}\}\text{-V}\{\text{Versão}\} \quad \text{(Exemplo: } \text{COT-12-5-V1}\text{)}$$

### 12.2 Ciclo de Viabilidade Técnica e Devolução para Correção (R1, R2...)
1. **Aguarda Viabilidade:** O artigo entra na fila dos engenheiros técnicos com perfil **Técnico**. O técnico analisa a viabilidade construtiva da peça e pode indicar um responsável pelo desenvolvimento técnico.
2. **Confirmação ou Devolução:**
   - **Confirmar Viabilidade:** O técnico valida o fabrico da peça e o artigo avança de imediato para a fase seguinte (**Aguarda Preço**).
   - **Devolver para Correção:** Se faltarem medidas, desenhos ou especificações, o técnico clica em Devolver, indica o destinatário e redige o motivo da rejeição (podendo anexar ficheiros de esclarecimento).
3. **Revisões e Histórico de Desenhos (R1, R2...):**
   - Ao devolver, os ficheiros antigos do artigo são automaticamente arquivados com o prefixo **R1**, **R2**, etc., mantendo-se disponíveis para consulta histórica.
   - *Regra Obrigatória:* O comercial responsável pela correção **é obrigado a anexar pelo menos um ficheiro novo corrigido** para que o sistema permita submeter novamente o artigo para viabilidade.
4. **Anulação de Viabilidade por Engano:** Enquanto o artigo ainda não tiver preços registados, o técnico que validou a viabilidade pode clicar em **Anular viabilidade**, fazendo o artigo regressar ao estado "Aguarda viabilidade" sem perda de dados.

### 12.3 Atribuição de Preço (Preço A, B e C)
Com a viabilidade aprovada, o artigo entra na bandeja da equipa de orçamentação com perfil **Cotação**:
- **Preço A (Obrigatório):** Preço de venda base calculado para a peça. Ao guardar o Preço A num artigo que já tem SKU gerado, o Floow atualiza automaticamente a tabela de preços do produto no sistema (`pv_1`).
- **Preço B (Obrigatório):** Segundo patamar de preço. Exige obrigatoriamente o preenchimento de uma **justificação textual** (ex.: margem reduzida para grandes quantidades ou preço de campanha).
- **Preço C (Opcional):** Terceiro patamar de preço de exceção. Se for introduzido um valor numérico, a justificação passa a ser obrigatória.
- Os preços podem ser reajustados a qualquer momento pela equipa de cotação, mesmo após a adjudicação do pedido.

### 12.4 Decisão Comercial: Adjudicação ou Perda
Quando o artigo possui Viabilidade Concluída e Preços A e B gravados, transita automaticamente para **Pronto para Resultado**:
- O criador e os utilizadores em "Notificar no Preço" recebem um email a informar que o preço está disponível.
- **Adjudicar:** O comercial clica em Adjudicado quando o cliente aprova o negócio. Pode optar por adjudicar apenas aquele artigo, vários artigos selecionados ou todos os artigos do pedido em simultâneo.
  - *Bloqueio de Cliente:* No primeiro artigo adjudicado, o sistema exige a confirmação formal do cliente. A partir desse instante, o cliente do pedido fica blindado e já não pode ser alterado (a menos que a adjudicação seja retirada).
- **Perdido:** Se o cliente recusar a proposta, o artigo é marcado como Perdido. A partir deste estado, o comercial pode clicar em **Nova Versão do Artigo** (gerando a versão `V2`) para propor ajustes de materiais ou medidas e reiniciar o ciclo.
- **Ações de Administrador do Módulo:**
  - **Retirar de Adjudicado:** Reverte o artigo para "Pronto para Resultado" sem apagar as viabilidades nem os preços já calculados.
  - **Alterar Estado:** Permite forçar manualmente a correção do estado do artigo mantendo o histórico de auditoria intacto.

### 12.5 Gestão Documental e Desenhos Assinados
- **Congelamento de Anexos Gerais:** Assim que um artigo recebe viabilidade ou preço, a sua área de anexos gerais fica congelada contra novas adições ou remoções para preservar o histórico do que foi orçamentado.
- **Categorias Especiais:**
  - **Desenho Final:** Onde a engenharia carrega o desenho CAD/PDF definitivo de fabrico (opcional para precificar).
  - **Desenho Assinado pelo Cliente:** Onde o comercial carrega a proposta aprovada e rubricada pelo cliente. No primeiro carregamento deste ficheiro, o sistema envia um email comemorativo ao criador confirmando a conclusão comercial da peça.

### 12.6 Retificação de Medidas no Cliente e Criação do C971 no Artsoft
Para peças de grande envergadura (ex.: roupeiros embutidos, cozinhas, painéis de parede), a adjudicação exige uma visita técnica ao local da obra para confirmar medidas milimétricas:
1. No artigo Adjudicado, aceda à secção de **Retificação de Medidas**.
2. **Atribuição Obrigatória:** É obrigatório selecionar pelo menos um **Técnico de Medições** para conseguir gravar o registo. Pode também indicar um **Designer a notificar**.
3. **Criação Automática do Documento C971 no ERP Artsoft:**
   - No exato momento em que a retificação de medidas é criada no Floow, o sistema comunica com o Artsoft e **gera automaticamente um documento de serviço C971** associado ao cliente do pedido.
   - O documento sai com preço zero, quantidade 1, e insere o código do artigo e do pedido na descrição suplementar.
   - O número oficial do Artsoft (ex.: `C971/123`) fica permanentemente gravado e visível na ficha da retificação no Floow.
4. **Campos da Ficha:**
   - **Retificação de Medidas:** Campo de preenchimento técnico exclusivo do técnico de medições;
   - **Notas de Retificação (Loja):** Informações de acesso à obra fornecidas pela loja comercial;
   - **Data Marcada:** Agendamento da visita presencial.
5. **Fechar Retificação:** O técnico clica em Fechar após validar o local. O sistema regista a data efetiva da visita, notifica o designer por email e liberta a peça para o fabrico definitivo.

### 12.7 Aplicação Móvel de Retificações no Terreno (`/cdp/app`)
Aplicação PWA dedicada para tablets de técnicos de medição:
- Exibe a agenda das visitas atribuídas ao técnico.
- **Navegação GPS:** Botão direto para abrir a morada da obra no Google Maps ou Apple Maps.
- **Chamada Rápida:** Atalho para ligar para o telefone do cliente.
- **Recolha Multimédia:** Permite capturar fotografias do espaço através da câmara do tablet, que ficam arquivadas na pasta "Anexos do Local".
- **Ditado por Voz:** Campo de medidas compatível com reconhecimento de voz para registar dimensões sem pousar a fita métrica.
- **Georreferenciação:** Ao fechar a retificação no local, se o GPS estiver ativo, a aplicação regista as coordenadas geográficas e desenha um minimapa de localização no detalhe do pedido.

### 12.8 Relatórios e Análises Estatísticas do CDP
Em `Pedidos de cotação → Análises` (`/cdp/cotacoes/analises`):
- Relatório estatístico por datas analisando: total de pedidos criados, artigos cotados, taxa de sucesso de adjudicação, rácio de peças perdidas, tempos médios de resposta de viabilidade e de preço.
- Gráficos comparativos por loja, comercial e categoria de produto.
- **Exportação Excel Multicomponente:** O botão de exportação gera um ficheiro XLSX estruturado em folhas separadas (*Resumo*, *Estados*, *Indicadores*, *Evolução Mensal*, *Por Loja*, *Por Criador*).

---

## 13. Aprovisionamento (Procurement / RFQ a Fornecedores)

Módulo concebido para auscultar o mercado e solicitar cotações de preços de matérias-primas, tecidos ou componentes a múltiplos fornecedores externos em simultâneo (Request for Quotation — RFQ).

### 13.1 Criação e Estruturação do Pedido de Cotação
Aceda a **Aprovisionamento → Novo pedido** (`/procurement/pedidos/novo`):
- **Referência Automática:** Gera o identificador sequencial `PR-AAAA-NNNN` (ex.: `PR-2026-0003`).
- **Título e Notas Internas:** Informação confidencial de controlo da equipa de compras.
- **Observações Públicas e Anexos:** Texto explicativo e ficheiros técnicos que os fornecedores convidados verão no portal.
- **Artigos do Pedido:** Cada linha representa uma necessidade (descrição da peça, quantidade pretendida e unidade de medida). Cada artigo possui a sua numeração sequencial: `{pedido}-A{sequência}-V{versão}` (ex.: `PR-2026-0003-A1-V1`).

### 13.2 Seleção de Fornecedores e Envio de Convites
- Na linha de cada artigo, clique em **Adicionar Fornecedor**. Pode associar o fornecedor apenas a essa linha ou a todas as linhas do pedido de uma vez só.
- O sistema pesquisa os fornecedores sincronizados do Artsoft.
- **Validação de Email:** O sistema valida a existência de email (prioritariamente o *Email Procurement* da ficha do terceiro). Se a entidade não tiver email registado, a linha fica inativa e exibe: *"Sem email — não é possível convidar"*.
- **Guardar Rascunho vs Enviar Pedido:**
  - **Guardar Rascunho:** Mantém o processo em edição livre. Nenhum contacto externo é estabelecido.
  - **Enviar Pedido:** Altera o estado para **Enviado** e despacha convites individuais por email a todos os fornecedores das linhas com links diretos e seguros para o portal.

### 13.3 Portal Externo do Fornecedor (`/fornecedor`)
- O fornecedor acede ao endereço `/fornecedor` sem necessitar de conta interna no Floow.
- No primeiro acesso, o link do email convida-o a definir a sua palavra-passe com base no seu endereço de email de receção.
- **Submissão de Proposta:** No portal, o fornecedor consulta os detalhes técnicos e os anexos, e introduz:
  - **Preço Unitário (€):** O valor total é calculado automaticamente pelo sistema multiplicando pela quantidade;
  - **Prazo de Entrega (em dias):** Tempo de resposta para fornecimento;
  - **Observações Comerciais:** Condições de transporte, validade da proposta, etc.
- **Sigilo Concorrencial Total:** O fornecedor tem visibilidade estrita e exclusiva sobre a sua própria cotação. Não tem acesso a dados de outros concorrentes nem sabe quem mais foi consultado.

### 13.4 Mensagens Bidirecionais e Esclarecimento de Dúvidas
- O portal disponibiliza um canal de mensagens diretas por artigo com suporte a anexos.
- Sempre que um fornecedor escreve uma pergunta no portal, o criador do pedido de compras recebe um email de alerta no Floow.
- A resposta do comprador no Floow é imediatamente refletida no portal do fornecedor, ficando todo o histórico de esclarecimentos centralizado e auditado.

### 13.5 Comparação de Propostas e Adjudicação Interna Sigilosa
- No detalhe do pedido no Floow, o comprador visualiza uma tabela comparativa com todas as propostas recebidas (preços, prazos, estados: *Enviado*, *Visto*, *Cotado*).
- **Adjudicar:** O comprador clica no botão verde **Adjudicar** na linha da melhor proposta.
- *Regra de Sigilo Comercial:* A adjudicação é uma **decisão estritamente interna**. O Floow **NÃO envia nenhum email** aos fornecedores a anunciar o vencedor nem altera o estado das propostas no portal exterior. A adjudicação serve apenas para seleção de fornecedor e encaminhamento da ordem de compra formal.

### 13.6 Interligação entre CDP e Aprovisionamento
- Num pedido de cotação especial (CDP), na versão mais recente de um artigo, existe o botão **Gerar Aprovisionamento**.
- Ao clicar, o Floow cria automaticamente um rascunho de pedido de compras no Procurement contendo os artigos e descrições do CDP. Pode também importar todos os desenhos técnicos através do botão **Importar anexos CDP**.
- Na ficha do CDP, a coluna **Cotação Forn.** passa a refletir em tempo real o estado das compras (*Por pedir*, *Parcial* ou *Pedida*), e a equipa comercial consegue ver os preços dos fornecedores à medida que são introduzidos.

---

## 14. Projetos de Decoração

Localizado em **Projetos** (manual em `/decoration-projects/manual`).
Gere todo o ciclo de vida de projetos de arquitetura de interiores, distribuição de ambientes, mobiliário e apresentação interativa a clientes.

### 14.1 Tipologias de Projeto
Ao criar um projeto em **Projetos → Novo**, deve escolher obrigatoriamente uma de quatro tipologias:
1. **Estudo de Planta:** Estudo preliminar de distribuição espacial de divisões e zonamento. Ativa o Wall Builder 2D.
2. **Projecto 2D:** Projeto detalhado de layout bidimensional com colocação de móveis e paredes. Ativa o Wall Builder 2D.
3. **Projecto 3D:** Desenvolvimento volumétrico e de renderização tridimensional de ambientes.
4. **Desenhos Técnicos:** Produção de peças desenhadas técnicas para carpintaria.
   - *Exceções de Desenhos Técnicos:* Não apresenta campos de preços nem importação de orçamentos Artsoft; os anexos não são de carregamento obrigatório para gravar.

### 14.2 Criação e Configuração da Equipa de Design
- **Nome do Projeto:** Editável clicando diretamente no título da ficha.
- **Cliente:** Seleção do cliente no catálogo.
- **Participantes (Designers):** São os técnicos de design alocados ao projeto. Têm permissões completas de edição sobre os ambientes, plantas e anexos exatamente como o criador. *Apenas o criador original pode apagar o projeto.*
- **Datas do Projeto:**
  - **Data Prevista:** A única data editável manualmente (apenas pelo criador ou participantes);
  - **Data de Abertura:** Registo automático da criação;
  - **Data de Início:** Preenchida automaticamente quando o estado passa a **EM EXECUÇÃO**;
  - **Data de Adjudicação:** Preenchida automaticamente quando o estado passa a **ADJUDICADO**;
  - **Data de Conclusão:** Preenchida automaticamente ao fechar o projeto ou passar a **FINALIZADO**.
- **Estados do Projeto:** PENDENTE $\rightarrow$ EM EXECUÇÃO $\rightarrow$ EM REFORMULAÇÃO $\rightarrow$ FINALIZADO $\rightarrow$ PERDIDO $\rightarrow$ ADJUDICADO.

### 14.3 Ferramenta de Desenho de Planta 2D (Wall Builder)
Disponível em Estudo de Planta e Projecto 2D para utilizadores com permissão de planta:
- Desenho vetorial no browser de paredes estruturais, divisões interiores, portas de abrir e correr, janelas e mobiliário básico.
- **Importação de Ficheiros CAD (DXF):** Permite importar plantas arquitetónicas em formato **DXF**. Ficheiros nativos do AutoCAD em formato `.dwg` têm de ser previamente guardados ou exportados como `.dxf` antes de importar.
- Permite trabalhar em ecrã completo e exportar a planta resultante como imagem de alta resolução em formato PNG.

### 14.4 Organização por Ambientes e Importação de Orçamentos Artsoft
- **Ambientes:** Estruture o projeto por divisões clicando em **Adicionar Ambiente** (ex.: "Sala de Estar", "Quarto Principal", "Cozinha").
- **Produtos:** Dentro de cada ambiente, clique em **Produto** para adicionar peças do catálogo, definindo quantidade, preço e percentagem de desconto comercial.
- **Regime de IVA:** Escolha entre **Com IVA (23%)** ou **Isento (0%)**. A barra fixa inferior recalcula instantaneamente os subtotais de incidência, imposto e montante global.
- **Importação Direta de Orçamentos Artsoft:**
  - Introduza a série e o número do orçamento comercial emitido no ERP no formato `Série/Número` (ex.: `C071/1545`).
  - Clique em **Importar Linhas**: o Floow lê as linhas do ERP e cria automaticamente um ambiente dedicado preenchido com os artigos e valores desse orçamento.

### 14.5 Regras de Anexos, Apresentação e Partilha Pública com Cliente
- *Regra Obrigatória de Segurança:* É estritamente **proibido gravar ou fechar um projeto que tenha produtos sem que exista pelo menos 1 ficheiro anexado** na secção de anexos gerais (exceto na tipologia Desenhos Técnicos).
- **Categorias de Ficheiros:**
  - **Anexos do Projeto:** Plantas, orçamentos e detalhes técnicos internos. Cada ficheiro possui um seletor **Cliente**: se estiver desmarcado, o ficheiro permanece confidencial.
  - **Anexo de Apresentação ao Cliente Final:** Zona de destaque para dossiês visuais e catálogos de apresentação da proposta.
- **Link de Visualização Pública:**
  - Ative a opção **Visualização pública** para gerar um URL encriptado de consulta sem login.
  - Copie e envie o link ao cliente: o cliente abre uma galeria interativa onde **apenas visualiza a informação e os anexos marcados com a etiqueta "Cliente"**. Ficheiros internos de custo e notas confidenciais ficam inacessíveis.

### 14.6 Fecho Financeiro do Projeto
- Para finalizar o projeto, clique no botão **Fechar Projeto** (o estado transita para FINALIZADO).
- **Validação de Confirmação:** O sistema abre uma janela de validação exigindo que o operador introduza manualmente o **valor total final** do projeto (com IVA, caso se aplique). O valor digitado tem de coincidir rigorosamente com a soma da barra inferior para que o encerramento seja aceite, evitando desvios entre orçamentos e faturação.
- Quando o projeto fica Finalizado, ativa-se o bloco especial de **Desenhos para Pedidos de Cotação** para despachar os ficheiros necessários à orçamentação técnica de carpintaria.

---

## 15. Gestão de Pós-Venda

Aceda através do menu **Pós-venda** (`/after-sales`).
Destina-se ao tratamento de reclamações, garantias, reparações de fábrica e assistência técnica a clientes após a entrega do produto.

### 15.1 Processos Provisórios vs Definitivos
- **Processos Provisórios:** Aberturas preliminares de incidência registadas em loja pelo vendedor no momento da queixa do cliente (aguarda recolha de fotos da anomalia ou transporte da peça).
- **Processos Definitivos:** Processo formalmente qualificado e admitido pelo departamento de qualidade para intervenção de assistência técnica.

### 15.2 Estados e Acompanhamento
- **Pré-Processamento:** Análise preliminar do relatório de avaria e responsabilidade.
- **Em Processamento:** Peça em trânsito ou a ser intervencionada na fábrica/estofador.
- **Terminado:** Assistência concluída, produto reparado e entregue de volta ao cliente com termo de receção.
- O painel contabiliza o valor financeiro acumulado das reparações e custos de assistência por loja e cliente.

---

## 16. Circulares Internas e Comunicados

Localizado em **Circulares** (`/circulares`).
Constitui o órgão de comunicação oficial da empresa para partilha de normas, novas regras operacionais, catálogos em vigor e alertas de gestão.

### 16.1 Leitura e Destaque
- O menu exibe um **crachá numérico vermelho** com o número de circulares publicadas que o utilizador ainda não leu.
- Ao abrir uma circular, a leitura é registada e o contador diminui.
- **Circulares Fixadas:** Comunicados de importância crítica surgem permanentemente fixados no topo da lista.
- **Filtros Laterais:** Permite navegar por: *Todas*, *Não Lidas*, *Rascunhos*, *Arquivadas* e filtrar por **Temas** coloridos (ex.: Recursos Humanos, Qualidade, Regras de Produção, Informática). O filtro **Só em vigor** exclui circulares descontinuadas.

---

## 17. Logística no Escritório (Consulta e Gestão de Stock)

Aceda através de **Logística → Consulta de stock** (`/logistics/stock`).

### 17.1 Consulta de Posições, Destinos e Histórico de Movimentos
- O painel exibe cartões superiores resumindo o número de **Linhas**, **Unidades** e **Encomendas** ativas no armazém selecionado.
- **Filtros de Pesquisa:** Código do artigo, nome, localização física na estante, número de encomenda de cliente, tipo de produto e destino do stock.
- **Destinos do Stock:**
  - `Livre`: Stock disponível em armazém que não está prometido a nenhuma ordem nem cliente.
  - `Encomenda`: Stock cativado para satisfazer uma encomenda comercial específica.
  - `Produção`: Componente ou matéria-prima alocada a uma Ordem de Fabrico.
- **Extrato Completo de Movimentos:** Clicando no código de qualquer artigo na grelha, o sistema abre o extrato detalhado de auditoria (data/hora, tipo de movimento, armazém, localização de origem/destino, quantidade e saldo resultante), exibindo até 1000 movimentos históricos.

### 17.2 Alocação e Desalocação de Stock Livre
- **Alocar Stock a Encomenda ou Ordem:**
  - Numa linha com destino `Livre`, clique no botão **Alocar**.
  - Defina a quantidade pretendida e escolha o destino:
    - *Encomenda de Cliente:* Selecione a linha da encomenda em carteira do Artsoft;
    - *Ordem de Produção:* Indique o número da ordem de fabrico.
  - O stock passa imediatamente a cativado, impedindo que outros utilizadores o utilizem.
- **Desalocar Stock:**
  - *Regra Estrita de Segurança:* Não é possível mudar stock diretamente de uma encomenda A para uma encomenda B.
  - O utilizador deve clicar na posição alocada, carregar em **Desalocar** para devolver as unidades ao estado `Livre`, e só depois executar uma nova alocação para o destino correto.

### 17.3 Mapa Visual Tridimensional do Armazém
- No lado direito do ecrã, o botão **Mapa** renderiza uma representação visual tridimensional do armazém selecionado.
- Os artigos resultantes da pesquisa ativa na grelha ficam destacados com iluminação no mapa.
- A gaveta **Fora do mapa** lista o stock existente que se encontra colocado em localizações que ainda não foram modeladas visualmente na estrutura do armazém.

---

## 18. Terminal Móvel de Logística (PWA de Armazém)

Aplicação Web Progressiva de alto desempenho concebida para telemóveis de mão, leitores PDA com leitor laser integrado e tablets de armazém. Aceda em **Logística → Terminal** (`/logistics/pwa`).
- **Instalação no Ecrã Principal:** Clique no botão **Instalar PWA**. Em dispositivos iOS (iPhone/iPad), clique no botão de partilha do Safari e selecione *"Adicionar ao ecrã principal"*.

### 18.1 Acesso por PIN e Seleção do Armazém de Trabalho
1. O operador introduz o seu **PIN numérico de logística**.
2. **Armazém de Trabalho:** O terminal pergunta ou assume o armazém predefinido. O operador pode clicar em **Alterar** no topo para alternar entre armazéns autorizados.
3. **Hub de Módulos Operacionais:** O ecrã inicial apresenta cartões para cada operação. Se um cartão estiver esbatido e inacessível, o terminal detalha o motivo por baixo (ex.: falta de permissão de grupo, falta de configuração de séries no Artsoft ou ERP offline).

### 18.2 Leitura e Descodificação de Etiquetas com Volumes
As etiquetas industriais de código de barras do Floow contêm informação enriquecida separada por barras verticais (`|`):
- `Linha|Artigo|Volume/Total` $\rightarrow$ Ex.: `F222/250000953-1|DKPAACESAAAAAADC|1/2`
  - Representa o **Volume 1 de 2** dessa unidade. O terminal regista a leitura desse volume parcelar.
- `Linha|Artigo|Total` $\rightarrow$ Ex.: `F222/250000953-1|ARTIGO|2`
  - Informa que a peça tem 2 volumes, mas não identifica qual. O terminal abre uma janela a pedir: *"Este artigo tem 2 volumes. Indique qual leu (1 ou 2)"*.
- `Linha|Artigo|0` $\rightarrow$ O zero assume que a peça é de volume único (1/1).
- **Código Simples (Apenas SKU):** Identifica o artigo sem segmentação de volumes.

> [!WARNING]
> **O último campo da etiqueta NÃO É a quantidade!**
> Numa etiqueta `...|1/2`, o `1/2` significa primeira metade da embalagem física e **não** meia unidade de stock. O Floow só consolida uma unidade física completa quando todos os volumes da linha forem lidos no destino.

### 18.3 Inventário Físico e Acertos de Stock
Módulo destinado a contagens periódicas ou gerais de armazém:
1. Aceda a **Inventário** no terminal.
2. Faça a leitura do código de barras da prateleira/local e leia os artigos ou etiquetas.
3. Se o artigo tiver múltiplos volumes, o Floow só fecha a unidade contada quando **todos os volumes daquela etiqueta forem bipados**. Se ler apenas o volume 1 de 2, a contagem não assume 1 unidade inteira.
4. Confira as quantidades lidas na grelha e clique em **Gravar Inventário**.
5. O Floow calcula as divergências face ao sistema e **lança automaticamente o documento oficial de regularização no Artsoft** utilizando a série e a entidade de acerto configuradas no escritório. O código da localização segue nas linhas do documento.

### 18.4 Receção de Mercadoria de Fornecedores
1. Aceda a **Recepção**. O terminal confirma o armazém de receção ativo.
2. Selecione a **Localização de Destino** (código da estante/baia onde a mercadoria vai ser depositada).
3. Clique em **Iniciar Recepção**.
4. Leia os artigos recebidos para o **Carrinho de Recepção**. O sistema cruza as leituras com as encomendas de compra pendentes a fornecedores.
5. Valide a conferência e confirme: o documento oficial de receção e acerto dá entrada imediata de stock no Artsoft.

### 18.5 Movimentação e Deslocalização com Carrinho de Transporte
Módulo para transferir artigos entre estantes dentro do mesmo armazém ou entre armazéns:
1. Indique a localização de origem e comece a ler os artigos a retirar da prateleira.
2. Os artigos entram no **Carrinho de Movimentação**. Se ler um volume individual (1/2), apenas esse volume específico é adicionado ao carrinho de transferência.
3. O operador desloca-se pelo armazém com o carrinho.
4. Na estante de destino, lê o **QR Code da localização de destino**.
5. Seleciona que artigos do carrinho vai depositar nessa localização e clica em **Confirmar e Lançar Transferência**.
6. O Floow lança o documento oficial de deslocalização no Artsoft e atualiza o mapa 3D. O carrinho tem de ser totalmente esvaziado ou limpo antes de iniciar uma nova recolha.

### 18.6 Consumos Internos com Saída de Stock
Módulo para registar saídas físicas de material (ex.: tintas, colas, ferramentas consumíveis, material para manutenção):
1. Aceda a **Consumos**.
2. Leia os artigos para a **Lista de Consumo**. A etiqueta identifica a referência; o operador digita a quantidade real consumida.
3. Selecione o centro de custos/motivo de consumo.
4. Clique em **Confirmar Consumo**: o Floow gera o documento oficial de saída de stock no Artsoft com o terceiro e a série de consumo interno configurados.

### 18.7 Consulta e Edição de Dados Logísticos do Artigo
- Permite ler qualquer etiqueta no armazém para inspecionar a ficha do artigo, stock em todos os armazéns, fotos e ficheiros.
- Operadores autorizados podem editar diretamente campos logísticos (ex.: número de unidades por caixa, empilhamento máximo, localização preferencial).

### 18.8 Expedição e Gestão do Mapa de Cargas
- Permite consultar em tempo real as cargas de camião e rotas de entrega planeadas no Artsoft.
- O operador valida a saída das caixas por cliente e transportadora antes do fecho da guia de transporte.

---

## 19. Estrutura de Armazéns e Localizações

Aceda através do menu **Armazéns** (`/warehouses`).
Gere a estrutura física de armazenamento da empresa: pavilhões, corredores, estantes, níveis e baias de arrumação.

- **Importar Localizações:** Lê a listagem oficial de armazéns e códigos de localização diretamente da base de dados do Artsoft ERP. O botão exibe *"A importar..."* e conclui informando o número exato de registos criados.
- **Exportar Localizações:** Descarrega a listagem completa em ficheiro Excel para auditoria física.
- **Desenho do Layout 3D:** É nesta secção que se associam as coordenadas espaciais às prateleiras para que a Consulta de Stock consiga desenhar o mapa interativo tridimensional.

---

## 20. Faturas OCR de Fornecedores

Localizado em **Faturas OCR** (`/ocr` — título *Faturas de Fornecedores*).
Sistema de ponta que utiliza modelos avançados de Inteligência Artificial para eliminar a digitação manual de faturas de compras, conferindo linhas de fatura contra encomendas e receções de armazém antes de as integrar no Artsoft.

### 20.1 Pipeline de Processamento Inteligente em 4 Fases
O painel superior exibe o funil de processamento em quatro passos:
1. **Captura:** O utilizador faz o carregamento dos documentos (ficheiros PDF de faturas originais ou digitalizações em imagem).
2. **Leitura OCR por IA:** O motor de Inteligência Artificial lê o documento em segundo plano, identificando de forma autónoma o NIF do fornecedor, número da fatura, data de emissão, taxas de IVA, valores totais e cada uma das linhas individuais de artigos (código, descrição, quantidade, preço unitário e valor tributável).
   - *Processamento Assíncrono:* O utilizador não fica preso ao ecrã. Pode fechar o browser e regressar mais tarde enquanto o motor analisa os documentos.
3. **Matching (Conferência Automática):** O Floow cruza as linhas lidas da fatura com os documentos de compra e guias de receção pendentes daquele fornecedor no Artsoft. Se os preços e quantidades baterem certo, a fatura fica **Conferida**. Se houver divergências de cêntimos ou de quantidade, segue para Quarentena.
4. **ARTSOFT (Envio Final):** Fase de exportação e criação do documento de compra definitivo na contabilidade do ERP.

### 20.2 Quarentena Inteligente e Cockpit de Reconciliação
As faturas que não obtiverem correspondência automática de $100\%$ entram em estado **Divergente (Quarentena)**:
1. Abra a fatura em quarentena para aceder ao **Cockpit de Reconciliação Visual**.
2. O ecrã apresenta uma vista dividida:
   - **Lado Esquerdo:** O documento PDF original do fornecedor, com ferramentas de zoom e navegação;
   - **Lado Direito:** As linhas lidas pelo OCR confrontadas lado a lado com as linhas de encomenda/receção pendentes no Artsoft.
3. O operador pode associar manualmente uma linha com divergência ao artigo correto do ERP, corrigir pequenas discrepâncias de arredondamento de cêntimos ou rejeitar linhas indevidas.

### 20.3 Associação de Linhas e Aprendizagem de Layout por NIF
- Ao reconciliar uma fatura, o operador pode clicar em **Guardar Layout do Fornecedor**.
- O sistema memoriza os padrões de texto e a estrutura daquele NIF específico. As próximas faturas recebidas desse fornecedor serão lidas e reconciliadas automaticamente com base nas regras aprendidas, reduzindo drasticamente o trabalho manual futuro.

### 20.4 Integração e Envio Final para o Artsoft
- Quando todas as linhas estiverem conferidas e sem erros, o botão **Enviar ARTSOFT** fica verde e disponível.
- Ao clicar, o Floow gera a fatura de compra no Artsoft e grava o número de documento devolvido pelo ERP na ficha.
- *Aviso Crítico de Controlo:* Não tente apagar ou reinserir uma fatura já marcada como *Enviada*. Se o documento já foi gravado no Artsoft, eventuais anulações contabilísticas têm de ser processadas no próprio ERP através de notas de crédito ou documentos de anulação.

---

## 21. Indicadores e Inteligência de Negócio (BI)

Localizado em **Indicadores** (`/admin/bi`).
Permite a diretores e chefias operacionais construir análises multidimensionais de dados sobre qualquer área da empresa em tabelas dinâmicas (*Pivot Tables*).

### Passos para Criar uma Análise Dinâmica
1. Clique em **Nova Análise**.
2. Selecione o **Conjunto de Dados** pretendido (ex.: *Vendas*, *Ordens de Produção*, *Tempos MES*, *Stocks*, *Assiduidade*).
3. Clique em **Campos do Pivot** (ou *Fields*):
   - Arraste dimensões para a secção de **Linhas** (ex.: *Loja*, *Comercial*);
   - Arraste dimensões para a secção de **Colunas** (ex.: *Mês*, *Ano*);
   - Arraste métricas para a secção de **Valores** (ex.: *Soma de Valor Venda*, *Média de Minutos de Fabrico*).
4. Aplique filtros condicionais de datas e estados.
5. Clique em **Guardar** e dê um título à sua análise. As análises gravadas ficam listadas no menu esquerdo em **Minhas**.
6. **Partilhar:** Pode partilhar o relatório com outros utilizadores ou grupos. Os colegas visualizam a análise na secção **Partilhadas**.
7. **Exportar:** Botão direto para descarregar a grelha resultante para ficheiro Excel.

---

## 22. Consultas Dinâmicas de Dados

Aceda através de **Consultas** (`/dynamic-queries`).
Repositório central de relatórios operacionais estruturados em consultas de base de dados estritamente de leitura (não alteram dados).

### 22.1 Executar Consultas
- Na listagem de consultas autorizadas para o seu perfil, clique em **Executar**.
- **Perguntas Interativas:** Se a consulta tiver sido desenhada com filtros dinâmicos, o sistema abre uma janela prévia solicitando os parâmetros de pesquisa (ex.: *"Data Inicial"*, *"Data Final"*, *"Escolha o Armazém"*, *"NIF do Cliente"*).
- Clique em **Ver Resultados**: a grelha apresenta os dados paginados com totalizadores.
- Clique em **Excel** para descarregar o relatório integral.

### 22.2 Criação e Partilha de Consultas (Utilizadores Avançados)
- Utilizadores com permissão de criação podem clicar em **Nova Consulta**.
- Podem redigir consultas em linguagem de interrogação ou recorrer ao **Assistente de IA integrado** para traduzir uma pergunta em linguagem natural para uma consulta estruturada.
- O sistema valida a consulta contra um dicionário rigoroso de tabelas autorizadas para garantir a privacidade e segurança do sistema.
- Pode restringir quem pode correr a consulta (por utilizador ou grupo) e gerar links temporários protegidos por chave de segurança para auditoria externa.

---

## 23. Módulos Complementares e Setoriais

Estes módulos só aparecem no menu caso estejam contratados e ativados nas definições da sua instalação:

### 23.1 AutoLog — Gestão de Frotas e Oficina
Módulo completo de apoio a oficinas mecânicas internas e parques de viaturas corporativas:
- **Painel:** Resumo do estado da frota, inspeções periódicas obrigatórias a caducar, seguros e viaturas paradas em oficina.
- **Viaturas:** Cadastro de matrículas, marca, modelo, quilometragem atualizada, condutor habitual e histórico de intervenções.
- **Peças:** Catálogo de consumíveis mecânicos (filtros, pneus, óleos) e stock de oficina.
- **Reparações / Serviços:** Registo de folhas de obra mecânica com alocação de mecânico responsável, horas de mão-de-obra e peças consumidas.

### 23.2 FSPS e Logística Praddy
- Módulos setoriais de verificação rápida e conferência documental por leitura laser de QR Code para expedição rápida de mobiliário e controlo de expedição em parceiros do grupo.

### 23.3 Assistentes de Inteligência Artificial e Conectores MCP
- **Chat MCP (Assistente Floow):** Chat de inteligência artificial embebido na barra lateral da aplicação. Permite aos utilizadores fazer perguntas em linguagem natural sobre ordens de fabrico, stocks e clientes, respondendo de forma segura respeitando escrupulosamente as permissões de acesso do utilizador autenticado.
- **MCP Server (Claude / ChatGPT):** Interface de conetividade moderna que permite ligar o ecossistema Floow diretamente ao Anthropic Claude Desktop ou OpenAI ChatGPT empresarial através do protocolo Model Context Protocol (MCP), viabilizando consultas executivas e automatizações avançadas.

---

## 24. Administração do Sistema, Permissões e Sincronização

Acesso reservado a administradores do sistema em **Configurações**.

### 24.1 Matriz de Grupos e Permissões
Localizado em **Configurações → Grupos**:
- No Floow, a segurança baseia-se em perfis de grupo (ex.: *Comercial Loja*, *Encarregado Produção*, *Engenharia*, *Operador Logística*, *Direção Financeira*).
- Cada grupo contém centenas de permissões granulares: acesso a menus, permissão de criar, editar, aprovar viabilidade técnica, atribuir preço, forçar alterações de estado, exportar para Excel ou gerir configurações.
- *Dica de Suporte:* Se um colaborador reportar que não vê determinado menu ou que um botão está desativado, o administrador deve aceder à ficha do grupo dessa pessoa e verificar se a respetiva permissão está assinalada.

### 24.2 Sincronização Periódica com o Artsoft ERP
Localizado em **Configurações → Sincronização**:
- Apresenta o painel de controlo de todas as rotinas automatizadas que sincronizam dados em segundo plano entre o Floow e o Artsoft (clientes, fornecedores, artigos, saldos de stock, encomendas e documentos).
- **Forçar Execução:** Permite disparar manualmente qualquer rotina em segundo plano.
- **Depuração de Erros:** Se uma sincronização falhar (ex.: quebra de rede com o servidor Artsoft), o log detalha o pacote de dados enviado e a resposta de erro devolvida pelo ERP.

### 24.3 Gestão de Limites de Compras
Localizado em `/purchase-limits`:
- Permite configurar limites orçamentais máximos mensais de aprovação de compras por departamento ou comprador, bloqueando desvios orçamentais sem autorização da administração.

---

## 25. O que o Floow NÃO Faz Sozinho (Regras Críticas e Limitações)

Para evitar erros operacionais e expectativas incorretas, todo o utilizador deve conhecer estes princípios inegociáveis do sistema:

1. **O Floow não substitui a contabilidade do Artsoft:** Faturação legal, fecho de contas, declarações fiscais e controlo oficial de crédito bancário vivem exclusivamente no ERP.
2. **Um Pedido de Cotação (CDP) não gera encomenda comercial por si só:** O CDP é uma ferramenta de cálculo técnico e orçamentação. A única exceção é a criação do documento **C971** de retificação de medidas. A adjudicação de um CDP não cria a fatura de venda no Artsoft; o comercial deve registar o orçamento normal no ERP.
3. **Adjudicar no Aprovisionamento é um ato confidencial:** Adjudicar um fornecedor no Procurement não lhe envia nenhum email automático nem fecha a sua proposta no portal. A comunicação final com o fornecedor é feita pela equipa de compras.
4. **A baixa de material no Planeamento não altera o stock de armazém:** O registo de consumo numa ordem no calendário Gantt ajusta os cálculos de rentabilidade teórica; quem movimenta stock físico é a picagem no MES ou os documentos de consumo da Logística.
5. **Suspender o tablet do MES não suspende a contagem de tempo:** Apagar o ecrã do tablet deixa o relógio a contar. Para parar o tempo de mão-de-obra, o operário tem de carregar formalmente no botão **Suspender** ou **Terminar**.
6. **Não é possível transferir stock alocado entre encomendas de forma direta:** O stock alocado à encomenda A tem obrigatoriamente de ser desalocado para o estado Livre antes de poder ser alocado à encomenda B.
7. **O último número da etiqueta de stock não é quantidade:** Num código `...|1/2`, o `1/2` é o número da embalagem e não a quantidade.
8. **Inventário parcelar não conta unidades inteiras:** No inventário físico, ler apenas o volume 1 de 2 de um artigo deixa a contagem dessa unidade pendente até ser lido o volume 2 de 2.
9. **Eliminar um anexo de um artigo não apaga o histórico:** Desenhos técnicos e anexos apagados das fichas permanecem gravados nos arquivos de auditoria em Atividade para segurança de engenharia.
10. **A simulação da BOM paramétrica não altera linhas na base de dados:** Testar variáveis ou alterar medidas na ferramenta paramétrica gera cálculos em memória. Nada afeta as ordens de fabrico reais até que seja gerado um snapshot definitivo.

---

## 26. Guia de Resolução de Problemas (Troubleshooting)

### 1. Um menu ou botão desapareceu ou não consigo aceder
- **Causa:** O seu utilizador não possui a permissão de grupo necessária, ou o módulo está desativado na empresa.
- **Solução:** Peça a um administrador para rever o seu grupo em **Configurações → Grupos**. Depois de receber a permissão, faça **Logout** e volte a entrar para refrescar a sessão.

### 2. O código de login por email (2FA) não chega
- **Causa:** Filtros de spam corporativos ou email incorreto.
- **Solução:** Verifique a pasta de Spam/Lixo Eletrónico. Confirme junto do administrador se o endereço de email na sua ficha está correto. Aguarde 2 minutos antes de solicitar novo código.

### 3. O Terminal MES diz: *"Lançamento sem ordem de fabrico libertada"*
- **Causa:** O setor fabril exige ordem formal e o planeamento de produção ainda não libertou a ordem de fabrico no escritório.
- **Solução:** O responsável de planeamento deve aceder a **Produção → Ordens de Produção** e mudar o estado da ordem para "Libertada".

### 4. O Terminal MES bloqueia com a mensagem `LAG_TIME_ACTIVE`
- **Causa:** A operação anterior tem um tempo de secagem ou espera que ainda não terminou.
- **Solução:** Aguarde o término do contador exibido no ecrã. Se houver autorização excecional, chame o supervisor de turno para aplicar o seu PIN de bypass.

### 5. O documento de entrada de stock do MES não foi criado no Artsoft
- **Causa:** Falta de stock de alguma matéria-prima no armazém de saída do Artsoft, ou o posto não tem armazém associado.
- **Solução:** Não volte a picar a ordem no tablet. Verifique a mensagem de erro no backoffice em **Produção → MES → Picagens**. Corrija o saldo da matéria-prima no Artsoft e processe o documento na fila de retentativas.

### 6. No Terminal de Logística, um cartão de operação está cinzento/esbatido
- **Causa:** O operador não tem permissão para essa operação, ou o escritório não configurou as séries de documentos Artsoft para esse armazém.
- **Solução:** O gestor de logística deve aceder a **Logística → Configurações** no computador e verificar se as séries de inventário, receção, consumo ou deslocalização estão devidamente preenchidas.

### 7. O ficheiro da fatura OCR não avança na leitura
- **Causa:** O ficheiro PDF tem proteção contra leitura, texto ilegível ou o serviço de IA está com fila extensa.
- **Solução:** Aguarde alguns minutos. Se persistir em erro, aceda à ficha da fatura para inspecionar a mensagem do motor e verifique se o documento pode ser visualizado no Cockpit de Reconciliação.

---

## 27. Glossário Geral de Conceitos

- **Artsoft:** Sistema ERP oficial da empresa que gere finanças, faturação, compras e stocks legais.
- **Artigo Base (Pai):** Ficha modelo mestre de engenharia. Não se vende diretamente; gera artigos filhos.
- **Artigo Filho (Variante):** Referência acabada vendável (SKU) associada a uma combinação concreta de atributos.
- **Atributo:** Característica configurável de um produto (ex.: Tecido, Acabamento, Pés).
- **Mini-BOM:** Lista parcial de materiais e tempos associada exclusivamente a um determinado valor de atributo.
- **Combinação de Mini-BOM:** Regra especial onde a escolha simultânea de dois atributos substitui as suas Mini-BOMs individuais por uma estrutura dedicada.
- **BOM (Bill of Materials):** Lista técnica de fabrico contendo todas as operações, tempos, matérias-primas e componentes de um produto.
- **BOM Paramétrica:** Camada de regras matemáticas e lógicas para cálculo dinâmico de materiais e medidas sem duplicar fichas.
- **Snapshot de BOM:** Versão fechada, estática e imutável de uma lista de materiais gerada para uma ordem de fabrico específica.
- **MES (Manufacturing Execution System):** Sistema e terminal móvel de chão de fábrica para picagem de tempos de operários e controlo de postos.
- **Posto de Trabalho:** Local físico ou máquina onde decorre uma operação fabril (ex.: Tupia, Banco de Estofo, Cabine de Pintura).
- **Lag Time:** Tempo de espera ou cura obrigatório entre duas operações consecutivas de fabrico.
- **C971:** Tipo de documento emitido automaticamente no Artsoft para formalizar o serviço de retificação de medidas de um pedido CDP.
- **CDP (Cotação e Desenvolvimento de Produto):** Circuito comercial interno para aprovação e orçamentação de peças à medida.
- **Procurement (Aprovisionamento):** Processo de consulta ao mercado externo e pedido de cotações a fornecedores (RFQ).
- **Wall Builder:** Ferramenta gráfica do Floow para desenho vetorial de plantas de arquitetura 2D e posicionamento de divisões e móveis.
- **DXF:** Formato universal de ficheiro de desenho vetorial CAD importável pelo Wall Builder.
- **PWA (Progressive Web App):** Aplicação web avançada capaz de ser instalada em dispositivos móveis funcionando como uma app nativa com alta velocidade.
- **Stock Livre:** Mercadoria armazenada em armazém que se encontra perfeitamente desimpedida de reservas comerciais ou de fabrico.
- **Alocar:** Ato de bloquear uma quantidade de stock livre associando-a a uma encomenda de cliente ou a uma ordem de produção.
- **Desalocar:** Libertar stock previamente cativado, devolvendo-o ao estado de livre.
- **Volume:** Embalagem ou fardo físico parcial de um artigo de grandes dimensões (ex.: Volume 1/2 e Volume 2/2).
- **Quarentena OCR:** Área de retenção de faturas onde o sistema detetou divergências entre a fatura do fornecedor e a encomenda do ERP para validação humana.
- **Pivot (Tabela Dinâmica):** Ferramenta analítica do módulo de BI para cruzamento dinâmico de dimensões e métricas de negócio.

---

## 28. Percursos Rápidos Operacionais ("Como Faço Para...")

Consulte este guia rápido para responder a questões operacionais do dia a dia:

### Como começo o meu dia de trabalho no escritório?
1. Faça login no Floow e introduza o código de verificação recebido no email.
2. No cabeçalho superior, clique em **Registar Ponto** para abrir o seu turno de assiduidade.
3. Consulte a bandeja **Para Mim Hoje** para ver tarefas urgentes pendentes sob a sua responsabilidade.
4. Consulte o sino de notificações e o bloco de **Tarefas Pessoais** no Painel Principal.

### Como crio novas variantes de um modelo de mobiliário?
1. Se necessário, crie os novos atributos ou valores em **Configurações → MRP**.
2. Abra a ficha do artigo base em **Artigos → Lista**, aceda ao separador **Atributos** e associe os valores permitidos e respetivas **Mini-BOMs**.
3. Aceda a **Artigos → Wizard**, selecione a base e assinale as opções pretendidas.
4. Se o total for até 30 variantes, confirme no ecrã. Se for superior (até 500), confirme o envio por email e aguarde a notificação de conclusão.

### Como orçimento uma peça especial à medida para um cliente?
1. Aceda a **Pedidos de cotação → Novo pedido**, selecione a loja, cliente, introduza a descrição e anexe desenhos ou fotografias de referência.
2. Adicione colegas em **Notificar no preço** caso pretenda partilha de gestão. Guarde o pedido.
3. A engenharia técnica analisa o pedido e clica em **Confirmar Viabilidade** (ou devolve para correção caso necessite de alterações de desenho).
4. A equipa de cotação introduz o **Preço A** e o **Preço B** (com justificação obrigatória).
5. Quando o cliente aceitar a proposta, clique em **Adjudicado**.

### Como marco e executo uma medição no cliente após adjudicação?
1. No artigo CDP adjudicado, abra o bloco de **Retificação de Medidas**, selecione obrigatoriamente o técnico de medições e grave. (O sistema cria o documento **C971** no Artsoft).
2. O técnico abre a aplicação móvel no tablet em `/cdp/app`, consulta a agenda e desloca-se à obra.
3. No local, tira fotografias da divisão, dita as medidas para o campo de notas e clica em **Fechar Retificação**. O designer do projeto recebe um email para avançar com o desenho final.

### Como peço preços de materiais a fornecedores externos?
1. No módulo de compras, aceda a **Aprovisionamento → Novo pedido** (ou clique em **Gerar Aprovisionamento** na ficha de um pedido CDP).
2. Adicione as linhas de artigos e associe os fornecedores pretendidos (certifique-se de que os fornecedores têm *Email Procurement* na ficha).
3. Clique em **Enviar Pedido**.
4. Cada fornecedor recebe um convite por email e regista a sua proposta diretamente no portal seguro `/fornecedor`.
5. No Floow, compare as propostas e clique em **Adjudicar** na melhor oferta (a decisão permanece em sigilo interno).

### Como crio e partilho um projeto de decoração com um cliente?
1. Aceda a **Projetos → Novo**, atribua um nome, cliente e selecione a tipologia (ex.: *Projecto 2D*).
2. Use o **Wall Builder** para desenhar a planta ou importe um ficheiro **DXF**.
3. Crie ambientes (*Sala*, *Quarto*) e insira produtos ou importe linhas de orçamentos Artsoft (`Série/Número`).
4. Anexe os ficheiros de apresentação e marque com a opção **Cliente** apenas os ficheiros autorizados para visualização externa.
5. Ative a **Visualização pública**, copie o link seguro e envie-o ao cliente.
6. Para finalizar o projeto, clique em **Fechar Projeto** e confirme o valor total financeiro.

### Como pico uma ordem de fabrico no chão de fábrica?
1. No tablet do setor, digite o seu **PIN de Operador** ou aponte o seu crachá QR Code.
2. Selecione o posto ou operação e aponte o leitor de código de barras para a folha de obra.
3. A tarefa transita para o estado *Em Curso*.
4. Se precisar de fazer uma pausa, clique obrigatoriamente em **Suspender** (não basta desligar o ecrã).
5. Ao concluir o fabrico das peças, clique em **Concluir**. Se o sistema abrir o questionário de embalamento, introduza o número de caixas, medidas e peso. O sistema lança a entrada de produto acabado no Artsoft.

### Como reservo stock existente em armazém para um cliente?
1. Aceda a **Logística → Consulta de stock**, pesquise pelo artigo pretendido e localize uma linha com destino **Livre**.
2. Clique no botão **Alocar**.
3. Digite a quantidade a cativar, selecione **Encomenda de cliente** e escolha a linha da encomenda pretendida.
4. Para libertar a reserva, clique na posição e selecione **Desalocar**.

### Como faço a contagem física de um armazém pelo telemóvel?
1. Aceda ao Terminal Móvel de Logística (`/logistics/pwa`) e introduza o seu PIN.
2. Selecione o armazém de trabalho e abra o módulo **Inventário**.
3. Leia o código da localização e leia as etiquetas das caixas. Se o artigo tiver múltiplos volumes (ex.: 1/2 e 2/2), certifique-se de ler ambos os volumes para consolidar a unidade física.
4. Confira as quantidades e clique em **Gravar Inventário**: o Floow emite automaticamente o documento de regularização de stock no ERP Artsoft.

### Como processo uma fatura de compras com inteligência artificial?
1. Aceda a **Faturas OCR** (`/ocr`) e carregue os ficheiros PDF das faturas recebidas dos fornecedores.
2. O sistema executa a leitura OCR por IA e tenta reconciliar as linhas com as ordens de compra pendentes no Artsoft.
3. Se a fatura entrar em Quarentena com divergências, abra o **Cockpit de Reconciliação**, confira o PDF lado a lado com as linhas do ERP, corrija eventuais associações de artigos e clique em **Guardar Layout**.
4. Quando tudo estiver conferido, clique em **Enviar ARTSOFT** para criar o documento de compra oficial no ERP.
