import discord
from openai import AsyncOpenAI
import aiohttp
import tempfile
import os
import config

class VoiceTool:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)
        
    async def transcribe_voice_message(self, attachment: discord.Attachment) -> str:
        """Transcribe Discord voice message using Whisper"""
        if not attachment.content_type or not attachment.content_type.startswith("audio"):
            return None
            
        # Download audio file
        async with aiohttp.ClientSession() as session:
            async with session.get(attachment.url) as resp:
                if resp.status != 200:
                    return None
                audio_data = await resp.read()
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as f:
            f.write(audio_data)
            temp_path = f.name
        
        try:
            # Transcribe with Whisper
            with open(temp_path, "rb") as audio_file:
                transcript = await self.client.audio.transcriptions.create(
                    model=config.WHISPER_MODEL,
                    file=audio_file,
                    language=config.WHISPER_LANGUAGE
                )
            return transcript.text
        finally:
            os.unlink(temp_path)

