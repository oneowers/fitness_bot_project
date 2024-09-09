from aiogram import types

async def handle_meal_plan(message: types.Message):
    await message.reply("Ваш план питания готов.")
