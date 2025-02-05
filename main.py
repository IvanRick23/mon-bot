from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from dotenv import load_dotenv

# Charge le token depuis .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
print("TOKEN:", TOKEN)  # Ajoute ça avant updater = Updater(TOKEN) add de token manuellement

# Fonction pour /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Salut ! Je suis ton premier bot. Tape /aide pour voir les commandes.")

# Fonction pour /aide
def help(update: Update, context: CallbackContext):
    update.message.reply_text("ℹ️ Commandes disponibles : /start, /aide")

# Configure le bot
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# Ajoute les gestionnaires de commandes
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("aide", help))

# Démarre le bot
updater.start_polling()
print("✅ Le bot est en ligne !")
updater.idle()
