#!/usr/bin/env python3
"""
Test de connexion à ta session Chrome existante
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright
import config

async def test_existing_chrome():
    print("🧪 Test de connexion à Chrome existant\n")
    
    cdp_url = f"http://localhost:{config.CHROME_CDP_PORT}"
    print(f"🔗 Tentative de connexion: {cdp_url}")
    
    playwright = await async_playwright().start()
    
    try:
        # Se connecte au Chrome déjà ouvert
        browser = await playwright.chromium.connect_over_cdp(cdp_url)
        print("✅ Connecté à ton Chrome!")
        
        # Liste les contextes (onglets)
        contexts = browser.contexts
        print(f"\n📑 Contextes disponibles: {len(contexts)}")
        
        # Utilise le premier contexte ou en crée un
        if contexts:
            context = contexts[0]
            print(f"   Utilisation du contexte existant")
        else:
            context = await browser.new_context()
            print(f"   Création d'un nouveau contexte")
        
        # Ouvre une page
        page = await context.new_page()
        print(f"\n🌐 Navigation vers Google...")
        
        await page.goto("https://www.google.com/search?q=test", timeout=15000)
        await page.wait_for_load_state("domcontentloaded")
        
        print("✅ Page chargée!")
        
        # Récupère le titre
        title = await page.title()
        print(f"📄 Titre: {title}")
        
        # Vérifie si on est connecté (regarde si profil Google visible)
        print(f"\n🔍 Vérification de la session...")
        
        content = await page.content()
        if "Sign in" in content or "Connexion" in content:
            print("⚠️  Pas connecté à Google")
        else:
            print("✅ Session Google active!")
        
        # Screenshot
        await page.screenshot(path="chrome_session_test.png")
        print(f"\n📸 Screenshot: chrome_session_test.png")
        
        print("\n⏸  Fenêtre ouverte 5 secondes...")
        await asyncio.sleep(5)
        
        await page.close()
        await browser.close()
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        print(f"\n💡 Solution:")
        print(f"   1. Lance Chrome en mode debug:")
        print(f"      ./scripts/start_chrome_debug.sh")
        print(f"   2. Relance ce test")
        
    finally:
        await playwright.stop()
        print("\n✅ Test terminé")

if __name__ == "__main__":
    asyncio.run(test_existing_chrome())

