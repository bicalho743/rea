# Análise do app "Viral" (viral.doti.gg) — resumo

Feita em 23 e 24/11/2026 com o REA nesta cópia do repositório.

## O APK

- É um **WebAPK** do Chrome (assinado por "Google / WebAPK" e "Chrome WebAPK CA"),
  com 125 KB e nenhum código próprio. Só abre `https://viral.doti.gg/m`.
- O produto é o site **viral · studio** (DOTI Tecnologia): "crie influencers
  sintéticos que postam sozinhos". Next.js atrás da Cloudflare, login com Auth.js,
  PostHog e Sentry, checkout pela Hubla.

## Como o Viral funciona (pelas ferramentas do MCP deles)

1. `create_influencer` (rascunho) → `set_influencer_appearance` (3 rostos por IA
   ou foto) → `choose_influencer_face` (gera 5 ângulos) → `set_influencer_voice`
   / `choose_influencer_voice` (vozes de catálogo; o campo `generated_voice_id`
   indica ElevenLabs).
2. Vídeo = imagem (`fi_`) + áudio (`fa_`) → vídeo falando com lipsync (`th_`);
   modo `fast` (~2 min) ou `normal` (~20 min, mais barato); controles de gesto e
   movimento.
3. Roteiro: o Viral **não escreve**; entrega contexto (`get_roteiro_context`) com
   uma base de conhecimento de vídeo curto (gancho por contraste, valor rápido,
   "mas/por isso", nome para o método, chamada para ação). Quem escreve é a IA
   que chama.
4. Postagem automática existe, mas não aparece no plano Starter.

## Custos observados

|                   | Viral Starter (R$ 49,90 / 1.000 cr)                                 | Kairogen Essential (R$ 49 / 280 cr)                             |
| ----------------- | ------------------------------------------------------------------- | --------------------------------------------------------------- |
| Imagem            | 23 cr ≈ R$ 1,15                                                     | 3–4 cr ≈ R$ 0,58                                                |
| Voz ~30 s         | por caractere                                                       | 1–2 cr                                                          |
| Vídeo com lipsync | sim (~R$ 10/min pela regra do plano)                                | **não** (vídeo só do plano Pro, R$ 149, "modelos selecionados") |
| Criar rostos      | cobrou 69 cr por 3 rostos (a isenção "antes do 1º vídeo" não valeu) | 11 cr por 3 rostos                                              |

## Decisão

- Imagens e voz no **Kairogen**; vídeo com boca sincronizada no **Viral**
  (modo `normal`); roteiro escrito pelo agente (grátis); postagem pelo UploadPost.
- O agente que orquestra tudo é o **Setor de Modelagem** no OpenBot
  (`agente-openbot.md`).
