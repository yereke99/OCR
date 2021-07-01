from logger import bot, storage

async def on_shut_down(dp):
    await bot.close()
    await storage.close()

if __name__ == "__main__":
    from aiogram import executor
    from telegram_bot import dp

    executor.start_polling(dp, on_shutdown=on_shut_down)
