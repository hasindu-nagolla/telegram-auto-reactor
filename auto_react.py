import os
import requests
import random
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/setMessageReaction"

EMOJIS = ["👍", "❤️", "😂", "🔥", "👏", "😮", "😎"]

def send_reaction(chat_id: int, message_id: int, emoji: str):
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [{"type": "emoji", "emoji": emoji}],
        "is_big": False
    }
    response = requests.post(API_URL, json=data)
    if not response.ok:
        print("Reaction failed:", response.text)

# --- Polling example with python-telegram-bot style updates ---
from telegram.ext import Application, MessageHandler, filters

async def on_message(update, context):
    emoji = random.choice(EMOJIS)
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    send_reaction(chat_id, message_id, emoji)

if __name__ == "__main__":
    from telegram.ext import ApplicationBuilder
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, on_message))
    print("🚀 Auto‑Reaction Bot (Bot API mode) running …")
    application.run_polling()
