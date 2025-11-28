# 🔊 Fonctionnalité Vocale de Sayann

## Capacités Vocales

Sayann peut maintenant:

✅ **Transcriber** tes messages vocaux → texte (déjà disponible)  
✅ **Répondre en vocal** quand tu le demandes (nouveau)

---

## Comment utiliser

### 1. Envoyer un message vocal

Enregistre un message vocal sur Discord et envoie-le à Sayann.

```
🎤 [message vocal]
→ Sayann transcrit automatiquement
→ Répond par texte
```

### 2. Demander une réponse vocale

Ajoute "en vocal" ou "en voix" dans ta demande:

```
@Sayann Prix du Bitcoin en vocal
→ 🔊 Réponse vocale: [fichier audio MP3]

@Sayann Météo Paris réponds en voix
→ 🔊 Réponse vocale: [fichier audio MP3]

@Sayann dis-moi en vocal le cours EUR/USD
→ 🔊 Réponse vocale: [fichier audio MP3]
```

### 3. Commande !voice

```bash
!voice Prix du Bitcoin
→ 🔊 Réponse vocale: [fichier audio MP3]
```

---

## Configuration

Dans ton `.env`:

```bash
# Voice Configuration
WHISPER_MODEL=whisper-1        # Modèle de transcription
WHISPER_LANGUAGE=fr            # Langue de transcription

TTS_MODEL=tts-1                # Modèle text-to-speech (tts-1 ou tts-1-hd)
TTS_VOICE=alloy                # Voix (alloy, echo, fable, onyx, nova, shimmer)
TTS_SPEED=1.0                  # Vitesse de parole (0.25 à 4.0)
```

### Voix disponibles

- **alloy** - Neutre, équilibrée
- **echo** - Masculine, claire
- **fable** - Masculine, expressive
- **onyx** - Masculine, profonde
- **nova** - Féminine, énergique
- **shimmer** - Féminine, douce

### Changer de voix

```bash
# Dans .env
TTS_VOICE=nova
```

Redémarre le bot pour appliquer les changements.

---

## Exemples d'usage

### Scénario 1: Question rapide en vocal

```
Toi: @Sayann en vocal, c'est quoi le S&P 500 ?
Sayann: 🔊 [Audio] "S&P 500 est à 5 873 points, en hausse de 0.87% aujourd'hui..."
```

### Scénario 2: Message vocal → Réponse vocale

```
Toi: 🎤 [audio] "Prix du Bitcoin maintenant"
Sayann: 🎤 Prix du Bitcoin maintenant
        🔊 Réponse vocale: [Audio] "Bitcoin est actuellement à 43,250 euros..."
```

### Scénario 3: Info complexe en vocal

```
!voice Explique-moi la situation économique actuelle
→ 🔊 [Audio long] avec explication complète
```

---

## Coûts

Les réponses vocales utilisent l'API OpenAI TTS:

- **tts-1**: $0.015 / 1K caractères (rapide)
- **tts-1-hd**: $0.030 / 1K caractères (haute qualité)

Exemple: Une réponse de 100 mots (≈600 caractères) coûte environ $0.01 avec tts-1.

---

## Limitations

- ⚠️ Les réponses longues (>4096 caractères) peuvent être tronquées
- ⚠️ Discord limite les fichiers à 8MB (largement suffisant)
- ⚠️ Génération vocale ajoute 1-3 secondes au temps de réponse

---

## Troubleshooting

**Le bot ne génère pas de voix:**
- Vérifie que `TTS_MODEL` et `TTS_VOICE` sont définis dans `.env`
- Check les logs: `tail -f logs/bot.log`
- Vérifie ton crédit OpenAI

**La voix est trop rapide/lente:**
```bash
# Dans .env
TTS_SPEED=0.8  # Plus lent
TTS_SPEED=1.5  # Plus rapide
```

**Erreur "Voice generation error":**
- Le texte est peut-être vide
- Vérifie ta clé API OpenAI
- Check que le modèle TTS est accessible dans ton compte

---

## Désactiver la voix

Si tu veux désactiver la synthèse vocale, commente simplement les lignes TTS dans `.env`:

```bash
# TTS_MODEL=tts-1
# TTS_VOICE=alloy
# TTS_SPEED=1.0
```

Le bot continuera à transcriber tes messages vocaux mais ne générera plus de réponses audio.

---

## Next Steps

- Ajouter support des voix personnalisées
- Permettre de changer de voix à la volée via commande
- Ajouter streaming audio en temps réel


