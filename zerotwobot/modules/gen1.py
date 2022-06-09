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

def bluetext(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 1 POKEMONS\n\n🌟 Bulbasaur\n🌟 Ivysaur\n🌟 Venusaur\n🌟 Charmander\n🌟 Charmeleon\n🌟 Charizard\n🌟 Squirtle\n🌟 Wartortle\n🌟 Blastoise\n🌟 Caterpie\n🌟 Metapod\n🌟 Butterfree\n🌟 Weedle\n🌟 Kakuna\n🌟 Beedrill\n🌟 Pidgey\n🌟 Pidgeotto\n🌟 Pidgeot\n🌟 Rattata\n🌟 Raticate\n🌟 Spearow\n🌟 Fearow\n🌟 Ekans\n🌟 Arbok\n🌟 Pikachu\n🌟 Raichu\n🌟 Sandshrew\n🌟 Sandslash\n🌟 Nidoran♀\n🌟 Nidorina\n🌟 Nidoqueen\n🌟 Nidoran♂\n🌟 Nidorino\n🌟 Nidoking\n🌟 Clefairy\n🌟 Clefable\n🌟 Vulpix\n🌟 Ninetales\n🌟 Jigglypuff\n🌟 Wigglytuff\n🌟 Zubat\n🌟 Golbat\n🌟 Oddish\n🌟 Gloom\n🌟 Vileplume\n🌟 Paras\n🌟 Parasect\n🌟 Venonat\n🌟 Venomoth\n🌟 Diglett\n🌟 Dugtrio\n🌟 Meowth\n🌟 Persian\n🌟 Psyduck\n🌟 Golduck\n🌟 Mankey\n🌟 Primeape\n🌟 Growlithe\n🌟 Arcanine\n🌟 Poliwag\n🌟 Poliwhirl\n🌟 Poliwrath\n🌟 Abra\n🌟 Kadabra\n🌟 Alakazam\n🌟 Machop\n🌟 Machoke\n🌟 Machamp\n🌟 Bellsprout\n🌟 Weepinbell\n🌟 Victreebel\n🌟 Tentacool\n🌟 Tentacruel\n🌟 Geodude\n🌟 Graveler\n🌟 Golem\n🌟 Ponyta\n🌟 Rapidash\n🌟 Slowpoke\n🌟 Slowbro\n🌟 Magnemite\n🌟 Magneton\n🌟 Farfetch'd\n🌟 Doduo\n🌟 Dodrio\n🌟 Seel\n🌟 Dewgong\n🌟 Grimer\n🌟 Muk\n🌟 Shellder\n🌟 Cloyster\n🌟 Gastly\n🌟 Haunter\n🌟 Gengar\n🌟 Onix\n🌟 Drowzee\n🌟 Hypno\n🌟 Krabby\n🌟 Kingler\n🌟 Voltorb\n🌟 Electrode\n🌟 Exeggcute\n🌟 Exeggutor\n🌟 Cubone\n🌟 Marowak\n🌟 Hitmonlee\n🌟 Hitmonchan\n🌟 Lickitung\n🌟 Koffing\n🌟 Weezing\n🌟 Rhyhorn\n🌟 Rhydon\n🌟 Chansey\n🌟 Tangela\n🌟 Kangaskhan\n🌟 Horsea\n🌟 Seadra\n🌟 Goldeen\n🌟 Seaking\n🌟 Staryu\n🌟 Starmie\n🌟 Mr.\n🌟 Mime\n🌟 Scyther\n🌟 Jynx\n🌟 Electabuzz\n🌟 Magmar\n🌟 Pinsir\n🌟 Tauros\n🌟 Magikarp\n🌟 Gyarados\n🌟 Lapras\n🌟 Ditto\n🌟 Eevee\n🌟 Vaporeon\n🌟 Jolteon\n🌟 Flareon\n🌟 Porygon\n🌟 Omanyte\n🌟 Omastar\n🌟 Kabuto\n🌟 Kabutops\n🌟 Aerodactyl\n🌟 Snorlax\n🌟 Articuno\n🌟 Zapdos\n🌟 Moltres\n🌟 Dratini\n🌟 Dragonair\n🌟 Dragonite\n🌟 Mewtwo\n🌟 Mew",
    )
