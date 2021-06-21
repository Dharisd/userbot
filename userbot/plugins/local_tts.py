import asyncio

import aiohttp
from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.plugins.help import add_command_help
from userbot.helpers.ttsHelper import ttsHelper
import soundfile as sf 
import os

#tts = ttsHelper()


@UserBot.on_message(filters.command("tts", ".") & filters.me)
async def do_tts(_, message: Message):
    if message.reply_to_message:
        txt = message.reply_to_message.text or message.reply_to_message.caption
    elif len(message.command) > 1:
        txt = " ".join(message.command[1:])
    else:
        await message.edit("Nothing to speak")
        await asyncio.sleep(3)
        await message.delete()
        return

    wav_data = tts.do_tts(txt)
    sf.write("temp.wav", output_wav.astype('int16'), 22050, 'PCM_16')
    message.reply_audio("temp.wav")
    os.remove("temp.wav")



add_command_help(
    "text to speech",
    [[".tts ", "speak given dhivehi text"]],
)
