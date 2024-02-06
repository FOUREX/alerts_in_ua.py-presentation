import asyncio
from os import getenv

from dotenv import load_dotenv
from PIL import Image

from alerts_in_ua.async_alerts_client import AsyncAlertsClient

load_dotenv()

client = AsyncAlertsClient(getenv("ALERTS_CLIENT_TOKEN"))


async def main():
    locations = await client.get_active()
    locations.clear()
    print(locations)

    print("Нікопольська територіальна громада" in locations)

    img = Image.open(locations.render_map())
    img.save("ClearMap.png", "png")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
