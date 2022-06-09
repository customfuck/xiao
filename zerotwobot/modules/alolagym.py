import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/d558de48f52303c59a3e5.jpg"

@register(pattern=("/alolagym"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
  TEXT += " **💥 GRAND SLAM CHAMPIONSHIP 💥** \n\n"
  TEXT += f"❍ ** RULES FOR ALOLAN GYM -:** \n\n"
  TEXT += f"❍ **4v4 battle. CHALLENGER SHOULD USE ONE POKE OF  ALOLA. ie:- 1 6l and one 0l from alola only allowed for challangers to have in their TEAMS.** \n\n"
  TEXT += f"❍ ** NO FOREFIT ... ONLY LEADER CAN** \n\n"
  TEXT += f"❍ ** BANNED POKE - Deo ( all form), Dialga, Giratina** \n\n"
  TEXT += f"❍ ** DULPICATES BANNED** \n\n"
  TEXT += f"❍ ** 3 RETRY ALLOWED** \n\n"
  TEXT += f"❍ ** BOTH THE CHALLENGER AND LEADER HAS INFINITE SWITCHES BUT SIMUTANEOUSLY ONLY 3 SWITCH ALLOWED** \n\n"
  TEXT += f"❍ ** BATTLE WILL BE FAIR. ** \n\n"
  TEXT += f"❍ ** MEGA ALLOWED ONLY FOR 0l POKE WHOSE BASE SPEED IS LESS THEN OR EQUAL TO 110.** \n\n"
  TEXT += f"**U CAN ALSO USE /gen7 in @officerjennyprobot to see useable pokemon for Alola gym**\n\n"
  TEXT += f"**PAY 90 PD TO GYM LEADER IF WON**\n\n"
  TEXT += "**   BEST OF LUCK   **"
  BUTTON = [[Button.url("SINNOH GYM", "https://t.me/+xduN0pdmIT4yNjRl"), Button.url("LEADER", "https://t.me/nothing_here_get_lost")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
