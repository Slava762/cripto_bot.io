import asyncio
from telegram import Bot, Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# --- ВАШИ ДАННЫЕ ---
BOT_TOKEN = '7203662704:AAGizI-3TREMhUXf55cMnZOMV8p6JYnWshs' 
# URL, на котором будет размещено ваше веб-приложение (пока используем временный)
WEB_APP_URL = 'https://github.com/Slava762/cripto_bot.io' # Замените на свой URL, когда он будет

# Команда /start
async def start(update: Update, context) -> None:
    """Отправляет приветственное сообщение и кнопку для открытия Web App."""
    keyboard = [
        [InlineKeyboardButton("📈 Открыть торговый терминал", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'Добро пожаловать в торговый терминал! Нажмите кнопку ниже, чтобы начать.',
        reply_markup=reply_markup
    )

def main() -> None:
    """Запуск бота."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчик для команды /start
    application.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
