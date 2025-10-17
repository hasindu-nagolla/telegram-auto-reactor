from pyrogram import Client, filters
from random import choice
import asyncio

# Replace with your own credentials
API_ID = 12345678
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

# Define a list of emojis to pick from
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

app = Client("auto_reactor", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# React to every new message in groups
@app.on_message(filters.group & ~filters.bot)
async def add_reaction(_, message):
    try:
        emoji = choice(EMOJIS)
        await message.react(emoji)
        print(f"Reacted to message {message.id} with {emoji}")
    except Exception as e:
        print(f"Error reacting to message {message.id}: {e}")

print("🤖 Auto Reaction Bot is running...")
app.run()
