from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8632806801:AAFDdYnpcPORnrgeYDmhEiJ0GqIcDf9R60s"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في بوت مصطفى للسفر والسياحة ✈️")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("البوت يعمل...")

app.run_polling()