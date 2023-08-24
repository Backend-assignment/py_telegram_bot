from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):

    chat_id = update.message.chat.id
    bot = context.bot

    contact = KeyboardButton(text='contact', request_contact=True)
    location = KeyboardButton(text='location', request_location=True)

    keyboard = ReplyKeyboardMarkup([[contact, location]], resize_keyboard=True)
    
    bot.sendMessage(chat_id, "Welcome to echo bot", reply_markup=keyboard)

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