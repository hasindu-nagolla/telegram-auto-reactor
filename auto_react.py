import os
import random
from dotenv import load_dotenv
from pyrogram import Client, filters

# Load environment variables from .env
load_dotenv()

# Bot credentials
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN is not set in .env")

# Emojis to react with
EMOJIS = [
    "👍", "❤️", "😂", "🔥", "😄", "😮", "👏", "😭", "🤔", 
    "😎", "😁", "🙌", "🤩", "😏", "😜", "😢", "😡", "😱", 
    "🥰", "🤯", "🤗", "💪", "😴", "😇", "😈", "💀", "👻",
    "🎉", "✨", "💥", "💫", "🌈", "⚡", "🌟", "🍕", "🍔",
    "🍟", "🍩", "🍎", "🍌", "☕", "🍺", "🍷", "🎂", "🍫",
    "🐶", "🐱", "🦊", "🐼", "🐨", "🐵", "🐸", "🐯", "🦁",
    "🌹", "🌻", "🌼", "🍀", "🌳", "🌲", "🌊", "🏔️", "🏖️",
    "🚗", "✈️", "🚀", "🏀", "⚽", "🎮", "🎵", "🎸", "🎤",
    "💌", "📚", "📝", "💎", "📸", "🎁", "🔑", "🔒", "🛒",
    "🧩", "🪐", "⚓", "⏰", "📅", "📌", "💡", "🧠", "🫀",
    "🤝", "🙈", "🙉", "🙊", "🫶", "💃", "🕺", "🤷", "🤦"
]


# Initialise Pyrogram in Bot mode
app = Client("reactor_bot", bot_token=BOT_TOKEN)

# Optional: restrict to a specific chat (uncomment and set CHAT_ID)
# CHAT_ID = int(os.getenv("CHAT_ID"))
# @app.on_message(filters.chat(CHAT_ID) & filters.group)

@app.on_message(filters.group)
async def react_to_message(client, message):
    try:
        emoji = random.choice(EMOJIS)
        await message.react(emoji)
        print(f"Reacted to message {message.message_id} in chat {message.chat.id} with {emoji}")
    except Exception as e:
        print(f"Reaction failed for message {getattr(message, 'message_id', 'unknown')}: {e}")


print("Reaction bot running...")
app.run()
