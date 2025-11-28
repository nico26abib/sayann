# 🧪 Lancer le test S&P 500

Test complet qui fait exactement ce que le bot doit faire:
1. ✅ Se connecte à ton Chrome (avec ta session)
2. ✅ Va sur Google
3. ✅ Cherche "S&P 500 Bloomberg"
4. ✅ Clique sur le lien Bloomberg
5. ✅ Extrait la valeur du S&P 500
6. ✅ Affiche le résultat

---

## 🚀 Lancer le test

### 1. Lance Chrome en mode debug
```bash
./scripts/start_chrome_debug.sh
```

Ou pour un profil spécifique:
```bash
# Voir les profils disponibles
./scripts/find_chrome_profiles.sh

# Utiliser un profil
./scripts/start_chrome_debug.sh 'Profile 2'
```

### 2. Vérifie que Chrome est accessible
```bash
curl http://localhost:9222/json/version
```

Tu dois voir du JSON.

### 3. Lance le test
```bash
python tests/test_sp500_complete.py
```

---

## 📊 Ce que tu vas voir

**Dans le terminal:**
```
🧪 Test: Chercher S&P 500 actuel sur Bloomberg

🔗 Connexion à Chrome: http://localhost:9222
✅ Connecté à ton Chrome!

📝 Étape 1: Recherche Google
   Query: S&P 500 Bloomberg
   ...

✅ Page Google chargée

📊 Étape 2: Extraction des données

🔍 Stratégie 1: Featured snippets
   → S&P 500: 5,873.42 (+0.87%)
   ...

💰 Extraction du prix sur Bloomberg:
   → 5,873.42

📈 RÉSULTAT FINAL
✅ S&P 500 estimé: 5873.42
```

**Fichiers générés:**
- `test_sp500_google.png` - Screenshot de Google
- `test_sp500_bloomberg.png` - Screenshot de Bloomberg

---

## 🔧 Debug

Si le test ne trouve pas la valeur:

1. **Regarde les screenshots** générés
2. **Check que tu es connecté** à Google (pour éviter captcha)
3. **Essaie avec un autre profil** Chrome

---

## ✅ Une fois que ça marche

Le bot Discord utilisera exactement la même logique!

```bash
python bot.py
```

Puis dans Discord:
```
@Sayann va me chercher le sp500 actuel
```

Le bot fera exactement ce que le test fait.

