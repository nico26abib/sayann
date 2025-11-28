#!/usr/bin/env python3
"""
Test complet: Chercher le S&P 500 sur Bloomberg via Google
Ce test simule exactement ce que le bot doit faire
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import config
import re

async def test_sp500_search():
    print("🧪 Test: Chercher S&P 500 actuel sur Bloomberg\n")
    
    cdp_url = f"http://localhost:{config.CHROME_CDP_PORT}"
    print(f"🔗 Connexion à Chrome: {cdp_url}")
    
    playwright = await async_playwright().start()
    
    try:
        # Connexion au Chrome existant
        browser = await playwright.chromium.connect_over_cdp(cdp_url)
        print("✅ Connecté à ton Chrome!\n")
        
        # Utilise le premier contexte ou en crée un
        if browser.contexts:
            context = browser.contexts[0]
        else:
            context = await browser.new_context()
        
        page = await context.new_page()
        
        # Étape 1: Recherche Google
        query = "S&P 500 Bloomberg"
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        
        print(f"📝 Étape 1: Recherche Google")
        print(f"   Query: {query}")
        print(f"   URL: {search_url}\n")
        
        await page.goto(search_url, timeout=15000)
        await page.wait_for_load_state("domcontentloaded")
        await asyncio.sleep(2)  # Laisse le temps à la page de charger
        
        print("✅ Page Google chargée\n")
        
        # Screenshot de Google
        await page.screenshot(path="test_sp500_google.png")
        print("📸 Screenshot sauvegardé: test_sp500_google.png\n")
        
        # Étape 2: Extraction des résultats
        print(f"📊 Étape 2: Extraction des données")
        
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        # Stratégie 1: Chercher les featured snippets / knowledge panel
        print("\n🔍 Stratégie 1: Featured snippets / Knowledge panel")
        featured = soup.find_all(['div', 'span'], class_=re.compile('(kCrYT|Z0LcW|IZ6rdc|kp-header)'))
        for f in featured[:5]:
            text = f.get_text(strip=True)
            if len(text) > 10 and len(text) < 200:
                print(f"   → {text}")
        
        # Stratégie 2: Chercher tous les chiffres qui ressemblent à un index
        print("\n🔍 Stratégie 2: Recherche de chiffres (format index)")
        all_text = soup.get_text()
        
        # Patterns pour S&P 500: 5,873.42 ou 5873.42 ou 5,873
        patterns = [
            r'S&P[^\d]*?(\d{1,2}[,.]?\d{3}\.?\d{0,2})',  # S&P 500: 5,873.42
            r'(\d{1,2}[,.]?\d{3}\.?\d{0,2}).*?(?:S&P|points?)',  # 5,873.42 ... S&P
        ]
        
        found_values = set()
        for pattern in patterns:
            matches = re.findall(pattern, all_text, re.IGNORECASE)
            for match in matches:
                clean = match.replace(',', '').replace(' ', '')
                try:
                    val = float(clean)
                    # S&P 500 est généralement entre 1000 et 10000
                    if 1000 <= val <= 10000:
                        found_values.add(clean)
                except:
                    pass
        
        if found_values:
            print(f"   Valeurs trouvées: {sorted(found_values, reverse=True)}")
        
        # Stratégie 3: Chercher dans les h3 (titres des résultats)
        print("\n🔍 Stratégie 3: Titres des résultats Google")
        h3s = soup.find_all('h3')
        for h3 in h3s[:5]:
            text = h3.get_text()
            print(f"   → {text}")
        
        # Stratégie 4: Chercher des divs avec des classes spécifiques
        print("\n🔍 Stratégie 4: Divs de résultats")
        result_divs = soup.find_all('div', class_=['g', 'N54PNb', 'BNeawe'])
        for div in result_divs[:5]:
            text = div.get_text(strip=True)
            if 'S&P' in text or '500' in text:
                # Extrait juste une partie
                snippet = text[:150] + "..." if len(text) > 150 else text
                print(f"   → {snippet}")
        
        # Stratégie 5: Cliquer sur le premier lien Bloomberg si trouvé
        print("\n🔍 Stratégie 5: Cherche lien Bloomberg")
        links = await page.query_selector_all('a[href*="bloomberg"]')
        
        if links:
            print(f"   ✅ {len(links)} lien(s) Bloomberg trouvé(s)")
            
            # Clique sur le premier
            try:
                first_link = links[0]
                href = await first_link.get_attribute('href')
                print(f"   🔗 Clic sur: {href[:100]}...")
                
                await first_link.click()
                await page.wait_for_load_state("domcontentloaded")
                await asyncio.sleep(2)
                
                print("   ✅ Page Bloomberg chargée\n")
                
                # Screenshot de Bloomberg
                await page.screenshot(path="test_sp500_bloomberg.png")
                print("📸 Screenshot Bloomberg: test_sp500_bloomberg.png\n")
                
                # Extrait le contenu de Bloomberg
                bloomberg_content = await page.content()
                bloomberg_soup = BeautifulSoup(bloomberg_content, 'html.parser')
                
                # Cherche le prix sur Bloomberg
                print("💰 Extraction du prix sur Bloomberg:")
                
                # Cherche dans le titre
                title = await page.title()
                print(f"   Title: {title}")
                
                # Cherche des spans/divs avec des chiffres
                price_elements = bloomberg_soup.find_all(['span', 'div'], class_=re.compile('(price|value|quote)'))
                for elem in price_elements[:10]:
                    text = elem.get_text(strip=True)
                    if re.search(r'\d{1,2}[,.]?\d{3}', text):
                        print(f"   → {text}")
                
                # Cherche tous les gros chiffres
                all_bloomberg_text = bloomberg_soup.get_text()
                sp500_values = re.findall(r'(\d{1,2}[,.]?\d{3}\.?\d{0,2})', all_bloomberg_text)
                sp500_values = [v for v in sp500_values if 1000 <= float(v.replace(',', '')) <= 10000]
                
                if sp500_values:
                    print(f"\n   📊 Valeurs potentielles du S&P 500:")
                    for val in sorted(set(sp500_values), reverse=True)[:5]:
                        print(f"      • {val}")
                
            except Exception as e:
                print(f"   ⚠️  Erreur clic Bloomberg: {e}")
        else:
            print("   ⚠️  Aucun lien Bloomberg trouvé dans les résultats")
        
        # Résumé final
        print("\n" + "="*60)
        print("📈 RÉSULTAT FINAL")
        print("="*60)
        
        if found_values:
            best_value = sorted(found_values, reverse=True)[0]
            print(f"✅ S&P 500 estimé: {best_value}")
            print(f"   (trouvé sur la page Google)")
        else:
            print("⚠️  Valeur du S&P 500 non trouvée automatiquement")
            print("   Regarde les screenshots pour analyse manuelle:")
            print("   - test_sp500_google.png")
            print("   - test_sp500_bloomberg.png")
        
        print("\n⏸  Fenêtre reste ouverte 10 secondes...")
        await asyncio.sleep(10)
        
        await page.close()
        await browser.close()
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        
        print(f"\n💡 Solution:")
        print(f"   1. Lance Chrome: ./scripts/start_chrome_debug.sh")
        print(f"   2. Vérifie: curl http://localhost:9222/json/version")
        print(f"   3. Relance ce test")
        
    finally:
        await playwright.stop()
        print("\n✅ Test terminé")

if __name__ == "__main__":
    asyncio.run(test_sp500_search())

