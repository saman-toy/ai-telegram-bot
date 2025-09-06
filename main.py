import openai
from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("8457495921:AAEapf2A8xbjkq_sUbnc1qpU9rJb_RvnkcY")
OPENAI_KEY = os.getenv("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")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

openai.api_key = OPENAI_KEY

@dp.message_handler()
async def chat_with_ai(message: types.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        answer = response.choices[0].message["content"]
        await message.answer(answer)
    except Exception as e:
        await message.answer("Ошибка: " + str(e))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
