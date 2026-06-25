import os
import time
from telebot import TeleBot

# Get the Bot Token from Render's Environment Variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")

bot = TeleBot(BOT_TOKEN)

# Telegram message handler for auto-reply
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    # Customize your automated reply here
    reply_text = "Hello! Thanks for reaching out to @Arch_907bot. We have received your message and will get back to you soon."
    
    try:
        bot.reply_to(message, reply_text)
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    print("Arch_907bot background worker is starting...")
    
    # infinity_polling automatically handles reconnects if connection drops
    bot.infinity_polling()
