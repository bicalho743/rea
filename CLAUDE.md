@AGENTS.md

# Projeto do Solano neste repositório (fork público do REA)

Trabalho no PC: ver bicalho743/meu-enxoval-em-dia/docs/CLAUDE-NO-PC.md

**Atenção: este repositório é PÚBLICO.** Não suba prints, e-mails, saldos de
conta nem nada pessoal.

## O que é

- **Não é um app de loja.** É uma cópia do REA (ferramenta de engenharia reversa,
  servidor MCP em Node/TypeScript) usada para analisar o app "Viral" e montar o
  **Setor de Modelagem**: um agente no OpenBot que cria influencers sintéticos
  (rosto, voz, roteiro, vídeo e postagem).
- Sem bundle/package, App Store Connect, Codemagic, Expo, RevenueCat, Supabase
  ou Render. Não há build nem envio para lojas.
- Serviços usados (todos pelos conectores do claude.ai, mesma conta):
  **Kairogen** (imagens e voz; plano Essential, sem vídeo), **Viral**
  (viral.doti.gg, vídeo com lipsync; plano Starter), **UploadPost** (postagem).

## Onde está cada coisa

- `setor-de-modelagem/analise-viral.md`: o que descobrimos sobre o Viral e os custos.
- `setor-de-modelagem/agente-openbot.md`: instruções para colar no Bot do OpenBot.
- `setor-de-modelagem/clara-organiza/ficha.md`: ficha, voz e bíblia de imagens.
- `setor-de-modelagem/clara-organiza/imagens/`: os 5 ângulos e os rostos não
  escolhidos (prévias; originais no CDN do Kairogen, links na ficha).
- `setor-de-modelagem/ferramentas/`: scripts usados na análise do APK.
- Para rodar o REA: `npm ci` e `npm run build:cached` (Node 22, ver `.nvmrc`).

## Onde paramos (26/11/2026)

- **Pronto:** análise do Viral; agente Setor de Modelagem escrito; Clara Organiza
  com ficha, rosto (Rosto 2), bíblia de 5 ângulos no closet e voz
  **Juliana Katrein** (Kairogen `ZExzO7iCJWL0gUN2WYbU`). Gasto no Kairogen: 28 créditos.
- **No Viral:** existe a influencer "Clara" (id 3092, @clara-mae), criada pelo
  chat do Viral, ainda sem rosto e sem voz. Os outros perfis: Cláudia Ordem (3072,
  bio com uma regra de educação física colada por engano) e Cris Arruma (3073, rascunho).
- **Próximo passo (aguardando o "pode"):**
  1. colocar o Rosto 2 como foto da Clara 3092 no Viral, pelo link público (grátis);
  2. escolher no Viral uma voz parecida com a Juliana (busca grátis);
  3. escrever o 1º roteiro (30–40 s) para aprovação;
  4. gerar o 1º vídeo no Viral, modo `normal`, com custo cotado antes.
- **Decisões pendentes:** renomear a 3092 para Clara Organiza / @clara.organiza
  no site do Viral (o MCP não renomeia); o que fazer com a Cláudia e a Cris;
  colar o agente no OpenBot e liberar os MCPs Kairogen, Viral e UploadPost.
- Branch de trabalho: `ccr-0c31094b-p2ey9m` (não foi para a `main`).
