import asyncio

from pyrogram import filters
from pyrogram.types import Message

from userbot import UserBot, ALLOWED_USERS
from userbot.plugins.help import add_command_help
from userbot.helpers.sttHelpers import sttHelper


stt_helper = sttHelper()

@UserBot.on_message(
    filters.command(["stt", "stt"], ".") & (filters.me | filters.user(ALLOWED_USERS))
)
async def send_stt(_, message: Message,stt_helper=stt_helper):
    try:
        cmd = message.command

        #taken to add support for dhivehi later
        input_string = ""
        if len(cmd) > 1:
            input_string = " ".join(cmd[1:])

        #use english model unless specified
        if message.reply_to_message:
            #check if the message media type is audio:
            if message.reply_to_message.voice:
                #download the file
                filename = await UserBot.download_media(message.reply_to_message.voice)
                print(filename)
                await message.edit("Processing..")

                if len(cmd) == 1:
                    stt_text = stt_helper.do_stt(filename)
                if len(cmd) == 2 and cmd[1] == "dv":
                    stt_text = stt_helper.do_stt(filename,"dv")

                await message.edit(stt_text)


        elif not message.reply_to_message:
            await message.edit("Not a reply to an audio")
            await asyncio.sleep(2)
            await message.delete()
            return 
        


    except Exception as e:
        print(e)
        await message.edit("`Failed to do stt`")
        await asyncio.sleep(2)
        await message.delete()


# Command help section
add_command_help("stt", [[".stt `or` .speechtotext", "Perform speech to text on voice message"]])
