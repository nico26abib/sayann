#!/bin/bash

# Lance Chrome avec le profil "Perso" spécifiquement

echo "🚀 Lancement de Chrome avec le profil 'Perso'..."

# Cherche le profil qui s'appelle "Perso"
CHROME_DIR="$HOME/Library/Application Support/Google/Chrome"
PROFILE_DIR=""

# Cherche dans tous les profils
for profile in "$CHROME_DIR"/Profile*; do
    if [ -f "$profile/Preferences" ]; then
        name=$(grep -o '"name":"[^"]*"' "$profile/Preferences" | head -1 | cut -d'"' -f4)
        if [ "$name" = "Perso" ] || [ "$name" = "perso" ]; then
            PROFILE_DIR=$(basename "$profile")
            echo "✅ Profil 'Perso' trouvé: $PROFILE_DIR"
            break
        fi
    fi
done

# Si pas trouvé dans Profile*, essaie Default
if [ -z "$PROFILE_DIR" ]; then
    if [ -f "$CHROME_DIR/Default/Preferences" ]; then
        name=$(grep -o '"name":"[^"]*"' "$CHROME_DIR/Default/Preferences" | head -1 | cut -d'"' -f4)
        if [ "$name" = "Perso" ] || [ "$name" = "perso" ]; then
            PROFILE_DIR="Default"
            echo "✅ Profil 'Perso' trouvé: Default"
        fi
    fi
fi

if [ -z "$PROFILE_DIR" ]; then
    echo "❌ Profil 'Perso' non trouvé"
    echo ""
    echo "📋 Profils disponibles:"
    ./scripts/find_chrome_profiles.sh
    exit 1
fi

# Lance Chrome avec ce profil
PORT=9222

echo "🔧 Configuration:"
echo "   Profil: $PROFILE_DIR"
echo "   Port: $PORT"
echo ""

# Ferme Chrome
osascript -e 'quit app "Google Chrome"' 2>/dev/null
sleep 2

# Lance avec le bon profil
open -na "Google Chrome" --args \
  --remote-debugging-port=$PORT \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome" \
  --profile-directory="$PROFILE_DIR"

echo "✅ Chrome lancé avec le profil 'Perso'"
echo ""
echo "Test: curl http://localhost:$PORT/json/version"

