import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/45afbd569b576298c5fcf.jpg"

@register(pattern=("/unovagym"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
  TEXT += " **💥GRAND SLAM CHAMPIONSHIP💥** \n\n"
  TEXT += f"❍ ** RULES FOR UNOVA GYM -:** \n\n"
  TEXT += f"❍ **5V5 battle,  CAN USE MAXIMUM 1 LEGENDARY** \n\n"
  TEXT += f"❍ ** NO FORFEIT ALLOWED FOR CHALLENGERS. BUT LEADER CAN** \n\n"
  TEXT += f"❍ ** BANNED POKE - SLAKING, ARCEUS, GIRATINA, YVELTAL, PHERO** \n\n"
  TEXT += f"❍ ** DULPICATES BANNED** \n\n"
  TEXT += f"❍ ** 3 RETRY ALLOWED** \n\n"
  TEXT += f"❍ ** UNLIMITED SWITCH** \n\n"
  TEXT += f"❍ ** THE BATTLE MUST BE FAIR. LUCK ONLY IF LEADER SAY.** \n\n"
  TEXT += f"❍ ** CHALLENGERS MUST USE 4 UNOVA POKES** \n\n"
  TEXT += f"❍ ** GYM LEADER WILL BE USING 4 POKES OF UNOVA AND ONE OUTSIDE POKEMON** \n\n"
  TEXT += f"**U CAN ALSO USE /gen5 in @officerjennyprobot to see useable pokemon for UNOVA gym**\n\n"
  TEXT += f"**PAY 90 PD TO GYM LEADER IF WON**\n\n"
  TEXT += "**   BEST OF LUCK   **"
  BUTTON = [[Button.url("UNOVA GYM", "https://t.me/+YprmTp-3ytRmYjBl"), Button.url("LEADER", "https://t.me/KING_AMAN_1")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
