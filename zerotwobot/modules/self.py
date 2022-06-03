import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "yaha jo image dalna ho daal dena tgm form mr"

@register(pattern=("/yahahandlerdalna"))
async def awake(event):
  TEXT = f"**YAHA jo likhna likh dena** \n\n"
  TEXT += "❍ **yaha bhi** \n\n"
  TEXT += f"❍ **yaha bhi** \n\n"
  TEXT += f"❍ **yaha bhi \n\n"
  TEXT += f"❍ **yahabhi \n\n"
  TEXT += f"❍ **yaha bhi \n\n"
  TEXT += "**yaha bhi ❤️**"
  BUTTON = [[Button.url(" CO OWNER", "https://t.me/yuitosan"), Button.url("OWNER", "https://t.me/SILVER_KING")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
