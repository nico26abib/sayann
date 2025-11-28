# 📁 Structure du Projet

```
sayann/
│
├── 🚀 FICHIERS PRINCIPAUX
│   ├── bot.py                  # Point d'entrée - Lance le bot Discord
│   ├── config.py               # Configuration (tokens, settings)
│   ├── requirements.txt        # Dépendances Python
│   ├── .env                    # Secrets (TOKEN, API_KEY) - À créer
│   └── README.md               # Ce fichier
│
├── 🧠 CODE SOURCE
│   ├── agents/
│   │   └── web_agent.py        # Logique OpenAI + function calling
│   │
│   ├── tools/
│   │   ├── browser.py          # Navigation web (Playwright)
│   │   └── voice.py            # Transcription vocale (Whisper)
│   │
│   └── utils/
│       └── logger.py           # Système de logs
│
├── 🧪 TESTS & DEBUG
│   └── tests/
│       ├── README.md           # Guide des tests
│       ├── check_env.py        # Vérifie les tokens
│       ├── test_browser_visual.py    # 👁️  Navigateur VISIBLE pour debug
│       ├── test_direct_api.py  # Test OpenAI seul
│       ├── test_agent.py       # Test complet
│       └── test_search.py      # Test scraping rapide
│
├── 📚 DOCUMENTATION
│   └── docs/
│       ├── START_HERE.md       # 👈 COMMENCE ICI
│       ├── QUICKSTART.md       # Setup détaillé
│       ├── DISCORD_SETUP.md    # Config Discord (intents, etc.)
│       ├── TROUBLESHOOTING.md  # Solutions aux problèmes
│       ├── ARCHITECTURE.md     # Comment ça marche
│       ├── SCALING.md          # Ajouter des features
│       ├── IDENTITY.md         # Personnalité du bot
│       └── PROJECT_SUMMARY.md  # Vue d'ensemble
│
├── 📜 SCRIPTS
│   └── scripts/
│       ├── README.md           # Documentation scripts
│       ├── setup.sh            # Installation complète
│       └── restart_bot.sh      # Redémarrer le bot
│
├── 🚢 DÉPLOIEMENT
│   └── deploy/
│       ├── README.md           # Guide déploiement
│       ├── Dockerfile          # Image Docker
│       ├── docker-compose.yml  # Compose multi-services
│       ├── railway.json        # Config Railway
│       ├── fly.toml            # Config Fly.io
│       └── Procfile            # Config Render/Heroku
│
└── 📊 LOGS
    └── logs/
        └── bot.log             # Logs du bot (auto-généré)
```

---

## 🎯 Workflow Rapide

### Premier lancement
```bash
1. ./scripts/setup.sh          # Install tout
2. cp .env.example .env        # Crée .env
3. # Édite .env avec tes tokens
4. python bot.py               # Lance le bot
```

### Debug
```bash
# Vérifie la config
python tests/check_env.py

# Test avec navigateur visible
python tests/test_browser_visual.py

# Logs en temps réel
tail -f logs/bot.log
```

### Développement
```bash
# Modifie le code
nano agents/web_agent.py

# Relance le bot
./scripts/restart_bot.sh
```

### Déploiement
```bash
# Railway (le plus simple)
railway login && railway init && railway up

# Docker
docker-compose -f deploy/docker-compose.yml up -d
```

---

## 📖 Par où commencer?

1. **Installation** → `docs/START_HERE.md`
2. **Problème?** → `docs/TROUBLESHOOTING.md`
3. **Comprendre** → `docs/ARCHITECTURE.md`
4. **Étendre** → `docs/SCALING.md`

---

## 🔑 Fichiers importants

| Fichier | Description |
|---------|-------------|
| `bot.py` | Lance le bot Discord |
| `config.py` | Toute la configuration |
| `.env` | Secrets (tokens) |
| `agents/web_agent.py` | Cerveau du bot |
| `tools/browser.py` | Scraping web |
| `tests/test_browser_visual.py` | Debug visuel |
| `logs/bot.log` | Logs détaillés |

---

## ⚡ Commandes Rapides

```bash
# Installer
./scripts/setup.sh

# Tester
python tests/check_env.py

# Lancer
python bot.py

# Debug
python tests/test_browser_visual.py

# Déployer
railway up
```

