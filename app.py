import os
from flask import Flask
from telebot import TeleBot

# Initialize Flask app for Render
app = Flask(__name__)

# Get the Bot Token from Render's Environment Variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)

# Flask route to satisfy Render's health checks
@app.route('/')
def home():
    return "Bot is running!"

# Telegram message handler for auto-reply
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    # Example logic: customize your auto-reply message here
    reply_text = "Hello! Thanks for reaching out to @Arch_907bot. We will get back to you shortly."
    bot.reply_to(message, reply_text)

# Run the bot
if __name__ == "__main__":
    # Start polling in a non-blocking way or let Render trigger the script
    print("Starting bot...")
    
    # We run the Flask app on the port Render provides, 
    # while running the bot's polling mechanism.
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
