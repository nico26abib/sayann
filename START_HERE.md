# 👋 Commence ici

## 🎯 Objectif

Bot Discord qui va chercher n'importe quelle info sur le web et te répond.

Exemple:
```
Toi: @bot Va me chercher le S&P 500 actuel
Bot: S&P 500 = 5 873,42 (+0,87%) – Bloomberg 28 nov 18h42
```

---

## ⚡ Installation (2 minutes)

### 1. Clone/Download
Tu as déjà le code ✅

### 2. Install
```bash
./setup.sh
```

Ou manuellement:
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Config

Crée `.env`:
```bash
DISCORD_TOKEN=ton_token_discord_ici
OPENAI_API_KEY=ta_clé_openai_ici
```

**Où trouver les tokens?**

**Discord:**
1. https://discord.com/developers/applications
2. New Application
3. Bot → Reset Token → Copy
4. OAuth2 → URL Generator → `bot` + permissions
5. Copy URL et invite le bot sur ton serveur

**OpenAI:**
1. https://platform.openai.com/api-keys
2. Create new secret key
3. Copy

### 4. Check
```bash
python check_env.py
```

Si tout est ✅ → Continue

### 5. Run
```bash
python bot.py
```

Tu devrais voir:
```
✓ TonBot ready
```

---

## 🎮 Utilisation

### Texte
```
@TonBot Va me chercher le prix du Bitcoin
@TonBot Météo Paris demain
@TonBot Cours EUR/USD
```

Ou en DM directement:
```
Prix du Bitcoin
```

### Vocal
Envoie un message vocal → Il transcrit → Il répond

### Commande
```
!search cours EUR/USD
```

---

## 📊 Check les logs
```bash
tail -f logs/bot.log
```

---

## 🚀 Deploy en prod

### Railway (le plus simple)
```bash
railway login
railway init
railway up
```
Ajoute `DISCORD_TOKEN` et `OPENAI_API_KEY` dans les variables d'env.

### Docker
```bash
docker-compose up -d
```

### Render
1. New Web Service
2. Connect ton repo
3. Add env vars
4. Deploy

---

## 📚 Plus d'infos

- **README.md** → Guide complet
- **QUICKSTART.md** → Démarrage détaillé
- **ARCHITECTURE.md** → Comment ça marche
- **SCALING.md** → Ajouter des features
- **PROJECT_SUMMARY.md** → Vue d'ensemble

---

## 🆘 Problèmes?

**Bot ne répond pas:**
- Check que tu l'as mentionné: `@BotName`
- Ou envoie en DM
- Check les logs: `logs/bot.log`

**Erreur API:**
- Vérifie `.env`
- Check ton crédit OpenAI
- Check token Discord valide

**Erreur Playwright:**
```bash
playwright install chromium
```

---

## ✅ Checklist

- [ ] `./setup.sh` executé
- [ ] `.env` créé avec vrais tokens
- [ ] `python check_env.py` → tout ✅
- [ ] `python bot.py` → bot ready
- [ ] Bot invité sur ton serveur Discord
- [ ] Test: `@bot Prix Bitcoin`

Si tout est ✅ → **Tu es prêt!** 🎉

---

## 🎯 Next

1. Test quelques requêtes
2. Check les logs pour voir ce qui se passe
3. Déploie en prod (Railway recommandé)
4. Ajoute des features (voir SCALING.md)
5. Personnalise (change le prompt dans `agents/web_agent.py`)

