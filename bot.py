import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Я так рада, что ты написал!")
    print(update)

def talk_to_me (update, context):
    text = update.message.text
    print(text)
    if text.lower() == "привет":
        update.message.reply_text("привет")
    elif text.lower() == "как дела?":
        update.message.reply_text("Хорошо, а у тебя?")
    else:
       update.message.reply_text(text[::-1])

def main ():
    mybot = Updater (settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()

if __name__ = "__main__":
    main()