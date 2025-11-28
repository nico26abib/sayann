#!/bin/bash
echo "🔄 Redémarrage du bot Sayann..."
pkill -f "python bot.py" 2>/dev/null
sleep 2
python bot.py &
echo "✅ Bot redémarré"
