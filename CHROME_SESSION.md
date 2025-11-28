# 🌐 Utiliser ta session Chrome

Sayann peut se connecter à ton Chrome **déjà ouvert** pour utiliser:
- ✅ Tes cookies
- ✅ Tes sessions (Google, sites connectés)
- ✅ Ton historique
- ✅ Tes extensions

**Avantage:** Pas de captcha, accès aux sites où tu es connecté!

---

## 🚀 Setup (une seule fois)

### 1. Lance Chrome en mode debug

```bash
./scripts/start_chrome_debug.sh
```

Ou manuellement:
```bash
# Ferme Chrome
osascript -e 'quit app "Google Chrome"'

# Lance avec remote debugging
open -na "Google Chrome" --args \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome"
```

### 2. Vérifie que ça marche

```bash
curl http://localhost:9222/json/version
```

Tu devrais voir des infos sur Chrome.

### 3. Configure le bot

Dans `.env`:
```bash
USE_EXISTING_CHROME=true
CHROME_CDP_PORT=9222
```

### 4. Lance le bot

```bash
python bot.py
```

**Le bot utilise maintenant TON Chrome avec toutes tes sessions!**

---

## 🧪 Tester la connexion

```bash
python tests/test_chrome_session.py
```

Ce test:
1. Se connecte à ton Chrome
2. Ouvre un onglet Google
3. Vérifie si tu es connecté
4. Fait un screenshot

---

## 💡 Workflow

```
1. Lance Chrome en mode debug (une fois au démarrage)
   ./scripts/start_chrome_debug.sh

2. Utilise Chrome normalement
   - Connecte-toi à tes sites
   - Navigue comme d'habitude
   
3. Lance le bot
   python bot.py
   
4. Le bot utilise TON Chrome
   - Avec tes sessions
   - Sans captcha
   - Comme si c'était toi qui naviguais
```

---

## 🔧 Options

### Port personnalisé

Dans `.env`:
```bash
CHROME_CDP_PORT=9223
```

Puis lance Chrome:
```bash
open -na "Google Chrome" --args --remote-debugging-port=9223
```

### Désactiver (revenir au mode normal)

Dans `.env`:
```bash
USE_EXISTING_CHROME=false
```

Le bot lancera son propre navigateur isolé.

---

## ⚠️ Troubleshooting

**Erreur: "Unable to connect"**
```bash
# Vérifie que Chrome tourne avec debug
curl http://localhost:9222/json/version

# Si pas de réponse → relance Chrome:
./scripts/start_chrome_debug.sh
```

**Chrome se ferme tout seul**
```bash
# Ne pas utiliser --user-data-dir si problème
open -na "Google Chrome" --args --remote-debugging-port=9222
```

**Conflit de port**
```bash
# Change le port dans .env
CHROME_CDP_PORT=9223

# Et lance Chrome avec ce port
open -na "Google Chrome" --args --remote-debugging-port=9223
```

---

## 🔐 Sécurité

**Le port 9222 donne accès complet à ton Chrome!**

- ⚠️ Ne partage jamais ce port sur Internet
- ✅ C'est OK en local (localhost only)
- ✅ Parfait pour dev/test

En production, utilise `USE_EXISTING_CHROME=false`.

---

## 🎯 Cas d'usage

**Local (dev):**
```bash
USE_EXISTING_CHROME=true   # Utilise ta session
BROWSER_HEADLESS=false     # Tu vois ce qui se passe
```

**Production:**
```bash
USE_EXISTING_CHROME=false  # Navigateur isolé
BROWSER_HEADLESS=true      # Mode serveur
```

