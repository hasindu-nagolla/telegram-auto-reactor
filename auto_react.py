import os
import random
import requests
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# ---------- Configuration ----------
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise SystemExit("❌ BOT_TOKEN missing in .env")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/setMessageReaction"

EMOJIS = ["👍", "❤️", "😂", "🔥", "😄", "😮", "👏", "😭", "🤔", "😎",
          "😁", "🙌", "🤩", "😏", "😜", "😢", "😡", "😱", "🥰", "🤯", 
          "🤗", "💪", "😴", "😇", "😈", "💀", "👻", "🎉", "✨", "💥",
          "💫", "🌈", "⚡", "🌟", "🍕", "🍔", "🍟", "🍩", "🍎", "🍌",
          "☕", "🍺", "🍷", "🎂", "🍫", "🐶", "🐱", "🦊", "🐼", "🐨",
          "🐵", "🐸", "🐯", "🦁", "🌹", "🌻", "🌼", "🍀", "🌳", "🌲",
          "🌊", "🏔️", "🏖️", "🚗", "✈️", "🚀", "🏀", "⚽", "🎮", "🎵",
          "🎸", "🎤", "💌", "📚", "📝", "💎", "📸", "🎁", "🔑", "🔒",
          "🛒", "🧩", "🪐", "⚓", "⏰", "📅", "📌", "💡", "🧠", "🫀",
          "🤝", "🙈", "🙉", "🙊", "🫶", "💃", "🕺", "🤷", "🤦"]

# ---------- Reaction send helper ----------


def send_reaction(chat_id: int, message_id: int, emoji: str):
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [{"type": "emoji", "emoji": emoji}],
        "is_big": False
    }
    response = requests.post(API_URL, json=data)
    if response.ok:
        print(f"✅ Reacted to message {message_id} with {emoji}")
    else:
        print(f"❌ Reaction failed ({response.status_code}): {response.text}")

# ---------- Handler ----------


async def on_message(update, context):
    """Pick a random emoji & send reaction via Bot API."""
    message = update.message
    if not message:  # skip non-message updates
        return
    try:
        emoji = random.choice(EMOJIS)
        send_reaction(message.chat_id, message.message_id, emoji)
    except Exception as e:
        print("Error reacting:", e)

# ---------- Main ----------


def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, on_message))
    print("🚀 Auto‑Reaction Bot running in Bot API mode …")
    application.run_polling()


if __name__ == "__main__":
    main()
