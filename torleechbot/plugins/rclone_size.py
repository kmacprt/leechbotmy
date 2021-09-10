import subprocess
import os
import asyncio

from torleechbot import (
    EDIT_SLEEP_TIME_OUT,
    DESTINATION_FOLDER,
    RCLONE_CONFIG
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def check_size_g(client, message):
    #await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    del_it = await message.reply_text("☁️ Checking File size...wait!!!")
    subprocess.Popen(('touch', 'rclone.conf'), stdout = subprocess.PIPE)
    with open('rclone.conf', 'a', newline="\n") as fole:
        fole.write("[DRIVE]\n")
        fole.write(f"{RCLONE_CONFIG}")
    destination = f'{DESTINATION_FOLDER}'
    dk_kaj = subprocess.Popen(['rclone', 'size', '--config=rclone.conf', 'DRIVE:'f'{destination}'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    dk, kaj = dk_kaj.communicate()
    print(dk)
    print(kaj)
    print(kaj.decode("utf-8"))
    kaviaj = kaj.decode("utf-8")
    print(kaviaj)
    await asyncio.sleep(5)
    await message.reply_text(f"☁️ CloudInfo:\n\n{kaviaj}")
    await del_it.delete()



async def g_clearme(client, message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton("Yes 🚫", callback_data=("yesdoit").encode("UTF-8")))
    ikeyboard.append(InlineKeyboardButton("No 🤗", callback_data=("nodont").encode("UTF-8")))
    inline_keyboard.append(ikeyboard)
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text("You sure? 🚫 All local downloads will be cleared! 🚫", reply_markup=reply_markup, quote=True)
