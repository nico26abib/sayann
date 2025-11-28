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
                "content": "Tu es un assistant de recherche web expert. Tu utilises les outils disponibles pour trouver des informations précises et récentes. Réponds de manière concise avec la source et la date."
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

