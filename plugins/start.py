rom pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = """
Hi, I am **ANONYMOUS SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!
You Can too Clone me :-
https://github.com/ProThinkerGang/Anonymous-Bot
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Captions ❓", callback_data="captz")],
        [InlineKeyboardButton("Owner 🤴", url="https://t.me/Warning_MadBoy_is_Back")],
    ]
)


@Client.on_message(filters.command("start"))
async def start(client, message):
    fuser = message.from_user.id
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    NewVar = START
    if var.OWNER_ID and not message.from_user.id == var.OWNER_ID:
        geto = await client.get_users(var.OWNER_ID)
        NewVar += f"\n\nMaintained By @Warning_MadBoy_is_Back"
    else:
        NewVar += "\n**Owner Commands** - https://telegra.ph/Commands-for-Owner-07-03"
    await message.reply_text(
        NewVar, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )
