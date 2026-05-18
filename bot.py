import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Read token from environment variable (secure)
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("No BOT_TOKEN found. Set the BOT_TOKEN environment variable.")

WELCOME_MESSAGE = (
    "Welcome to our AI community 🤖\n\n"
    "We share insights, stories, and useful tools about artificial intelligence and technology."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.initialize()
    await application.start()
    port = int(os.environ.get('PORT', 8080))
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=TOKEN,
        webhook_url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    )
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
