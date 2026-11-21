import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://kotlinhgs2w.github.io/nomerok/")

if not TOKEN:
    raise RuntimeError("Добавь BOT_TOKEN в файл .env")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🎰 КРУТИТЬ НОМЕРА",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]])
    await message.answer(
        "Зашёл покрутить номера? 🗿\n"
        "Тогда залетай — вдруг сегодня выпадет легенда! ⬇️",
        reply_markup=keyboard
    )

async def main():
    print("НОМЕРОК запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
