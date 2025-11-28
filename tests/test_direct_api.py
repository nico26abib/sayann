#!/usr/bin/env python3
"""
Test direct de l'API OpenAI avec function calling
pour voir si le problème vient du modèle ou du scraping
"""
import asyncio
import sys
from pathlib import Path

# Ajoute le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from openai import AsyncOpenAI
import config
import json

async def test_function_calling():
    print("🧪 Test OpenAI Function Calling\n")
    
    client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "search_web",
                "description": "Effectue une recherche Google. Utilise TOUJOURS cet outil pour les infos récentes: prix, cours, météo, etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "La requête de recherche"
                        }
                    },
                    "required": ["query"]
                }
            }
        }
    ]
    
    messages = [
        {
            "role": "system",
            "content": "Tu es un agent web. Tu DOIS utiliser search_web() pour TOUTE demande d'information. Ne réponds JAMAIS sans appeler l'outil."
        },
        {
            "role": "user",
            "content": "Va me chercher le S&P 500 actuel"
        }
    ]
    
    print("📤 Envoi de la requête à OpenAI...")
    print(f"   Model: {config.OPENAI_MODEL}")
    print(f"   Tool choice: required\n")
    
    response = await client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=messages,
        tools=tools,
        tool_choice="required"
    )
    
    response_message = response.choices[0].message
    
    print("📥 Réponse reçue:")
    print(f"   Finish reason: {response.choices[0].finish_reason}")
    
    if response_message.tool_calls:
        print(f"   ✅ Tool calls: {len(response_message.tool_calls)}")
        for i, tool_call in enumerate(response_message.tool_calls, 1):
            print(f"\n   Tool call #{i}:")
            print(f"      Function: {tool_call.function.name}")
            print(f"      Arguments: {tool_call.function.arguments}")
    else:
        print("   ❌ Aucun tool call!")
        if response_message.content:
            print(f"   Content: {response_message.content}")
    
    print("\n" + "="*50)
    print("Conclusion:")
    if response_message.tool_calls:
        print("✅ OpenAI appelle bien les outils!")
        print("→ Le problème doit venir du scraping Google")
    else:
        print("❌ OpenAI n'appelle pas les outils!")
        print("→ Le problème est dans le prompt ou la config")

if __name__ == "__main__":
    asyncio.run(test_function_calling())

