from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
button_ai_analysis = KeyboardButton(text='AI-анализ тела')
button_meal_plan = KeyboardButton(text='Планы питания')
button_exercises = KeyboardButton(text='Упражнения')

main_menu = ReplyKeyboardMarkup(keyboard=[[button_ai_analysis, button_meal_plan, button_exercises]], resize_keyboard=True)
