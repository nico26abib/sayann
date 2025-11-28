# ⚙️ Variables d'environnement

Toutes les variables disponibles pour configurer Sayann.

## 🔑 Obligatoires

```bash
# Token Discord Bot
DISCORD_TOKEN=your_discord_bot_token_here

# Clé API OpenAI
OPENAI_API_KEY=your_openai_api_key_here
```

## 🎨 Optionnelles

### OpenAI
```bash
# Modèle à utiliser (défaut: gpt-4o)
OPENAI_MODEL=gpt-4o

# Température (0 = déterministe, 1 = créatif)
OPENAI_TEMPERATURE=0
```

### Discord
```bash
# Préfixe des commandes (défaut: !)
COMMAND_PREFIX=!
```

### Navigateur
```bash
# Timeout navigation en ms (défaut: 15000 = 15s)
BROWSER_TIMEOUT=15000

# Mode headless (défaut: false pour debug local)
BROWSER_HEADLESS=false

# Utiliser Chrome local au lieu de Chromium embarqué (défaut: true)
USE_LOCAL_CHROME=true
```

**Note:** Chrome local est automatiquement détecté sur macOS, Linux, Windows.

### Vocal
```bash
# Modèle Whisper (défaut: whisper-1)
WHISPER_MODEL=whisper-1

# Langue de transcription (défaut: fr)
WHISPER_LANGUAGE=fr
```

### Réponses
```bash
# Longueur max réponse Discord (défaut: 2000)
MAX_RESPONSE_LENGTH=2000

# Afficher indicateur "typing..." (défaut: true)
TYPING_INDICATOR=true
```

### Rate Limiting
```bash
# Nombre de requêtes max par fenêtre (défaut: 10)
RATE_LIMIT_REQUESTS=10

# Fenêtre en secondes (défaut: 60)
RATE_LIMIT_WINDOW=60
```

## 📝 Exemple .env complet

```bash
# Obligatoire
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=sk-proj-abc123...

# Optionnel
OPENAI_MODEL=gpt-4o
BROWSER_HEADLESS=false
USE_LOCAL_CHROME=true
COMMAND_PREFIX=!
```

## 🔍 Chrome local

Sayann cherche Chrome/Chromium automatiquement:

**macOS:**
- `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- `/Applications/Chromium.app/Contents/MacOS/Chromium`

**Linux:**
- `/usr/bin/google-chrome`
- `/usr/bin/chromium-browser`
- `/usr/bin/chromium`

**Windows:**
- `C:\Program Files\Google\Chrome\Application\chrome.exe`
- `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`

Si Chrome n'est pas trouvé, Playwright utilise Chromium embarqué automatiquement.

## 🚀 Environnements

### Local (dev)
```bash
BROWSER_HEADLESS=false
USE_LOCAL_CHROME=true
```

### Production
```bash
BROWSER_HEADLESS=true
USE_LOCAL_CHROME=false
```

Le bot s'adapte automatiquement!

