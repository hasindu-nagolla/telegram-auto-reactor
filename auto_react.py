import os
import random
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not all([API_ID, API_HASH, BOT_TOKEN]):
    raise SystemExit("API_ID, API_HASH, or BOT_TOKEN missing in .env")

EMOJIS = ["👍", "❤️", "😂", "🔥", "👏", "😮", "😎"]

# Bot mode, but with full API creds
app = Client(
    "auto_reactor_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.group & filters.incoming)
async def react_to_message(_, message):
    try:
        if message.service:  # skip join/leave notices
            return
        emoji = random.choice(EMOJIS)
        await message.react(emoji)
        print(f"Reacted to message {message.id} in {message.chat.title} with {emoji}")
    except Exception as e:
        print(f"Reaction failed → {e}")

print("🚀 Auto‑Reaction Bot running …")
app.run()
