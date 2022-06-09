import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/472763617f15cd1146011.jpg"

@register(pattern=("/hoenngym"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id})** \n\n"
  TEXT += " **💥GRAND SLAM CHAMPIONSHIP💥** \n\n"
  TEXT += f"❍ ** RULES FOR HOENN GYM -:** \n\n"
  TEXT += f"❍ **5V5 battle,  CAN USE MAXIMUM 2 LEGENDARY OF HOENN** \n\n"
  TEXT += f"❍ ** 1 FORFIET ALLOWDED ONLY** \n\n"
  TEXT += f"❍ ** BANNED POKE - SLAKING, DEOXYS** \n\n"
  TEXT += f"❍ ** DULPICATES BANNED** \n\n"
  TEXT += f"❍ ** 3 RETRY ALLOWED** \n\n"
  TEXT += f"❍ ** UNLIMITED SWITCH** \n\n"
  TEXT += f"❍ ** LUCK OR FAIR WILL BE DECIDED AT BATTLE TIME** \n\n"
  TEXT += f"❍ ** CHALLENGERS MUST USE HOENN POKES** \n\n"
  TEXT += f"❍ ** GYM LEADER WILL USE HOENN POKES** \n\n"
  TEXT += "**PAY 90 PD TO GYM LEADER IF WON**"
  BUTTON = [[Button.url("HOENN GYM", "https://t.me/+dGqBAKOTu101Yjdl"), Button.url("LEADER", "https://t.me/Lucarioaurra")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
