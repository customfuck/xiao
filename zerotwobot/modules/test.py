import html
import random
import time

import zerotwobot.modules.fun_strings as fun_strings
from zerotwobot import dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from zerotwobot.modules.helper_funcs.chat_status import is_user_admin
from zerotwobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext


def heizou(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "`Points         IV |  EV`\n`———————————————————————`\n`HP             24 | 252`\n`Attack         21 |  40`\n`Defense        16 |  30`\n`Sp. Attack     23 |   3`\n`Sp. Defense    25 |  31`\n`Speed          12 |  32`\n`———————————————————————`\n`Total         121 | 388`",
    )

def chichi(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "`Points         IV |  EV\n———————————————————————\nHP             24 | 252\nAttack         21 |  40\nDefense        16 |  30\nSp. Attack     23 |   3\nSp. Defense    25 |  31\nSpeed          12 |  32\n———————————————————————\nTotal         121 | 388`",
    )

HEIZOU_HANDLER = DisableAbleCommandHandler("heizou", heizou, run_async=True)
CHICHI_HANDLER = DisableAbleCommandHandler("chichi", chichi, run_async=True)

dispatcher.add_handler(HEIZOU_HANDLER)
dispatcher.add_handler(CHICHI_HANDLER)
