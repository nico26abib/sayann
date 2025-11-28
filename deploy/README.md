# 🚢 Déploiement

Fichiers de configuration pour déployer Sayann en production.

## Railway (le plus simple)

```bash
railway login
railway init
railway up
```

Variables d'env à configurer:
- `DISCORD_TOKEN`
- `OPENAI_API_KEY`

## Docker

```bash
docker-compose up -d
```

Ou avec le fichier spécifique:
```bash
docker-compose -f deploy/docker-compose.yml up -d
```

## Render

1. New Web Service
2. Connect repo
3. Build: `pip install -r requirements.txt && playwright install chromium`
4. Start: `python bot.py`
5. Add env vars: `DISCORD_TOKEN`, `OPENAI_API_KEY`

## Fly.io

```bash
fly launch
fly secrets set DISCORD_TOKEN=xxx OPENAI_API_KEY=xxx
fly deploy
```

## Fichiers

- `Dockerfile` - Image Docker
- `docker-compose.yml` - Compose multi-services
- `railway.json` - Config Railway
- `fly.toml` - Config Fly.io
- `Procfile` - Config Render/Heroku

