import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
from aiogram.filters import CommandStart

load_dotenv()

API_KEY = os.getenv('API_KEY')

bot = Bot(API_KEY)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('hi!')

@dp.message()
async def echo_cmd(message: Message):
    await message.answer(message.text)    

async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())

