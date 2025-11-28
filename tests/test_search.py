import asyncio
import sys
from pathlib import Path

# Ajoute le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.browser import browser_tool

async def test():
    print("🧪 Testing web search...")
    
    await browser_tool.start()
    
    queries = [
        "S&P 500 index live",
        "Bitcoin price USD",
    ]
    
    for query in queries:
        print(f"\n📝 Query: {query}")
        result = await browser_tool.search_and_extract(query)
        print(f"✅ Result ({len(result)} chars):")
        print(result[:500])
        print("...")
    
    await browser_tool.stop()

if __name__ == "__main__":
    asyncio.run(test())

