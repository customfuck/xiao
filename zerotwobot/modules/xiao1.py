import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/15be3dd814d66abd6ba92.jpg"
PHOTO = "https://telegra.ph/file/8e4f01cb34665ba49cb2d.jpg"

@register(pattern=("/xiao"))
async def awake(event):
  TEXT = f"**XIAO** \n\n"
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT)
