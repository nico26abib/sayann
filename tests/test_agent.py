import asyncio
import sys
from pathlib import Path

# Ajoute le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.web_agent import WebAgent
from tools.browser import browser_tool
import config

async def test_agent():
    print("🧪 Testing Web Agent...\n")
    
    agent = WebAgent(api_key=config.OPENAI_API_KEY)
    await browser_tool.start()
    
    test_queries = [
        "Quel est le cours du Bitcoin maintenant ?",
        "Va me chercher le S&P 500 actuel",
    ]
    
    for query in test_queries:
        print(f"📝 Query: {query}")
        try:
            result = await agent.process_query(query)
            print(f"✅ Result: {result}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
    
    await browser_tool.stop()
    print("✓ Tests complete")

if __name__ == "__main__":
    asyncio.run(test_agent())

