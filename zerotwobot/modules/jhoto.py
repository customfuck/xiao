import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/4c3af8adfbd377e353baf.jpg"

@register(pattern=("/jhotogym"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
  TEXT += " **💥 GRAND SLAM CHAMPIONSHIP 💥** \n\n"
  TEXT += f"❍ ** RULES FOR JHOTO GYM -:** \n\n"
  TEXT += f"❍ **4V4 battle,  CAN USE 1 LEGENDARY** \n\n"
  TEXT += f"❍ ** NO FORFEIT ALLOWED (DEPENDS ON LEADER)** \n\n"
  TEXT += f"❍ ** BANNED POKE - NOTHING👀** \n\n"
  TEXT += f"❍ ** DULPICATES BANNED** \n\n"
  TEXT += f"❍ ** 3 RETRY ALLOWED** \n\n"
  TEXT += f"❍ ** 3 SWITCH ALLOWED FOR LEADER AND CHALLENGER** \n\n"
  TEXT += f"❍ ** BATTLE WILL BE FAIR (MAYBE LUCK IF LEADER SAYS)** \n\n"
  TEXT += f"❍ ** CHALLENGERS MUST USE JHOTO POKES ( 0LS )** \n\n"
  TEXT += f"❍ ** GYM LEADER WILL USE JHOTO POKES** \n\n"
  TEXT += "**PAY 90 PD TO GYM LEADER IF WON**"
  BUTTON = [[Button.url("JHOTO GYM", "https://t.me/killers69"), Button.url("LEADER", "https://t.me/Oo_ShInChAn")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
