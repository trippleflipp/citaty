import json
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

# Замените 'YOUR_BOT_TOKEN' на ваш токен от @BotFather
BOT_TOKEN = '8044210024:AAEwTozNv90i7J0ZfWGWcRSCvzfbhV8LhiI'

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Загрузка цитат из JSON файла
def load_quotes():
    with open('data.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Создание клавиатуры с кнопкой "Цитата"
def get_quote_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Цитата")]],
        resize_keyboard=True
    )
    return keyboard

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот с цитатами Фридриха Ницше. Нажми на кнопку 'Цитата', чтобы получить случайную цитату. \nЯ могу работать плохо, но я стараюсь!",
        reply_markup=get_quote_keyboard()
    )

# Обработчик нажатия кнопки "Цитата"
@dp.message(lambda message: message.text == "Цитата")
async def send_quote(message: types.Message):
    quotes = load_quotes()
    random_quote = random.choice(quotes)
    await message.answer(f'{random_quote["quote"]}\n\n-- Фридрих Ницше')

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
