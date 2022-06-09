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

def gen1(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 1 POKEMONS\n\n🌟 Bulbasaur\n🌟 Ivysaur\n🌟 Venusaur\n🌟 Charmander\n🌟 Charmeleon\n🌟 Charizard\n🌟 Squirtle\n🌟 Wartortle\n🌟 Blastoise\n🌟 Caterpie\n🌟 Metapod\n🌟 Butterfree\n🌟 Weedle\n🌟 Kakuna\n🌟 Beedrill\n🌟 Pidgey\n🌟 Pidgeotto\n🌟 Pidgeot\n🌟 Rattata\n🌟 Raticate\n🌟 Spearow\n🌟 Fearow\n🌟 Ekans\n🌟 Arbok\n🌟 Pikachu\n🌟 Raichu\n🌟 Sandshrew\n🌟 Sandslash\n🌟 Nidoran♀\n🌟 Nidorina\n🌟 Nidoqueen\n🌟 Nidoran♂\n🌟 Nidorino\n🌟 Nidoking\n🌟 Clefairy\n🌟 Clefable\n🌟 Vulpix\n🌟 Ninetales\n🌟 Jigglypuff\n🌟 Wigglytuff\n🌟 Zubat\n🌟 Golbat\n🌟 Oddish\n🌟 Gloom\n🌟 Vileplume\n🌟 Paras\n🌟 Parasect\n🌟 Venonat\n🌟 Venomoth\n🌟 Diglett\n🌟 Dugtrio\n🌟 Meowth\n🌟 Persian\n🌟 Psyduck\n🌟 Golduck\n🌟 Mankey\n🌟 Primeape\n🌟 Growlithe\n🌟 Arcanine\n🌟 Poliwag\n🌟 Poliwhirl\n🌟 Poliwrath\n🌟 Abra\n🌟 Kadabra\n🌟 Alakazam\n🌟 Machop\n🌟 Machoke\n🌟 Machamp\n🌟 Bellsprout\n🌟 Weepinbell\n🌟 Victreebel\n🌟 Tentacool\n🌟 Tentacruel\n🌟 Geodude\n🌟 Graveler\n🌟 Golem\n🌟 Ponyta\n🌟 Rapidash\n🌟 Slowpoke\n🌟 Slowbro\n🌟 Magnemite\n🌟 Magneton\n🌟 Farfetch'd\n🌟 Doduo\n🌟 Dodrio\n🌟 Seel\n🌟 Dewgong\n🌟 Grimer\n🌟 Muk\n🌟 Shellder\n🌟 Cloyster\n🌟 Gastly\n🌟 Haunter\n🌟 Gengar\n🌟 Onix\n🌟 Drowzee\n🌟 Hypno\n🌟 Krabby\n🌟 Kingler\n🌟 Voltorb\n🌟 Electrode\n🌟 Exeggcute\n🌟 Exeggutor\n🌟 Cubone\n🌟 Marowak\n🌟 Hitmonlee\n🌟 Hitmonchan\n🌟 Lickitung\n🌟 Koffing\n🌟 Weezing\n🌟 Rhyhorn\n🌟 Rhydon\n🌟 Chansey\n🌟 Tangela\n🌟 Kangaskhan\n🌟 Horsea\n🌟 Seadra\n🌟 Goldeen\n🌟 Seaking\n🌟 Staryu\n🌟 Starmie\n🌟 Mr.Mime\n🌟 Scyther\n🌟 Jynx\n🌟 Electabuzz\n🌟 Magmar\n🌟 Pinsir\n🌟 Tauros\n🌟 Magikarp\n🌟 Gyarados\n🌟 Lapras\n🌟 Ditto\n🌟 Eevee\n🌟 Vaporeon\n🌟 Jolteon\n🌟 Flareon\n🌟 Porygon\n🌟 Omanyte\n🌟 Omastar\n🌟 Kabuto\n🌟 Kabutops\n🌟 Aerodactyl\n🌟 Snorlax\n🌟 Articuno\n🌟 Zapdos\n🌟 Moltres\n🌟 Dratini\n🌟 Dragonair\n🌟 Dragonite\n🌟 Mewtwo\n🌟 Mew",
    )

def gen2(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 2 POKEMONS\n\n🌟 Chikorita\n🌟 Bayleef\n🌟 Meganium\n🌟 Cyndaquil\n🌟 Quilava\n🌟 Typhlosion\n🌟 Totodile\n🌟 Croconaw\n🌟 Feraligatr\n🌟 Sentret\n🌟 Furret\n🌟 Hoothoot\n🌟 Noctowl\n🌟 Ledyba\n🌟 Ledian\n🌟 Spinarak\n🌟 Ariados\n🌟 Crobat\n🌟 Chinchou\n🌟 Lanturn\n🌟 Pichu\n🌟 Cleffa\n🌟 Igglybuff\n🌟 Togepi\n🌟 Togetic\n🌟 Natu\n🌟 Xatu\n🌟 Mareep\n🌟 Flaaffy\n🌟 Ampharos\n🌟 Bellossom\n🌟 Marill\n🌟 Azumarill\n🌟 Sudowoodo\n🌟 Politoed\n🌟 Hoppip\n🌟 Skiploom\n🌟 Jumpluff\n🌟 Aipom\n🌟 Sunkern\n🌟 Sunflora\n🌟 Yanma\n🌟 Wooper\n🌟 Quagsire\n🌟 Espeon\n🌟 Umbreon\n🌟 Murkrow\n🌟 Slowking\n🌟 Misdreavus\n🌟 Unown\n🌟 Wobbuffet\n🌟 Girafarig\n🌟 Pineco\n🌟 Forretress\n🌟 Dunsparce\n🌟 Gligar\n🌟 Steelix\n🌟 Snubbull\n🌟 Granbull\n🌟 Qwilfish\n🌟 Scizor\n🌟 Shuckle\n🌟 Heracross\n🌟 Sneasel\n🌟 Teddiursa\n🌟 Ursaring\n🌟 Slugma\n🌟 Magcargo\n🌟 Swinub\n🌟 Piloswine\n🌟 Corsola\n🌟 Remoraid\n🌟 Octillery\n🌟 Delibird\n🌟 Mantine\n🌟 Skarmory\n🌟 Houndour\n🌟 Houndoom\n🌟 Kingdra\n🌟 Phanpy\n🌟 Donphan\n🌟 Porygon2\n🌟 Stantler\n🌟 Smeargle\n🌟 Tyrogue\n🌟 Hitmontop\n🌟 Smoochum\n🌟 Elekid\n🌟 Magby\n🌟 Miltank\n🌟 Blissey\n🌟 Raikou\n🌟 Entei\n🌟 Suicune\n🌟 Larvitar\n🌟 Pupitar\n🌟 Tyranitar\n🌟 Lugia\n🌟 Ho-Oh\n🌟 Celebi",
    )
    
def gen3(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 3 POKEMONS\n\n🌟 Treecko\n🌟 Grovyle\n🌟 Sceptile\n🌟 Torchic\n🌟 Combusken\n🌟 Blaziken\n🌟 Mudkip\n🌟 Marshtomp\n🌟 Swampert\n🌟 Poochyena\n🌟 Mightyena\n🌟 Zigzagoon\n🌟 Linoone\n🌟 Wurmple\n🌟 Silcoon\n🌟 Beautifly\n🌟 Cascoon\n🌟 Dustox\n🌟 Lotad\n🌟 Lombre\n🌟 Ludicolo\n🌟 Seedot\n🌟 Nuzleaf\n🌟 Shiftry\n🌟 Taillow\n🌟 Swellow\n🌟 Wingull\n🌟 Pelipper\n🌟 Ralts\n🌟 Kirlia\n🌟 Gardevoir\n🌟 Surskit\n🌟 Masquerain\n🌟 Shroomish\n🌟 Breloom\n🌟 Slakoth\n🌟 Vigoroth\n🌟 Slaking\n🌟 Nincada\n🌟 Ninjask\n🌟 Shedinja\n🌟 Whismur\n🌟 Loudred\n🌟 Exploud\n🌟 Makuhita\n🌟 Hariyama\n🌟 Azurill\n🌟 Nosepass\n🌟 Skitty\n🌟 Delcatty\n🌟 Sableye\n🌟 Mawile\n🌟 Aron\n🌟 Lairon\n🌟 Aggron\n🌟 Meditite\n🌟 Medicham\n🌟 Electrike\n🌟 Manectric\n🌟 Plusle\n🌟 Minun\n🌟 Volbeat\n🌟 Illumise\n🌟 Roselia\n🌟 Gulpin\n🌟 Swalot\n🌟 Carvanha\n🌟 Sharpedo\n🌟 Wailmer\n🌟 Wailord\n🌟 Numel\n🌟 Camerupt\n🌟 Torkoal\n🌟 Spoink\n🌟 Grumpig\n🌟 Spinda\n🌟 Trapinch\n🌟 Vibrava\n🌟 Flygon\n🌟 Cacnea\n🌟 Cacturne\n🌟 Swablu\n🌟 Altaria\n🌟 Zangoose\n🌟 Seviper\n🌟 Lunatone\n🌟 Solrock\n🌟 Barboach\n🌟 Whiscash\n🌟 Corphish\n🌟 Crawdaught\n🌟 Baltoy\n🌟 Claydol\n🌟 Lileep\n🌟 Cradily\n🌟 Anorith\n🌟 Armaldo\n🌟 Feebas\n🌟 Milotic\n🌟 Castform\n🌟 Kecleon\n🌟 Shuppet\n🌟 Banette\n🌟 Duskull\n🌟 Dusclops\n🌟 Tropius\n🌟 Chimecho\n🌟 Absol\n🌟 Wynaut\n🌟 Snorunt\n🌟 Glalie\n🌟 Spheal\n🌟 Sealeo\n🌟 Walrein\n🌟 Clamperl\n🌟 Huntail\n🌟 Gorebyss\n🌟 Relicanth\n🌟 Luvdisc\n🌟 Bagon\n🌟 Shelgon\n🌟 Salamence\n🌟 Beldum\n🌟 Metang\n🌟 Metagross\n🌟 Regirock\n🌟 Regice\n🌟 Registeel\n🌟 Latias\n🌟 Latios\n🌟 Kyogre\n🌟 Groudon\n🌟 Rayquaza\n🌟 Jirachu\n🌟 Deoxys ",
    )
    
def gen4(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 4 POKEMONS\n\n🌟 Turtwig\n🌟 Grotle\n🌟 Torterra\n🌟 Chimchar\n🌟 Monferno\n🌟 Infernape\n🌟 Piplup\n🌟 Prinplup\n🌟 Empoleon\n🌟 Starly\n🌟 Staravia\n🌟 Staraptor\n🌟 Bidoof\n🌟 Bibarel\n🌟 Kricketot\n🌟 Kricketune\n🌟 Shinx\n🌟 Luxio\n🌟 Luxray\n🌟 Budew\n🌟 Roserade\n🌟 Cranidos\n🌟 Rampardos\n🌟 Shieldon\n🌟 Bastiodon\n🌟 Burmy\n🌟 Wormadam\n🌟 Mothim\n🌟 Combee\n🌟 Vespiquen\n🌟 Pachirisu\n🌟 Buizel\n🌟 Floatzel\n🌟 Cherubi\n🌟 Cherrim\n🌟 Shellos\n🌟 Gastrodon\n🌟 Ambipom\n🌟 Drifloon\n🌟 Drifblim\n🌟 Buneary\n🌟 Lopunny\n🌟 Mismagius\n🌟 Honchkrow\n🌟 Glameow\n🌟 Purugly\n🌟 Chingling\n🌟 Stunky\n🌟 Skuntank\n🌟 Bronzor\n🌟 Bronzong\n🌟 Bonsly\n🌟 MimeJr.\n🌟 Happiny\n🌟 Chatot\n🌟 Spiritomb\n🌟 Gible\n🌟 Gabite\n🌟 Garchomp\n🌟 Munchlax\n🌟 Riolu\n🌟 Lucario\n🌟 Hippopotas\n🌟 Hippowdon\n🌟 Skorupi\n🌟 Drapion\n🌟 Croagunk\n🌟 Toxicroak\n🌟 Carnivine\n🌟 Finneon\n🌟 Lumineon\n🌟 Mantyke\n🌟 Snover\n🌟 Abomasnow\n🌟 Weavile\n🌟 Magnezone\n🌟 Lickilicky\n🌟 Rhyperior\n🌟 Tangrowth\n🌟 Electivire\n🌟 Magmortar\n🌟 Togekiss\n🌟 Yanmega\n🌟 Leafeon\n🌟 Glaceon\n🌟 Gliscor\n🌟 Mamoswine\n🌟 Porygon-Z\n🌟 Gallade\n🌟 Probopass\n🌟 Dusknoir\n🌟 Froslass\n🌟 Rotom\n🌟 Uxie\n🌟 Mesprit\n🌟 Azelf\n🌟 Dialga\n🌟 Palkia\n🌟 Heatran\n🌟 Regigigas\n🌟 Giratina\n🌟 Cresselia\n🌟 Phione\n🌟 Manaphy\n🌟 Darkrai\n🌟 Shaymin\n🌟 Arceus",
    )
    
def gen5(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 5 POKEMONS\n\n🌟Victini\n🌟 Snivy\n🌟 Servine\n🌟 Serperior\n🌟 Tepig\n🌟 Pignite\n🌟 Emboar\n🌟 Oshawott\n🌟 Dewott\n🌟 Samurott\n🌟 Patrat\n🌟 Watchog\n🌟 Lillipup\n🌟 Herdier\n🌟 Stoutland\n🌟 Purrloin\n🌟 Liepard\n🌟 Pansage\n🌟 Simisage\n🌟 Pansear\n🌟 Simisear\n🌟 Panpour\n🌟 Simipour\n🌟 Munna\n🌟 Musharna\n🌟 Pidove\n🌟 Tranquill\n🌟 Unfezant\n🌟 Blitzle\n🌟 Zebstrika\n🌟 Roggenrola\n🌟 Boldore\n🌟 Gigalith\n🌟 Woobat\n🌟 Swoobat\n🌟 Drilbur\n🌟 Excadrill\n🌟 Audino\n🌟 Timburr\n🌟 Gurdurr\n🌟 Conkeldurr\n🌟 Tympole\n🌟 Palpitoad\n🌟 Seismitoad\n🌟 Throh\n🌟 Sawk\n🌟 Sewaddle\n🌟 Swadloon\n🌟 Leavanny\n🌟 Venipede\n🌟 Whirlipede\n🌟 Scolipede\n🌟 Cottonee\n🌟 Whimsicott\n🌟 Petilil\n🌟 Lilligant\n🌟 Basculin\n🌟 Sandile\n🌟 Krokorok\n🌟 Krookodile\n🌟 Darumaka\n🌟 Darmanitan\n🌟 Maractus\n🌟 Dwebble\n🌟 Crustle\n🌟 Scraggy\n🌟 Scrafty\n🌟 Sigilyph\n🌟 Yamask\n🌟 Cofagrigus\n🌟 Tirtouga\n🌟 Carracosta\n🌟 Archen\n🌟 Archeops\n🌟 Trubbish\n🌟 Garbodor\n🌟 Zorua\n🌟 Zoroark\n🌟 Minccino\n🌟 Cinccino\n🌟 Gothita\n🌟 Gothorita\n🌟 Gothitelle\n🌟 Solosis\n🌟 Duosion\n🌟 Reuniclus\n🌟 Ducklett\n🌟 Swanna\n🌟 Vanillite\n🌟 Vanillish\n🌟 Vanilluxe\n🌟 Deerling\n🌟 Sawsbuck\n🌟 Emolga\n🌟 Karrablast\n🌟 Escavalier\n🌟 Foongus\n🌟 Amoonguss\n🌟 Frillish\n🌟 Jellicent\n🌟 Alomomola\n🌟 Joltik\n🌟 Galvantula\n🌟 Ferroseed\n🌟 Ferrothorn\n🌟 Klink\n🌟 Klang\n🌟 Klinklang\n🌟 Tynamo\n🌟 Eelektrik\n🌟 Eelektross\n🌟 Elgyem\n🌟 Beheeyem\n🌟 Litwick\n🌟 Lampent\n🌟 Chandelure\n🌟 Axew\n🌟 Fraxure\n🌟 Haxorus\n🌟 Cubchoo\n🌟 Beartic\n🌟 Cryogonal\n🌟 Shelmet\n🌟 Accelgor\n🌟 Stunfisk\n🌟 Mienfoo\n🌟 Mienshao\n🌟 Druddigon\n🌟 Golett\n🌟 Golurk\n🌟 Pawniard\n🌟 Bisharp\n🌟 Bouffalant\n🌟 Rufflet\n🌟 Braviary\n🌟 Vullaby\n🌟 Mandibuzz\n🌟 Heatmor\n🌟 Durant\n🌟 Deino\n🌟 Zweilous\n🌟 Hydreigon\n🌟 Larvesta\n🌟 Volcarona\n🌟 Cobalion\n🌟 Terrakion\n🌟 Virizion\n🌟 Tornadus\n🌟 Thundurus\n🌟 Reshiram\n🌟 Zekrom\n🌟 Landorus\n🌟 Kyurem\n🌟 Keldeo\n🌟 Meloetta\n🌟 Genesect",
    )
    
def gen6(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 6 POKEMONS\n\n🌟Chespin\n🌟 Quilladin\n🌟 Chesnaught\n🌟 Fennekin\n🌟 Braixen\n🌟 Delphox\n🌟 Froakie\n🌟 Frogadier\n🌟 Greninja\n🌟 Bunnelby\n🌟 Diggersby\n🌟 Fletchling\n🌟 Fletchinder\n🌟 Talonflame\n🌟 Scatterbug\n🌟 Spewpa\n🌟 Vivillon\n🌟 Litleo\n🌟 Pyroar\n🌟 Flabébé\n🌟 Floette\n🌟 Florges\n🌟 Skiddo\n🌟 Gogoat\n🌟 Pancham\n🌟 Pangoro\n🌟 Furfrou\n🌟 Espurr\n🌟 Meowstic\n🌟 Honedge\n🌟 Doublade\n🌟 Aegislash\n🌟 Spritzee\n🌟 Aromatisse\n🌟 Swirlix\n🌟 Slurpuff\n🌟 Inkay\n🌟 Malamar\n🌟 Binacle\n🌟 Barbaracle\n🌟 Skrelp\n🌟 Dragalge\n🌟 Clauncher\n🌟 Clawitzer\n🌟 Helioptile\n🌟 Heliolisk\n🌟 Tyrunt\n🌟 Tyrantrum\n🌟 Amaura\n🌟 Aurorus\n🌟 Sylveon\n🌟 Hawlucha\n🌟 Dedenne\n🌟 Carbink\n🌟 Goomy\n🌟 Sliggoo\n🌟 Goodra\n🌟 Klefki\n🌟 Phantump\n🌟 Trevenant\n🌟 Pumpkaboo\n🌟 Gourgeist\n🌟 Bergmite\n🌟 Avalugg\n🌟 Noibat\n🌟 Noivern\n🌟 Xerneas\n🌟 Yveltal\n🌟 Zygarde\n🌟 Diancie\n🌟 Hoopa\n🌟 Volcanion",
    )
    
def gen7(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE THE LIST OF GENERATION 7 POKEMONS\n\n🌟 Alolan Rattata\n🌟 Alolan Raticate\n🌟 Alolan Raichu\n🌟 Alolan Sandshrew\n🌟 Alolan Sandslash\n🌟 Alolan Vulpix\n🌟 Alolan Ninetales\n🌟 Alolan Diglett\n🌟 Alolan Dugtrio\n🌟 Alolan Meowth\n🌟 Alolan Persian\n🌟 Alolan Geodude\n🌟 Alolan Graveler\n🌟 Alolan Golem\n🌟 Alolan Grimer\n🌟 Alolan Muk\n🌟 Alolan Exeggutor\n🌟 Alolan Marowak\n🌟 Rowlet\n🌟 Dartrix\n🌟 Decidueye\n🌟 Litten\n🌟 Torracat\n🌟 Incineroar\n🌟 Popplio\n🌟 Brionne\n🌟 Primarina\n🌟 Pikipek\n🌟 Trumbeak\n🌟 Toucannon\n🌟 Yungoos\n🌟 Gumshoos\n🌟 Grubbin\n🌟 Charjabug\n🌟 Vikavolt\n🌟 Crabrawler\n🌟 Crabominable\n🌟 Oricorio\n🌟 Cutiefly\n🌟 Ribombee\n🌟 Rockruff\n🌟 Lycanroc\n🌟 Wishiwashi\n🌟 Mareanie\n🌟 Toxapex\n🌟 Mudbray\n🌟 Mudsdale\n🌟 Dewpider\n🌟 Araquanid\n🌟 Fomantis\n🌟 Lurantis\n🌟 Morelull\n🌟 Shiinotic\n🌟 Salandit\n🌟 Salazzle\n🌟 Stufful\n🌟 Bewear\n🌟 Bounsweet\n🌟 Steenee\n🌟 Tsareena\n🌟 Comfey\n🌟 Oranguru\n🌟 Passimian\n🌟 Wimpod\n🌟 Golisopod\n🌟 Sandygast\n🌟 Palossand\n🌟 Pyukumuku\n🌟 Type:Null\n🌟 Silvally\n🌟 Minior\n🌟 Komala\n🌟 Turtonator\n🌟 Togedemaru\n🌟 Mimikyu\n🌟 Bruxish\n🌟 Drampa\n🌟 Dhelmise\n🌟 Jangmo-o\n🌟 Hakamo-o\n🌟 Kommo-o\n🌟 Tapu-Koko\n🌟 Tapu-Lele\n🌟 Tapu-Bulu\n🌟 Tapu-Fini\n🌟 Cosmog\n🌟 Cosmoem\n🌟 Solgaleo\n🌟 Lunala\n🌟 Nihilego\n🌟 Buzzwole\n🌟 Pheromosa\n🌟 Xurkitree\n🌟 Celesteela\n🌟 Kartana\n🌟 Guzzlord\n🌟 Necrozma\n🌟 Magearna\n🌟 Marshadow\n🌟 Poipole\n🌟 Naganadel\n🌟 Stakataka\n🌟 Blacephalon\n🌟 Zeraora\n🌟 Meltan\n🌟 Melmetal",
    )
GEN1_HANDLER = DisableAbleCommandHandler("gen1", gen1, run_async=True)
GEN2_HANDLER = DisableAbleCommandHandler("gen2", gen2, run_async=True)
GEN3_HANDLER = DisableAbleCommandHandler("gen3", gen3, run_async=True)
GEN4_HANDLER = DisableAbleCommandHandler("gen4", gen4, run_async=True)
GEN5_HANDLER = DisableAbleCommandHandler("gen5", gen5, run_async=True)
GEN6_HANDLER = DisableAbleCommandHandler("gen6", gen6, run_async=True)
GEN7_HANDLER = DisableAbleCommandHandler("gen7", gen7, run_async=True)

dispatcher.add_handler(GEN1_HANDLER)
dispatcher.add_handler(GEN2_HANDLER)
dispatcher.add_handler(GEN3_HANDLER)
dispatcher.add_handler(GEN4_HANDLER)
dispatcher.add_handler(GEN5_HANDLER)
dispatcher.add_handler(GEN6_HANDLER)
dispatcher.add_handler(GEN7_HANDLER)
