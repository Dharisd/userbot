from datetime import datetime

import speedtest
from pyrogram import Filters, Message
from pyrogram.api import functions

from userbot import UserBot
from userbot.helpers.PyroHelpers import SpeedConvert
from userbot.helpers.constants import WWW
from userbot.helpers.expand import expand_url
from userbot.helpers.shorten import shorten_url
from userbot.plugins.help import add_command_help


@UserBot.on_message(Filters.command(["speed", 'speedtest'], ".") & Filters.me)
async def speed_test(bot: UserBot, message: Message):
    new_msg = await message.edit(
        "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n"
        "`Getting best server based on ping . . .`")
    spd.get_best_server()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n"
        "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n"
        "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n"
        "`Getting results and preparing formatting . . .`")
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results['timestamp'],
            ping=results['ping'],
            download=SpeedConvert(results['download']),
            upload=SpeedConvert(results['upload']),
            isp=results['client']['isp']
        ))


@UserBot.on_message(Filters.command("dc", ".") & Filters.me)
async def nearest_dc(bot: UserBot, message: Message):
    dc = await bot.send(
        functions.help.GetNearestDc())
    await message.edit(
        WWW.NearestDC.format(
            dc.country,
            dc.nearest_dc,
            dc.this_dc))


@UserBot.on_message(Filters.command("ping", ".") & Filters.me)
async def ping_me(bot: UserBot, message: Message):
    start = datetime.now()
    await message.edit('`Pong!`')
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{ms} ms`")


@UserBot.on_message(Filters.command("expand", ".") & Filters.me)
async def expand(bot: UserBot, message: Message):
    if message.reply_to_message:
        url = message.reply_to_message.text or message.reply_to_message.caption
    elif len(message.command) > 1:
        url = message.command[1]
    else:
        url = None

    if url:
        expanded = await expand_url(url)
        if expanded:
            await message.edit(
                f"<b>Shortened URL</b>: {url}\n<b>Expanded URL</b>: {expanded}", disable_web_page_preview = True
            )
        else:
            await message.edit(
                "No bro that's not what I do"
            )
    else:
        await message.edit("Nothing to expand")
        
@UserBot.on_message(Filters.command("shorten", ".") & Filters.me)
async def shorten(bot: UserBot, message: Message):
    if message.reply_to_message:
        msg = (message.reply_to_message.text or message.reply_to_message.caption).split(" ")
        if len(msg) > 0:
            url = msg[0]
            if len(msg) > 1:
                keyword = msg[1]
    elif len(message.command) > 1:
        url = message.command[1]
        if len(message.command) > 2:
            keyword = message.command[2]
        else:
            keyword = None
    else:
        url = None
        
    if url:
        shortened = shorten_url(url, keyword)
        if shortened == "API ERROR":
            message.edit("API URL or API KEY not found! Add YOURLS details to config")
        elif shortened == "INVALID URL":
            message.edit("Invalid URL")
        else:
            txt = f"<b>Original URL</b>:{url}\n<b>Shortened URL</b>:{shortened}"
            message.edit(txt)
    else:
        message.edit("Please provide a URL to shorten")
        
add_command_help(
    'www', [
        ['.ping', 'Calculates ping time between you and Telegram.'],
        ['.dc', 'Get\'s your Telegram DC.'],
        ['.speedtest `or` .speed', 'Runs a speedtest on the server this userbot is hosted.. Flex on them haters. With an in '
                       'Telegram Speedtest of your server..'],
        ['.expand', 'Expands a shortened url. Works for replied to message, photo caption or .expand url'],
        ['.shorten', 'Shortens a url. Works for replied to message, photo caption or .shorten url keyword']
    ]
)
