from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, "Welcome to echo bot")

def main(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot

    bot.sendMessage(chat_id, text)

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()