import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from command_handlers import send_spotify_songs

# Загрузка переменных окружения из .env
load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Use /spotify <query> to search for songs.")

async def spotify_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)
    await send_spotify_songs(update, context, query)

def main():
    token = os.getenv("TOKEN")
    url = os.getenv("URL")
    port = int(os.getenv("PORT", 8443))

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("spotify", spotify_command))

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=token,
        webhook_url=f"{url}/{token}"
    )

if __name__ == "__main__":
    main()
