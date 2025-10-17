import os
import random
from dotenv import load_dotenv
from pyrogram import Client, filters

# Load variables from .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN missing in .env")

# Emojis to use as reactions
EMOJIS = ["👍", "❤️", "😂", "🔥", "👏", "😮", "😎", "💯", "🤔"]

# Initialize client in Bot API mode
app = Client("auto_reactor_bot", bot_token=BOT_TOKEN)

# React to each new group message
@app.on_message(filters.group & filters.incoming)
async def auto_react(_, message):
    try:
        # Ignore service messages (join/leave etc.)
        if message.service:
            return

        emoji = random.choice(EMOJIS)
        await message.react(emoji)
        print(f"Reacted to message {message.id} in {message.chat.title} with {emoji}")

    except Exception as e:
        print(f"Failed reaction → {e}")

print("🚀 Auto‑Reaction Bot is running…")
app.run()
