
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio, os

TOKEN = os.getenv("TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

if not TOKEN:
    raise ValueError("TOKEN переменная окружения не установлена")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📍 Найти терминал")],
            [types.KeyboardButton(text="💰 Оценить золото")],
            [types.KeyboardButton(text="🛒 Купить слиток")],
            [types.KeyboardButton(text="📤 Продать золото")],
            [types.KeyboardButton(text="👤 Мои заявки")]
        ],
        resize_keyboard=True
    )
    await message.answer("👋 Добро пожаловать в GOLDEXROBOT!\nВыберите действие:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
