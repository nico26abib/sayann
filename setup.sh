#!/bin/bash

echo "🚀 Setup Web Agent Discord Bot"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Install it first."
    exit 1
fi
echo "✓ Python $(python3 --version)"

# Check pip
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "❌ pip not found. Install it first."
    exit 1
fi
echo "✓ pip"

# Install deps
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Install Playwright
echo ""
echo "🌐 Installing Playwright..."
playwright install chromium

# Create .env if not exists
if [ ! -f .env ]; then
    echo ""
    echo "📝 Creating .env file..."
    cat > .env << EOF
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
EOF
    echo "✓ .env created"
    echo ""
    echo "⚠️  EDIT .env with your tokens!"
else
    echo ""
    echo "✓ .env already exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your tokens"
echo "   - Discord: https://discord.com/developers/applications"
echo "   - OpenAI: https://platform.openai.com/api-keys"
echo "2. Check config: python check_env.py"
echo "3. Run bot: python bot.py"

