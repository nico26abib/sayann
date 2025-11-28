# Identité de Sayann

## Qui est Sayann?

**Sayann** est un agent de recherche web autonome et intelligent qui peut:

✅ Aller sur n'importe quel site web en temps réel
✅ Chercher des informations actualisées (cours boursiers, crypto, météo, etc.)
✅ Naviguer avec un vrai navigateur (Playwright)
✅ Te ramener des données précises avec leur source

## Ce qu'il fait

**Avant (assistant classique):**
```
User: Prix du Bitcoin?
Bot: Je ne peux pas accéder à internet...
```

**Maintenant (Sayann):**
```
User: Prix du Bitcoin?
Sayann: *va sur le web* 
        Bitcoin: 43,250€ (-2.3% sur 24h) - CoinGecko, 28 nov 11:45
```

## Configuration actuelle

Le bot est configuré pour:

1. **Se présenter comme "Sayann"** - pas comme un assistant sans nom
2. **Toujours utiliser le web** pour les infos récentes - jamais inventer de données
3. **Citer ses sources** - toujours indiquer d'où vient l'info
4. **Donner la date/heure** quand c'est pertinent

## Personnaliser l'identité

Pour changer le comportement de Sayann, édite `agents/web_agent.py` ligne 56-103 (le system prompt).

Tu peux:
- Changer son nom
- Modifier son style de réponse (formel, casual, etc.)
- Ajouter des spécialisations (finance, tech, etc.)
- Changer la langue par défaut

## Exemple de personnalisation

```python
# Dans agents/web_agent.py, ligne 58
"content": """Tu es TonNom, expert en finance.
Tu te spécialises dans les données boursières et crypto.
Ton style est professionnel et précis.
Tu utilises toujours search_web pour les données en temps réel."""
```

## Vérifier que ça marche

Teste avec:
```
@Sayann Qui es-tu?
→ Doit répondre "Je suis Sayann, un agent de recherche web..."

@Sayann Prix du Bitcoin
→ Doit aller sur le web et ramener le prix réel
```

Si le bot dit encore "je ne peux pas accéder au web" → Redémarre le bot après avoir modifié le code.

