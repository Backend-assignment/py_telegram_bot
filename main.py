from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot

    bot.sendMessage(chat_id, text)

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text, start))

updater.start_polling()

updater.idle()