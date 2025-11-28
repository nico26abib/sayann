# Troubleshooting

## Erreurs courantes et solutions

### 1. PrivilegedIntentsRequired

**Erreur:**
```
discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents...
```

**Cause:** Le bot demande le MESSAGE CONTENT INTENT qui n'est pas activé.

**Solution:**
1. Va sur https://discord.com/developers/applications
2. Sélectionne ton application
3. Menu **Bot** (à gauche)
4. Scroll jusqu'à **Privileged Gateway Intents**
5. Coche ✅ **MESSAGE CONTENT INTENT**
6. Coche ✅ **PRESENCE INTENT** (optionnel)
7. Coche ✅ **SERVER MEMBERS INTENT** (optionnel)
8. Clique **Save Changes**
9. Relance le bot: `python bot.py`

Voir `DISCORD_SETUP.md` pour le guide complet.

---

### 2. Erreur OpenAI API

**Erreur:**
```
openai.AuthenticationError: Incorrect API key
```

**Solution:**
- Vérifie que ta clé API est correcte dans `.env`
- Check sur https://platform.openai.com/api-keys
- Vérifie que tu as du crédit OpenAI

---

### 3. Module not found

**Erreur:**
```
ModuleNotFoundError: No module named 'discord'
```

**Solution:**
```bash
pip install -r requirements.txt
```

---

### 4. Playwright not installed

**Erreur:**
```
playwright._impl._api_types.Error: Executable doesn't exist
```

**Solution:**
```bash
playwright install chromium
```

---

### 5. Bot ne répond pas

**Symptôme:** Le bot est en ligne mais ne répond pas aux messages.

**Checklist:**
- [ ] Tu as mentionné le bot: `@BotName ta question`
- [ ] Ou tu es en DM avec le bot
- [ ] MESSAGE CONTENT INTENT est activé (voir #1)
- [ ] Le bot a les permissions sur le serveur
- [ ] Check les logs: `tail -f logs/bot.log`

---

### 6. Timeout lors de la recherche web

**Erreur:**
```
playwright._impl._api_types.TimeoutError: Timeout 15000ms exceeded
```

**Cause:** Site web trop lent ou problème réseau.

**Solutions:**
1. Augmente le timeout dans `.env`:
   ```
   BROWSER_TIMEOUT=30000
   ```

2. Vérifie ta connexion internet

3. Certains sites bloquent les bots (normal)

---

### 7. Voice transcription failed

**Erreur:**
```
Error transcribing voice message
```

**Causes possibles:**
1. Format audio non supporté
2. Fichier trop gros (max 25MB)
3. Problème API Whisper

**Solution:**
- Réessaye avec un message plus court
- Check les logs pour plus de détails

---

### 8. Rate limit OpenAI

**Erreur:**
```
openai.RateLimitError: Rate limit exceeded
```

**Causes:**
- Trop de requêtes simultanées
- Quota OpenAI dépassé

**Solutions:**
1. Attends quelques secondes et réessaye
2. Check ton usage: https://platform.openai.com/usage
3. Upgrade ton plan OpenAI si nécessaire

---

### 9. Permission denied (lors du setup)

**Erreur:**
```
PermissionError: [Errno 1] Operation not permitted
```

**Solution:**
```bash
chmod +x setup.sh
./setup.sh
```

Ou manuellement:
```bash
pip install -r requirements.txt
playwright install chromium
```

---

### 10. Bot démarre puis crash immédiatement

**Symptôme:** Le bot démarre mais crash après quelques secondes.

**Debug:**
```bash
python bot.py
# Check l'erreur affichée

# Ou check les logs
tail -f logs/bot.log
```

**Causes courantes:**
- Token Discord invalide
- Pas de connexion internet
- Port bloqué par firewall

---

## Debugging général

### Check environment
```bash
python check_env.py
```

### Mode verbose
Change dans `config.py`:
```python
LOG_LEVEL = "DEBUG"
```

Ou directement:
```bash
python -c "import logging; logging.basicConfig(level=logging.DEBUG); exec(open('bot.py').read())"
```

### Test imports
```bash
python -c "from agents.web_agent import WebAgent; from tools.browser import browser_tool; print('OK')"
```

### Test agent seul
```bash
python test_agent.py
```

---

## Logs

**Localisation:** `logs/bot.log`

**Voir en temps réel:**
```bash
tail -f logs/bot.log
```

**Chercher une erreur:**
```bash
grep ERROR logs/bot.log
```

---

## Support

Si le problème persiste:

1. Check les logs: `logs/bot.log`
2. Vérifie la config: `python check_env.py`
3. Teste les imports: `python -c "import bot"`
4. Check la doc Discord: https://discord.com/developers/docs
5. Check la doc OpenAI: https://platform.openai.com/docs

