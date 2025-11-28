# Comment scaler l'agent

## Ajouter un nouveau tool

### 1. Créer le tool

```python
# tools/crypto.py
import aiohttp

async def get_crypto_price(symbol: str) -> dict:
    """Get crypto price from CoinGecko"""
    async with aiohttp.ClientSession() as session:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        async with session.get(url) as resp:
            return await resp.json()
```

### 2. Enregistrer dans l'agent

```python
# agents/web_agent.py
self.tools = [
    # ... tools existants
    {
        "type": "function",
        "function": {
            "name": "get_crypto_price",
            "description": "Récupère le prix d'une crypto en temps réel",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Le symbole de la crypto (bitcoin, ethereum, etc.)"
                    }
                },
                "required": ["symbol"]
            }
        }
    }
]
```

### 3. Ajouter l'exécution

```python
# agents/web_agent.py
async def execute_tool(self, tool_name: str, arguments: dict) -> str:
    # ... conditions existantes
    elif tool_name == "get_crypto_price":
        from tools.crypto import get_crypto_price
        result = await get_crypto_price(arguments["symbol"])
        return f"Prix: ${result[arguments['symbol']]['usd']}"
```

Done. L'agent utilise automatiquement le nouveau tool.

## Exemples de tools à ajouter

### Weather
```python
# tools/weather.py
async def get_weather(city: str) -> str:
    # OpenWeatherMap API
```

### Finance
```python
# tools/finance.py
async def get_stock_price(ticker: str) -> dict:
    # Yahoo Finance API
```

### Database
```python
# tools/database.py
async def query_db(query: str) -> list:
    # PostgreSQL/MongoDB
```

### Screenshot
```python
# tools/screenshot.py
async def take_screenshot(url: str) -> bytes:
    # Playwright screenshot
```

### PDF Reader
```python
# tools/pdf.py
async def extract_pdf_text(url: str) -> str:
    # PyPDF2
```

## Multi-agents

```python
# agents/specialist_agent.py
class FinanceAgent(WebAgent):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.tools.extend([
            # Finance-specific tools
        ])
```

```python
# bot.py
finance_agent = FinanceAgent(api_key)
research_agent = WebAgent(api_key)

# Route based on query type
if "prix" in query or "cours" in query:
    result = await finance_agent.process_query(query)
else:
    result = await research_agent.process_query(query)
```

## Memory / Context

```python
# agents/web_agent.py
self.conversation_history = {}

async def process_query(self, user_query: str, user_id: str) -> str:
    if user_id not in self.conversation_history:
        self.conversation_history[user_id] = []
    
    self.conversation_history[user_id].append({
        "role": "user",
        "content": user_query
    })
    
    messages = [system_prompt] + self.conversation_history[user_id]
    # ... rest of the logic
```

## Rate Limiting

```python
# utils/rate_limit.py
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, max_requests=5, window=60):
        self.requests = defaultdict(list)
        self.max_requests = max_requests
        self.window = window
    
    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        self.requests[user_id] = [
            req for req in self.requests[user_id]
            if now - req < self.window
        ]
        
        if len(self.requests[user_id]) < self.max_requests:
            self.requests[user_id].append(now)
            return True
        return False
```

## Caching

```python
# utils/cache.py
import aioredis
import json

class Cache:
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(redis_url)
    
    async def get(self, key: str):
        value = await self.redis.get(key)
        return json.loads(value) if value else None
    
    async def set(self, key: str, value: any, ttl=3600):
        await self.redis.set(key, json.dumps(value), ex=ttl)
```

Architecture devient:

```
bot.py → router → agents/ → tools/ → cache → APIs
                    ↓
                 memory
```

Scalable jusqu'à des milliers d'utilisateurs simultanés.

