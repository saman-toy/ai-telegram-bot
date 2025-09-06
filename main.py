import openai
from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

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
