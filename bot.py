import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token from BotFather
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Your welcome message
WELCOME_MESSAGE = (
    "Welcome to our AI community 🤖\n\n"
    "We share insights, stories, and useful tools about artificial intelligence and technology."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text(WELCOME_MESSAGE)

async def main():
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot using webhooks (the correct method for Render)
    await application.initialize()
    await application.start()
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get('PORT', 8080))
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    )
    # Keep the bot running
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
