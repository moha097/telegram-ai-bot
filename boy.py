import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Récupérer ton token Telegram et ta clé API
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def start(update, context):
    update.message.reply_text("👋 Salut, je suis ton bot IA Python !")

def ask_ai(update, context):
    user_message = update.message.text
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    payload = {"model": "deepseek-chat", "messages": [{"role":"user","content": user_message}]}

    r = requests.post("https://api.deepseek.com/chat/completions", json=payload, headers=headers)
    response = r.json()["choices"][0]["message"]["content"]

    update.message.reply_text(response)

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ask_ai))

updater.start_polling()
