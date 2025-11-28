# Web Agent Discord Bot

Agent Discord autonome qui va chercher des infos sur le web en temps réel.

## Setup rapide

```bash
./setup.sh
```

Ou manuellement:

```bash
pip install -r requirements.txt
playwright install chromium

# Créer .env avec:
# DISCORD_TOKEN=ton_token_discord
# OPENAI_API_KEY=ta_clé_openai
```

## Créer le bot Discord

1. https://discord.com/developers/applications
2. New Application → Bot
3. Copie le TOKEN
4. Bot Permissions: `Send Messages`, `Read Messages`, `Read Message History`
5. OAuth2 → URL Generator → `bot` + permissions → Invite

## Lancer

```bash
python bot.py
```

## Usage

**DM ou mention:**
```
@bot Va me chercher le S&P 500 actuel sur Bloomberg
→ S&P 500 = 5 873,42 (+0,87% aujourd'hui) – source Bloomberg 28 nov 2025 18h42

@bot Donne-moi la météo à Paris demain
→ Paris demain: 12°C, partiellement nuageux, 40% de pluie – Météo France

@bot Prix du Bitcoin en ce moment
→ Bitcoin: $43,256 (-2.3% sur 24h) – CoinGecko 18:45
```

**Commande:**
```
!search cours EUR/USD aujourd'hui
```

**Vocal:**
```
🎤 Envoie un message vocal → Il transcrit → Répond
@bot Prix Bitcoin en vocal → Il répond en audio 🔊
```

Le bot répond en 15-25 secondes avec l'info + source.

## Deploy prod

### Railway (gratuit)
```bash
railway login
railway init
railway up
```
Variables env: `DISCORD_TOKEN`, `OPENAI_API_KEY`

### Render (gratuit)
1. New → Web Service
2. Connect repo
3. Build: `pip install -r requirements.txt && playwright install chromium`
4. Start: `python bot.py`
5. Environment → Add `DISCORD_TOKEN` + `OPENAI_API_KEY`

### Fly.io
```bash
fly launch
fly secrets set DISCORD_TOKEN=xxx OPENAI_API_KEY=xxx
fly deploy
```

## Stack

- **Discord.py** → Interface texte/vocal
- **OpenAI GPT-4o** → Cerveau + function calling natif
- **Playwright** → Navigation web headless réelle
- **BeautifulSoup** → Extraction contenu

## Architecture

```
bot.py              → Point d'entrée Discord
agents/web_agent.py → Logique OpenAI + tools
tools/browser.py    → Navigation Playwright
```

Scalable → Ajoute tools dans `tools/`, enregistre dans `web_agent.py`

