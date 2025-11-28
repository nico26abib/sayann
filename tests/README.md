# 🧪 Tests & Debug

## Tests disponibles

### 1. check_env.py
Vérifie que les tokens sont configurés.

```bash
python tests/check_env.py
```

### 2. test_browser_visual.py
Ouvre un navigateur VISIBLE pour voir ce qui se passe.
- Va sur Google
- Fait une recherche "S&P 500"
- Sauvegarde screenshot + HTML
- Affiche les résultats trouvés

```bash
python tests/test_browser_visual.py
```

Tu verras le navigateur s'ouvrir en vrai!

### 3. test_direct_api.py
Test OpenAI function calling sans le bot Discord.
Vérifie que le modèle appelle bien les outils.

```bash
python tests/test_direct_api.py
```

### 4. test_agent.py
Test l'agent complet (scraping + OpenAI).

```bash
python tests/test_agent.py
```

### 5. test_search.py
Test rapide du scraping Google.

```bash
python tests/test_search.py
```

## Debugging

**Voir les logs en temps réel:**
```bash
tail -f logs/bot.log
```

**Mode debug (navigateur visible):**
Édite `.env`:
```
BROWSER_HEADLESS=false
```

**Tester une requête spécifique:**
```bash
python tests/test_agent.py
# Édite le fichier pour changer la requête
```

## Fichiers générés

Les tests génèrent ces fichiers pour debug:
- `debug_google.png` - Screenshot de Google
- `debug_google.html` - HTML brut de la page
- `logs/bot.log` - Logs du bot

## Workflow de debug

1. `check_env.py` → Vérifie les tokens
2. `test_browser_visual.py` → Vérifie le scraping (avec navigateur visible)
3. `test_direct_api.py` → Vérifie qu'OpenAI appelle les outils
4. `test_agent.py` → Test complet
5. `python bot.py` → Lance le bot

Si ça ne marche toujours pas → Check `logs/bot.log`

