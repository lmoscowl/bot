import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from dotenv import load_dotenv
import sqlite3

# Загружаем переменные из .env
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Создание базы данных SQLite
conn = sqlite3.connect('gold_requests.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS requests
             (id INTEGER PRIMARY KEY, user_id INTEGER, city TEXT, weight REAL, value REAL, status TEXT)''')
conn.commit()

# Главная команда
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📍 Найти терминал", "💰 Оценить золото", "🛒 Купить слиток", "📤 Продать золото", "👤 Мои заявки")
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=markup)

# Обработка выбора действий
@dp.message_handler(lambda message: message.text == "📍 Найти терминал")
async def find_terminal(message: types.Message):
    terminals = [
        {"city": "Москва", "address": "ул. Тверская, 10", "hours": "9:00-18:00", "link": "https://maps.google.com/?q=Москва, ул. Тверская, 10"},
        {"city": "Санкт-Петербург", "address": "ул. Невский, 5", "hours": "10:00-20:00", "link": "https://maps.google.com/?q=Санкт-Петербург, ул. Невский, 5"}
    ]
    for terminal in terminals:
        await message.answer(f"Город: {terminal['city']}\nАдрес: {terminal['address']}\nРежим работы: {terminal['hours']}\n[Показать на карте]({terminal['link']})", parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(lambda message: message.text == "💰 Оценить золото")
async def evaluate_gold(message: types.Message):
    await message.answer("Введите металл (например, золото, серебро):")

@dp.message_handler(lambda message: message.text == "🛒 Купить слиток")
async def buy_bar(message: types.Message):
    await message.answer("Выберите вес слитка и его пробу.")

@dp.message_handler(lambda message: message.text == "📤 Продать золото")
async def sell_gold(message: types.Message):
    await message.answer("Введите вес вашего золота и выберите пробу.")

@dp.message_handler(lambda message: message.text == "👤 Мои заявки")
async def my_requests(message: types.Message):
    c.execute("SELECT * FROM requests WHERE user_id = ?", (message.from_user.id,))
    rows = c.fetchall()
    if rows:
        for row in rows:
            await message.answer(f"Заявка ID: {row[0]}\nГород: {row[2]}\nВес: {row[3]} г\nСумма: {row[4]} руб\nСтатус: {row[5]}")
    else:
        await message.answer("У вас нет заявок.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
