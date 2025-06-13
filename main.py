from dotenv import load_dotenv

from src.bot.bot_main import Bot

if __name__ == '__main__':
    load_dotenv()
    bot = Bot()
    bot.bot.run_polling()
