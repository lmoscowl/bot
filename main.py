
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "YOUR_BOT_TOKEN"
ADMIN_CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text="📍 Найти терминал")],
        [types.KeyboardButton(text="💰 Оценить золото")],
        [types.KeyboardButton(text="🛒 Купить слиток")],
        [types.KeyboardButton(text="📤 Продать золото")],
        [types.KeyboardButton(text="👤 Мои заявки")]
    ], resize_keyboard=True)
    await message.answer("👋 Добро пожаловать в GOLDEXROBOT!", reply_markup=keyboard)

@dp.message()
async def handle_buttons(message: types.Message):
    if message.text == "📍 Найти терминал":
        await message.answer("Выберите город: Москва, Санкт-Петербург, Казань...")
    elif message.text == "💰 Оценить золото":
        await message.answer("Введите параметры: металл, проба, вес.")
    elif message.text == "🛒 Купить слиток":
        await message.answer("Каталог слитков доступен на сайте: https://investingold.club/buy-bullions")
    elif message.text == "📤 Продать золото":
        await message.answer("Введите параметры для продажи.")
    elif message.text == "👤 Мои заявки":
        await message.answer("Ваши заявки: (пока что здесь пусто)")
    else:
        await message.answer("Выберите действие с клавиатуры.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
