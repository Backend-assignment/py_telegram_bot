from telegram import Bot
TOKEN ='5913199109:AAG9-dVunDn9L499yI7bG-E8CFvBn2Rr6Ws'
# Create a bot object using the token
bot = Bot(token=TOKEN)  
user = bot.get_me()
print(user.first_name)