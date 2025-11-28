#!/usr/bin/env python3
import os
from dotenv import load_dotenv

load_dotenv()

checks = {
    "DISCORD_TOKEN": os.getenv("DISCORD_TOKEN"),
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
}

print("🔍 Checking environment...\n")

all_good = True
for key, value in checks.items():
    if value and value != f"your_{key.lower()}_here" and len(value) > 10:
        print(f"✅ {key}")
    else:
        print(f"❌ {key} - Missing or invalid")
        all_good = False

print()

if all_good:
    print("✅ All set! Run: python bot.py")
else:
    print("⚠️  Edit .env with valid tokens")
    print("   Discord: https://discord.com/developers/applications")
    print("   OpenAI: https://platform.openai.com/api-keys")

