# Architecture

```
sayann/
├── bot.py                    # Point d'entrée Discord
├── config.py                 # Configuration centralisée
├── agents/
│   ├── __init__.py
│   └── web_agent.py         # Agent principal (OpenAI + function calling)
├── tools/
│   ├── __init__.py
│   ├── browser.py           # Navigation web (Playwright)
│   └── voice.py             # Transcription (Whisper)
└── .env                     # Secrets (gitignored)
```

## Flow

```
User (Discord) 
    ↓
bot.py (Discord handler)
    ↓
web_agent.py (OpenAI function calling)
    ↓
tools/ (browser, voice, ...)
    ↓
Web / APIs
    ↓
Response → Discord
```

## Détails techniques

### bot.py
- Gère les événements Discord (`on_message`, `on_ready`)
- Routing: DM, mentions, commandes
- Transcription vocale automatique
- Gestion des réponses longues (chunking)

### agents/web_agent.py
- Interface avec OpenAI GPT-4o
- Function calling natif
- Exécution dynamique des tools
- Gestion du contexte conversationnel

### tools/browser.py
- Playwright headless
- 2 fonctions:
  - `search_and_extract()`: Google search
  - `navigate_to()`: Visite URL spécifique
- BeautifulSoup pour extraction

### tools/voice.py
- Télécharge attachments Discord
- Transcription via Whisper API
- Support multi-langues

### config.py
- Variables d'environnement centralisées
- Defaults intelligents
- Facile à override via .env

## Ajout de fonctionnalités

1. **Nouveau tool** → `tools/mon_tool.py`
2. **Enregistrer** → `agents/web_agent.py:self.tools`
3. **Exécuter** → `agents/web_agent.py:execute_tool()`

## Scalabilité

- Playwright = pool de navigateurs
- OpenAI = rate limits gérés côté API
- Discord = asyncio natif (milliers de users)
- Déploiement = Docker (horizontal scaling)

## Sécurité

- Tokens en `.env` (gitignore)
- Sandbox Playwright (headless)
- Rate limiting possible (voir `SCALING.md`)
- Pas d'exécution de code arbitraire

