import os
import random
import requests
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# ---------- Configuration ----------
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise SystemExit("❌ BOT_TOKEN missing in .env")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/setMessageReaction"

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Emoji Categories (Telegram-compatible reactions only)
EMOJI_POSITIVE = ["❤", "🔥", "🎉", "🥰", "😍", "🤩", "👏", "🏆", "💯", "⚡"]
EMOJI_NEGATIVE = ["😢", "💔", "👎", "😭", "🤮", "🤬", "😱", "🥱"]
EMOJI_FUNNY = ["😂", "🤣", "🤪", "🤡", "🤭"]
EMOJI_NEUTRAL = ["🤔", "👀", "🤷", "😐", "🙄"]
EMOJI_DEFAULT = [
    "👍", "👌", "🤝", "😎", "🤖", "⭐",
]

# Keyword Triggers (Lowercase keys) - Using Telegram-compatible emojis
KEYWORD_TRIGGERS = {
    "coffee": "☕",
    "good night": "😴",
    "sleep": "🥱",
    "hello": "👋",
    "hi": "👋",
    "bye": "👋",
    "good morning": "🌅",
    "congrats": "🎉",
    "congratulations": "🎉",
    "happy birthday": "🎂",
    "party": "🥳",
    "love": "❤",
    "hate": "💔",
    "lol": "😂",
    "lmao": "🤣",
    "rofl": "🤣",
    "haha": "😂",
    "thanks": "🙏",
    "thank you": "🙏",
    "cool": "😎",
    "wow": "🤯",
}

# ---------- Logic Helper ----------
def get_reaction_emoji(text: str) -> str:
    """Determine the best emoji reaction based on keywords and sentiment."""
    text_lower = text.lower()

    # 1. Check for Keyword Triggers
    for keyword, emoji in KEYWORD_TRIGGERS.items():
        # Check if keyword is in the text (simple substring match)
        # For more strict matching, we could use regex with word boundaries
        if keyword in text_lower:
            return emoji

    # 2. explicit "Funny" markers are handled in keywords (lol, haha),
    # but let's double check if we want a dedicated logic or just stick to keywords.
    # The KEYWORD_TRIGGERS already handles "lol", "haha" etc.

    # 3. Analyze Sentiment
    sentiment = analyzer.polarity_scores(text)
    compound_score = sentiment['compound']

    if compound_score >= 0.05:
        return random.choice(EMOJI_POSITIVE)
    elif compound_score <= -0.05:
        return random.choice(EMOJI_NEGATIVE)
    else:
        # Neutral sentiment
        return random.choice(EMOJI_NEUTRAL)


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

# ---------- Handlers ---------
async def on_start(update, context):
    """Send welcome message when /start is issued."""
    welcome_message = (
        "🎉 **Welcome to the Smart Auto-Reactor Bot!** 🎉\n\n"
        "I react to every message—but now I'm smarter! 🧠\n\n"
        "**Features:**\n"
        "❤️ **Sentiment Analysis:** I can tell if you're happy, sad, or angry.\n"
        "🔑 **Keywords:** Say 'coffee', 'hello', or 'good night' for special reactions!\n"
        "😂 **Fun Mode:** I laugh at your jokes!\n\n"
        "Add me to a group and start chatting!"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


async def on_message(update, context):
    """Analyze text & send reaction via Bot API."""
    message = update.message
    if not message or not message.text:  # skip non-text messages
        return

    try:
        emoji = get_reaction_emoji(message.text)
        send_reaction(message.chat_id, message.message_id, emoji)
    except Exception as e:
        print("Error reacting:", e)

# ---------- Main ----------
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", on_start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), on_message))
    print("🚀 Smart Auto‑Reaction Bot running...")
    application.run_polling()


if __name__ == "__main__":
    main()
