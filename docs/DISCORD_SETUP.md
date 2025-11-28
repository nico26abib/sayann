# Configuration Discord Bot

## ⚠️ Erreur: PrivilegedIntentsRequired

Si tu vois cette erreur:
```
discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents...
```

**Solution:** Active les intents privilégiés dans Discord Developer Portal

---

## 🔧 Configuration complète (5 minutes)

### 1. Créer l'application Discord

1. Va sur https://discord.com/developers/applications
2. Clique **New Application**
3. Donne un nom (ex: "Sayann Web Agent")
4. Accepte les conditions

### 2. Créer le bot

1. Menu de gauche → **Bot**
2. Clique **Add Bot** → **Yes, do it!**
3. Clique **Reset Token** → Copy le token
4. Colle-le dans ton `.env`:
   ```
   DISCORD_TOKEN=ton_token_ici
   ```

### 3. ⚠️ ACTIVER LES PRIVILEGED INTENTS (OBLIGATOIRE)

**Dans la page Bot, scroll down jusqu'à "Privileged Gateway Intents":**

Coche les 3 options:
- ✅ **PRESENCE INTENT**
- ✅ **SERVER MEMBERS INTENT**
- ✅ **MESSAGE CONTENT INTENT** ← **CRUCIAL**

Clique **Save Changes**

### 4. Permissions du bot

Dans **Bot** → **Bot Permissions**, active:
- ✅ Send Messages
- ✅ Read Messages/View Channels
- ✅ Read Message History
- ✅ Attach Files
- ✅ Embed Links
- ✅ Use Slash Commands (optionnel)

### 5. Générer l'URL d'invitation

1. Menu de gauche → **OAuth2** → **URL Generator**
2. **Scopes:** Coche `bot`
3. **Bot Permissions:** Coche les mêmes que ci-dessus
4. Copy l'URL générée en bas

### 6. Inviter le bot

1. Colle l'URL dans ton navigateur
2. Sélectionne ton serveur Discord
3. Clique **Authorize**
4. Complète le captcha

---

## ✅ Vérification

Une fois fait:

```bash
python check_env.py
# Doit afficher ✅ DISCORD_TOKEN

python bot.py
# Doit afficher: ✓ TonBot ready
```

---

## 📝 Récapitulatif des intents requis

Le bot a besoin de ces intents:

```python
intents = discord.Intents.default()
intents.message_content = True  # OBLIGATOIRE pour lire les messages
intents.voice_states = True     # Pour le support vocal
```

Sans `MESSAGE CONTENT INTENT` activé dans le portail → Le bot ne peut pas lire le contenu des messages → Erreur.

---

## 🔗 Liens rapides

- Developer Portal: https://discord.com/developers/applications
- Documentation Intents: https://discord.com/developers/docs/topics/gateway#privileged-intents

---

## 💡 Alternative (si tu ne peux pas activer les intents)

Si ton bot est sur +100 serveurs ou vérifié, tu dois passer par un processus d'approbation Discord.

Pour un bot perso/petit serveur → Pas de problème, active juste les intents comme décrit ci-dessus.

