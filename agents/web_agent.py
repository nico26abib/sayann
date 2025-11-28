from openai import AsyncOpenAI
from tools.browser import browser_tool
import json
import config

class WebAgent:
    def __init__(self, api_key: str, model: str = None):
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model or config.OPENAI_MODEL
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "search_web",
                    "description": "Cherche des informations sur Google et extrait les résultats pertinents",
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
            },
            {
                "type": "function",
                "function": {
                    "name": "visit_url",
                    "description": "Visite une URL spécifique et extrait son contenu",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "L'URL complète à visiter"
                            }
                        },
                        "required": ["url"]
                    }
                }
            }
        ]
        
    async def execute_tool(self, tool_name: str, arguments: dict) -> str:
        if tool_name == "search_web":
            return await browser_tool.search_and_extract(arguments["query"])
        elif tool_name == "visit_url":
            return await browser_tool.navigate_to(arguments["url"])
        return "Tool not found"
        
    async def process_query(self, user_query: str) -> str:
        messages = [
            {
                "role": "system",
                "content": """Tu es Sayann, un agent de recherche web intelligent et autonome.

**Ta personnalité:**
- Tu es direct, efficace et précis
- Tu t'exprimes de manière naturelle et conversationnelle
- Tu n'hésites pas à utiliser des émojis quand c'est pertinent
- Tu es proactif: tu vas chercher l'info sans attendre

**Ton fonctionnement:**
- Tu utilises TOUJOURS les outils (search_web/visit_url) pour les infos récentes
- Tu CITES toujours tes sources (site web + heure si pertinent)
- Tu ne devines JAMAIS, tu vas vérifier sur le web
- Tu synthétises l'info de manière claire et concise

**Ton style de réponse:**
- Format: [Réponse précise] - [Source] [Date/Heure si pertinent]
- Exemple: "Bitcoin: 43,250€ (-2.3% sur 24h) - CoinGecko, 28 nov 11:45"
- Si on te demande qui tu es: "Je suis Sayann, ton agent de recherche web. Je vais chercher n'importe quelle info en temps réel sur internet."

Tu es là pour aller chercher ce que les autres assistants ne peuvent pas: l'info en temps réel sur le web."""
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
        
        # First call to get tool calls
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=self.tools,
            tool_choice="auto",
            temperature=config.OPENAI_TEMPERATURE
        )
        
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        
        if tool_calls:
            messages.append(response_message)
            
            # Execute each tool call
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                function_response = await self.execute_tool(function_name, function_args)
                
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response
                })
            
            # Second call to get final response
            final_response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=config.OPENAI_TEMPERATURE
            )
            
            return final_response.choices[0].message.content
        
        return response_message.content

