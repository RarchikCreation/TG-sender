import asyncio
from manager.bot_instance import bot, dp
import manager.handlers

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True))
