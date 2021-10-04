from discord.ext import commands
from config import Config

import logging
import asyncio

def main():
    # Setup logging config
    logging.basicConfig(level=logging.INFO)

    # Setup bot
    bot = commands.Bot(
        command_prefix=Config.BOT_PREFIX,
        description="Test"
    )

    # Killfeed cog
    cogs = [
        'cogs.killfeed',
    ]

    logging.debug("Loading cogs...")

    for extension in cogs:
        try:
            bot.load_extension(extension)
            logging.debug(f"Cog: {extension} loaded!")
        except Exception as e:
            logging.exception('Failed to load cog {}\n{}: {}'.format(extension, type(e).__name__, e))

    # Start bot loop
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(bot.start(Config.DISCORD_TOKEN))
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()