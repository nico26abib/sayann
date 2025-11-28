from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import asyncio
import config

class BrowserTool:
    def __init__(self):
        self.playwright = None
        self.browser = None
        
    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=config.BROWSER_HEADLESS)
        
    async def stop(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
            
    async def search_and_extract(self, query: str) -> str:
        """Search web and extract relevant info"""
        if not self.browser:
            await self.start()
            
        context = await self.browser.new_context()
        page = await context.new_page()
        
        try:
            # Search on Google
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            await page.goto(search_url, timeout=config.BROWSER_TIMEOUT)
            await page.wait_for_load_state("networkidle")
            
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract search results
            results = []
            for g in soup.find_all('div', class_='g')[:3]:
                title = g.find('h3')
                snippet = g.find('div', class_=['VwiC3b', 'yXK7lf'])
                if title and snippet:
                    results.append(f"{title.get_text()}: {snippet.get_text()}")
                    
            return "\n\n".join(results) if results else "Aucun résultat trouvé"
            
        except Exception as e:
            return f"Erreur: {str(e)}"
        finally:
            await context.close()
            
    async def navigate_to(self, url: str) -> str:
        """Navigate to specific URL and extract content"""
        if not self.browser:
            await self.start()
            
        context = await self.browser.new_context()
        page = await context.new_page()
        
        try:
            await page.goto(url, timeout=config.BROWSER_TIMEOUT)
            await page.wait_for_load_state("networkidle")
            
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text[:5000]  # Limit to 5000 chars
            
        except Exception as e:
            return f"Erreur: {str(e)}"
        finally:
            await context.close()

browser_tool = BrowserTool()

