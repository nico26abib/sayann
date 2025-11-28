import discord
from discord.ext import commands
from agents.web_agent import WebAgent
from tools.browser import browser_tool
from tools.voice import VoiceTool
from utils.logger import setup_logger
import config

logger = setup_logger()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix=config.COMMAND_PREFIX, intents=intents)
agent = WebAgent(api_key=config.OPENAI_API_KEY)
voice_tool = VoiceTool(api_key=config.OPENAI_API_KEY)

@bot.event
async def on_ready():
    await browser_tool.start()
    logger.info(f"✓ {bot.user.name} ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    if message.content.startswith("!"):
        await bot.process_commands(message)
        return
    
    # Check for voice attachments
    query = message.content.replace(f"<@{bot.user.id}>", "").strip()
    
    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type and attachment.content_type.startswith("audio"):
                async with message.channel.typing():
                    transcribed = await voice_tool.transcribe_voice_message(attachment)
                    if transcribed:
                        query = transcribed
                        logger.info(f"Transcribed: {transcribed[:50]}...")
                        await message.channel.send(f"🎤 *{transcribed}*")
                break
    
    # Process any message as a query
    if isinstance(message.channel, discord.DMChannel) or bot.user.mentioned_in(message) or message.attachments:
        if not query:
            return
            
        async with message.channel.typing():
            try:
                logger.info(f"Query from {message.author}: {query[:100]}...")
                result = await agent.process_query(query)
                logger.info(f"Response: {result[:100]}...")
                
                # Split long messages
                if len(result) > config.MAX_RESPONSE_LENGTH:
                    chunks = [result[i:i+config.MAX_RESPONSE_LENGTH] for i in range(0, len(result), config.MAX_RESPONSE_LENGTH)]
                    for chunk in chunks:
                        await message.reply(chunk)
                else:
                    await message.reply(result)
                    
            except Exception as e:
                logger.error(f"Error: {e}", exc_info=True)
                await message.reply(f"Erreur: {str(e)}")

@bot.command(name="search")
async def search_command(ctx, *, query: str):
    """Recherche une info sur le web"""
    async with ctx.typing():
        try:
            result = await agent.process_query(query)
            await ctx.reply(result)
        except Exception as e:
            await ctx.reply(f"Erreur: {str(e)}")

@bot.event
async def on_close():
    await browser_tool.stop()

if __name__ == "__main__":
    bot.run(config.DISCORD_TOKEN)

