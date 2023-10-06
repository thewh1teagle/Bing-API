from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from bingapi import BingAPI, HighDemandException
from telegram import InputMediaPhoto
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
assert TOKEN, '[DEBUG] TOKEN must be set in .env file or environment variables!'

print("[DEBUG] init Bing API")
api = BingAPI()


async def create(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text.split().__len__() < 3:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}. Please describe the image with at least 3 words')
    else:
        await update.message.reply_text(f'Creating images...\nYou will receive notification when ready.')
        try:
            images = api.create_images(text)
            media_group = []
            for index, image in enumerate(images):
                media_object = InputMediaPhoto(image.bytes(), caption=text if index == 0 else None)
                media_group.append(media_object)
            await update.message.reply_media_group(media_group)
        except HighDemandException:
            await update.message.reply_text(f'Cant create images due to high demand. max retry exceeded')
        except Exception as e:
            await update.message.reply_text(f'Cant create images due to unknown error. max retry exceeded')


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, create))

print("[DEBUG] bot running")
app.run_polling()