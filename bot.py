import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from config import BOT_TOKEN
from keyboards import main_menu

# Включение логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Хендлер на команду /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я твой фитнес-тренер.", reply_markup=main_menu)

# Хендлер на команду "AI-анализ тела"
@dp.message(lambda message: message.text == "AI-анализ тела")
async def ai_analysis(message: types.Message):
    await message.reply("Загрузите ваше фото для анализа.")

# Обработка фото для AI-анализа
@dp.message(lambda message: message.photo)
async def handle_photo(message: types.Message):
    # Здесь будет код анализа фотографии с использованием ИИ
    await message.reply("Фото получено. Анализ начат...")

async def main():
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
