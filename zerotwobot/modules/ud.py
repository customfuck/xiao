import requests
from zerotwobot import dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext


def data(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/ud ") :]
    results = requests.get(
        f"https://pokemondb.net/pokedex/{text}",
    ).json()
    try:
        reply_text = f'*{text}*\n\n{results["BASE STATS"][0]["Moves learnt and Tms"]}\n\n_{results["BASE STATS"][0]["Moves learnt and base"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


DATA_HANDLER = DisableAbleCommandHandler(["data"], data, run_async=True)

dispatcher.add_handler(Data_HANDLER)

__command_list__ = ["ud"]
__handlers__ = [DATA_HANDLER]
