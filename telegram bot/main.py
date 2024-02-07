from os import getenv

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from alerts_in_ua.async_alerts_client import AsyncAlertsClient


load_dotenv("../.env")

bot = Bot(getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher(bot)

alerts_client = AsyncAlertsClient(getenv("ALERTS_CLIENT_TOKEN"))


@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.reply("Список тривог:\n/alerts")


@dp.message_handler(commands=["alerts"])
async def alerts(message: Message):
    locations = await alerts_client.get_active()
    alerts_map = locations.render_map()
    message_text = "\n".join(locations.location_title)

    await message.reply_photo(alerts_map, message_text)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
