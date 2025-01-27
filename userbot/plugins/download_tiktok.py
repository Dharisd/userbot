import asyncio

import aiohttp
from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.plugins.help import add_command_help
from userbot.helpers.tiktokHelper import TikTok
import os



@UserBot.on_message(filters.command("t", ".") & filters.me)
async def download_tiktok(_, message: Message):


    try:

        if message.reply_to_message:
            txt = message.reply_to_message.text or message.reply_to_message.caption
        elif len(message.command) > 1:
            txt = " ".join(message.command[1:])
        else:
            await message.edit("TikTok link not found")
            await asyncio.sleep(3)
            await message.delete()
            return

        try:
            await message.edit("Processing link...")
            tiktok_video = await TikTok.download_tiktok(txt)
            await message.reply_video(tiktok_video)
            await message.delete()
            os.remove(tiktok_video)
            return 
    
        except Exception as e:
            print(f"{e}")
            await message.edit("Error while processing tiktok link")
            await asyncio.sleep(3)
            await message.delete()
            await message.delete()
            return 

    except Exception as e:
        await message.edit("`Failed to download video`")
        await asyncio.sleep(2)
        await message.delete()




add_command_help(
    "Tiktok",
    [[".t ", "given a link to a tiktok video"]],
)
