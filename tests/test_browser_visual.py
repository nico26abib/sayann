#!/usr/bin/env python3
"""
Test du browser en mode VISIBLE pour debugging
"""
import asyncio
import sys
from pathlib import Path

# Ajoute le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def test_google_search():
    print("🌐 Démarrage du navigateur (VISIBLE)...")
    
    # Trouve Chrome local
    import config
    chrome_path = config.get_chrome_path()
    
    if chrome_path:
        print(f"✅ Chrome local trouvé: {chrome_path}")
    else:
        print("⚠️  Chrome local non trouvé, utilisation de Chromium embarqué")
    
    playwright = await async_playwright().start()
    
    launch_options = {
        "headless": False,  # VISIBLE
        "slow_mo": 1000  # Ralenti pour voir ce qui se passe
    }
    
    if chrome_path:
        launch_options["executable_path"] = chrome_path
    
    browser = await playwright.chromium.launch(**launch_options)
    
    context = await browser.new_context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    
    page = await context.new_page()
    
    try:
        query = "S&P 500 index live"
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        
        print(f"📝 Recherche: {query}")
        print(f"🔗 URL: {search_url}")
        print("\n⏳ Navigation en cours... (regarde le navigateur)")
        
        await page.goto(search_url, timeout=30000)
        await page.wait_for_load_state("domcontentloaded")
        
        print("✅ Page chargée!")
        
        # Attends 3 secondes pour que tu puisses voir
        await asyncio.sleep(3)
        
        # Screenshot
        await page.screenshot(path="debug_google.png")
        print("📸 Screenshot sauvegardé: debug_google.png")
        
        # Extraire le contenu
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        # Sauvegarder le HTML brut
        with open("debug_google.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("💾 HTML sauvegardé: debug_google.html")
        
        # Chercher les résultats
        print("\n🔍 Recherche de résultats...")
        
        # Strategy 1: Divs avec class 'g'
        results = soup.find_all('div', class_='g')
        print(f"   Strategy 1 - class='g': {len(results)} trouvés")
        
        # Strategy 2: Featured snippets
        featured = soup.find_all('div', class_=['kp-header', 'IZ6rdc', 'kCrYT'])
        print(f"   Strategy 2 - featured: {len(featured)} trouvés")
        
        # Strategy 3: h3 tags (titres)
        h3s = soup.find_all('h3')
        print(f"   Strategy 3 - h3 tags: {len(h3s)} trouvés")
        
        # Afficher les 3 premiers h3
        print("\n📄 Premiers titres trouvés:")
        for i, h3 in enumerate(h3s[:5], 1):
            print(f"   {i}. {h3.get_text()[:100]}")
        
        # Chercher des prix / chiffres
        print("\n💰 Recherche de chiffres/prix...")
        text = soup.get_text()
        import re
        numbers = re.findall(r'\d+[,\.]\d+', text)[:10]
        print(f"   Chiffres trouvés: {numbers}")
        
        print("\n⏸  Le navigateur reste ouvert 10 secondes pour inspection...")
        await asyncio.sleep(10)
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        await browser.close()
        await playwright.stop()
        print("\n✅ Test terminé")

if __name__ == "__main__":
    asyncio.run(test_google_search())

