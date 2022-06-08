import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/cbaf3bd068b2612689ef8.png"

@register(pattern=("/kantogym"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
  TEXT += " **💥 GRAND SLAM CHAMPIONSHIP 💥** \n\n"
  TEXT += f"❍ ** RULES FOR KANTO GYM -:** \n\n"
  TEXT += f"❍ **5v5 battle,  USE  0ls ( no legendaries )** \n\n"
  TEXT += f"❍ ** 1 FORFIET ALLOWDED ONLY** \n\n"
  TEXT += f"❍ ** BANNED POKE - NOTHING👀** \n\n"
  TEXT += f"❍ ** DULPICATES BANNED** \n\n"
  TEXT += f"❍ ** 3 RETRY ALLOWED** \n\n"
  TEXT += f"❍ ** UNLIMITED SWITCH** \n\n"
  TEXT += f"❍ ** DECIDE FAIR OR LUCK AT BATTLE TYM** \n\n"
  TEXT += f"❍ ** CHALLENGERS MUST USE ALL KANTO POKES ( 0LS )** \n\n"
  TEXT += f"❍ ** GYM LEADER WILL USE ALL KANTO POKES** \n\n"
  TEXT += "**PAY 90 PD TO GYM LEADER IF WON**"
  BUTTON = [[Button.url("KANTO GYM", "https://t.me/+1FynhMswVcBmNTU1"), Button.url("LEADER", "https://t.me/kaustubh_kurosaki")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON
