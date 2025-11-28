#!/bin/bash

# Liste les profils Chrome disponibles

CHROME_DIR="$HOME/Library/Application Support/Google/Chrome"

echo "📂 Profils Chrome disponibles:"
echo ""

if [ ! -d "$CHROME_DIR" ]; then
    echo "❌ Chrome data directory not found"
    exit 1
fi

cd "$CHROME_DIR"

# Profile par défaut
if [ -d "Default" ]; then
    echo "✅ Default (profil par défaut)"
fi

# Autres profils
for profile in Profile*; do
    if [ -d "$profile" ]; then
        # Cherche le nom du profil dans les prefs
        if [ -f "$profile/Preferences" ]; then
            name=$(grep -o '"name":"[^"]*"' "$profile/Preferences" | head -1 | cut -d'"' -f4)
            if [ -n "$name" ]; then
                echo "✅ $profile → $name"
            else
                echo "✅ $profile"
            fi
        else
            echo "✅ $profile"
        fi
    fi
done

echo ""
echo "💡 Pour utiliser un profil spécifique:"
echo "   ./scripts/start_chrome_debug.sh 'Default'"
echo "   ./scripts/start_chrome_debug.sh 'Profile 1'"
echo ""
echo "Ou dans .env:"
echo "   CHROME_PROFILE=Default"
echo "   CHROME_PROFILE='Profile 1'"

