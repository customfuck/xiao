import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "tgm of ganyu mats"

@register(pattern=("/ganyu"))
async def awake(event):
  TEXT = f"**MATERIALS** \n\n"
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT)
