from telegram.ext import Updater, CommandHandler, MessageHandler, filters, Application, ContextTypes

from telegram import ForceReply, Update, ReplyKeyboardMarkup, KeyboardButton


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def Aburdabar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        rf"I am mighty Aburdabar. Kneel before me!",
        reply_markup=ForceReply(selective=True),
    )

async def NOno(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        rf"Please?",
        reply_markup=ForceReply(selective=True),
    )

async def NOno_absolutely(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        rf"Pretty please?",
        reply_markup=ForceReply(selective=True),
    )



application = Application.builder().token("").build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("Aburdabar", Aburdabar))
application.add_handler(CommandHandler("no", NOno))
application.add_handler(CommandHandler("never", NOno_absolutely))
application.run_polling(allowed_updates=Update.ALL_TYPES)
