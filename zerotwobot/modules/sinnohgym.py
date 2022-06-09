import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/5a7441155f7051f961e07.jpg"

@register(pattern=("/sinnohgym"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
  TEXT += " **💥 GRAND SLAM CHAMPIONSHIP 💥** \n\n"
  TEXT += f"❍ ** RULES FOR SINNOH GYM -:** \n\n"
  TEXT += f"❍ **4v4 battle,  OF 1 LEGENDARY AND 3-0L** \n\n"
  TEXT += f"❍ ** NO FOREFIT ... ONLY LEADER CAN** \n\n"
  TEXT += f"❍ ** BANNED POKE - GEN 3👀** \n\n"
  TEXT += f"❍ ** DULPICATES BANNED** \n\n"
  TEXT += f"❍ ** 3 RETRY ALLOWED** \n\n"
  TEXT += f"❍ ** UNLIMITED SWITCH** \n\n"
  TEXT += f"❍ ** BATTLE WILL BE FAIR. LUCK ONLY IF LEADER SAYS** \n\n"
  TEXT += f"❍ ** CHALLENGERS MUST USE POKES FOUND IN HOENN, KANTO, UNOVA, SINNOH POKES ** \n\n"
  TEXT += f"❍ ** GYM LEADER WILL USE 3 SINNOH POKES AND ONE OTHER GEN POKE** \n\n"
  TEXT += f"**U CAN ALSO USE /gen1, /gen3, /gen4, /gen5 in @officerjennyprobot to see useable pokemon for hoenn gym**\n\n"
  TEXT += f"**PAY 90 PD TO GYM LEADER IF WON**\n\n"
  TEXT += "**   BEST OF LUCK   **"
  BUTTON = [[Button.url("SINNOH GYM", "https://t.me/+LMdJxC_2AoIzODE1"), Button.url("LEADER", "https://t.me/kaustubh_kurosaki")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
