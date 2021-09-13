# -*- coding: utf-8 -*-

import vkbottle
from vkbottle.bot import Bot, Message
from vkbottle import keyboard, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD
from vkbottle.tools.dev_tools.keyboard.button import KeyboardButton
from vkbottle.tools.dev_tools.keyboard.keyboard import Keyboard
from settiings import settings, tokens
from vkbottle import vkscript

bot = Bot(token=tokens)

raspisanie = ("☀️ Понедельник: \n"\
    "👣 Вторник: \n"\
    "👥 Среда: \n"\
    "🌝 Четверг: \n"\
    "🏖 Пятница: \n")
@bot.on.chat_message(text=[f".расписание", "@for10arsp .расписание" ])
async def handler(message:Message):
    # keyboard = Keyboard()

    # Keyboard(inline=True)

    # keyboard.add(Text(".расписание"), color=KeyboardButtonColor.SECONDARY)
    await message.answer(raspisanie)

@bot.on.chat_message(text=[f".расписание-пн", ])
async def handler(message:Message):
    await message.answer("☀️ Понедельник: ")

@bot.on.chat_message(text=[f".расписание-вт", ])
async def handler(message:Message):
    await message.answer("👣 Вторник: ")

@bot.on.chat_message(text=[f".расписание-ср", ])
async def handler(message:Message):
    await message.answer("👥 Среда:  ")

@bot.on.chat_message(text=[f".расписание-чт", ])
async def handler(message:Message):
    await message.answer("🌝 Четверг: ")

@bot.on.chat_message(text=[f".расписание-пт", ])
async def handler(message:Message):
    await message.answer("🏖 Пятница: ")

@bot.on.chat_message(text=[f".helpa", ])
async def handler(message:Message):
    await message.answer("help is ejected:\n\n"\
    ".helpa - это меню\n"\
    ".расписание - вызывает постоянное расписание на неделю\n"\
    ".расписание-day - показывает постоянное расписание на какой то день, доступные аргументы для day:\n\n"\
    "пн, вт, ср, чт, пт.\n\n"\
    "пример: .расписание-пн\n\n"\
    "домашка с сайта школы в разработке")

# @bot.on.chat_message(text=[f".admin-unlock", ])
# async def handler(message:Message):
#     user = await bot.api.users.get(user_ids=user_id) [0]
#     adminid = ["id206646211"]
#     for user_id in user_ids:
#         user = await bot.api.users.get(user_ids=user_id) [0]
#         if user_id in user_ids:
#             await message.answer("admin ejected")
#             break
#         else:
#             await message.answer("no permissions")

bot.run_forever()