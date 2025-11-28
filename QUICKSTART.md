# Démarrage en 3 minutes

## 1. Install

```bash
./setup.sh
```

## 2. Get tokens

**Discord:**
- https://discord.com/developers/applications
- New Application → Bot → Copy Token

**OpenAI:**
- https://platform.openai.com/api-keys
- Create new secret key

## 3. Config

Edit `.env`:

```
DISCORD_TOKEN=ton_token_ici
OPENAI_API_KEY=ta_cle_ici
```

## 4. Run

```bash
python bot.py
```

## 5. Invite bot

- Discord Dev Portal → OAuth2 → URL Generator
- Select: `bot`
- Permissions: `Send Messages`, `Read Messages`, `Attach Files`
- Copy URL → Open → Add to server

## 6. Test

Dans Discord:

```
@BotName Va me chercher le cours du Bitcoin
```

Vocal: Envoie un message vocal → il transcrit + répond

## Deploy

```bash
# Railway
railway login && railway init && railway up

# Docker
docker-compose up -d
```

Done.

