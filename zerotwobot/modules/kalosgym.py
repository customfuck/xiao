import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/2f613d6ffbf88f38aec25.png"

@register(pattern=("/kalosgym"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
  TEXT += " **💥 GRAND SLAM CHAMPIONSHIP 💥** \n\n"
  TEXT += f"❍ ** RULES FOR KALOS GYM -:** \n\n"
  TEXT += f"❍ **4v4 battle OF 0L** \n\n"
  TEXT += f"❍ ** NO FOREFIT ... ONLY LEADER CAN** \n\n"
  TEXT += f"❍ ** BANNED POKE NONE👀** \n\n"
  TEXT += f"❍ ** DULPICATES BANNED** \n\n"
  TEXT += f"❍ ** 3 RETRY ALLOWED** \n\n"
  TEXT += f"❍ ** 4 SWITCHES FOR BOTH LEADER AND CHALLENGER** \n\n"
  TEXT += f"❍ ** BATTLE WILL BE FAIR.** \n\n"
  TEXT += f"❍ ** BOTH THE CHALLENGER AND LEADER MUST USE ONE STARTER OF KALOS.** \n\n"
  TEXT += f"❍ ** THE 0L FIRST APPEARANCE MUST BE KALOS(650 to 751). ** \n\n"
  TEXT += f"❍ ** NO MEGA** \n\n"
  TEXT += f"**U CAN ALSO USE /gen6 in @officerjennyprobot to see useable pokemon for KALOS gym**\n\n"
  TEXT += f"**PAY 90 PD TO GYM LEADER IF WON**\n\n"
  TEXT += "**   BEST OF LUCK   **"
  BUTTON = [[Button.url("KALOS GYM", "https://t.me/+sok9IlVLYfAyNGRl"), Button.url("LEADER", "https://t.me/unown_legend")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
