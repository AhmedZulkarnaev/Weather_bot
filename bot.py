import os
from dotenv import load_dotenv

import aiohttp
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Moscow")],
        [types.KeyboardButton(text="Grozny")],
        [types.KeyboardButton(text="Krasnodar")],
        [types.KeyboardButton(text="Vladivostok")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(
        f"Привет, {message.from_user.first_name}! "
        "Выбери город, чтобы узнать погоду!",
        reply_markup=keyboard
    )


@dp.message()
async def get_response_weather(message: types.Message):
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.get(
                f'https://api.openweathermap.org/data/2.5/weather?q='
                f'{message.text}&appid={WEATHER_TOKEN}&units=metric'
            )
            response_data = await response.json()
            city = response_data['name']
            temp = response_data['main']['temp']
            await message.answer(
                f"Температура в городе - {city}: {temp:.0f}°C"
            )
    except Exception as e:
        await message.answer(
            f'Ошибка при получении данных о погоде: ({e})'
        )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
