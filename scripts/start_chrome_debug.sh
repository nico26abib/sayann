#!/bin/bash

# Lance Chrome en mode debug pour que Sayann puisse s'y connecter
# Cela permet d'utiliser ta session Chrome existante (cookies, logins, etc.)

PORT=9222
PROFILE="${1:-Default}"  # Profil à utiliser (par défaut: Default)

echo "🚀 Lancement de Chrome en mode debug..."
echo ""
echo "Port: $PORT"
echo "Profil: $PROFILE"
echo "URL debug: http://localhost:$PORT"
echo ""

# Ferme Chrome si déjà ouvert
osascript -e 'quit app "Google Chrome"' 2>/dev/null

# Attend que Chrome se ferme
sleep 2

# Lance Chrome avec remote debugging et profil spécifique
open -na "Google Chrome" --args \
  --remote-debugging-port=$PORT \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome" \
  --profile-directory="$PROFILE"

echo "✅ Chrome lancé avec remote debugging"
echo ""
echo "Tu peux maintenant:"
echo "1. Utiliser Chrome normalement (surfer, te connecter, etc.)"
echo "2. Lancer le bot: python bot.py"
echo "3. Le bot utilisera TON Chrome avec TOUTES tes sessions!"
echo ""
echo "Pour vérifier que ça marche:"
echo "  curl http://localhost:$PORT/json/version"
echo ""
echo "💡 Pour utiliser un autre profil:"
echo "  ./scripts/start_chrome_debug.sh 'Profile 1'"
echo "  ./scripts/start_chrome_debug.sh 'Profile 2'"

