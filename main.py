from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import bot, dp
import logging


@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("NEXT",  callback_data="button_call1")
    markup.add(button_call1)

    question = "Как звали младшего сына Дона Корлеоне?"
    answers = [
        'Сантино',
        'Фредерико',
        'Антонио',
        'Майкл',
        'Том',
        'Паоло'
    ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question = question,
        options = answers,
        is_anonymous=False,
        type = 'quiz',
        correct_option_id=3,
        explanation='Майкл Корлеоне - младший сын Дона',
        open_period = 15,
        reply_markup=markup

    )
@dp.callback_query_handler(lambda call: call.data == "button_call1")
async def quiz2(call: types.CallbackQuery):
        question = 'В каком году вышел фильм "Крестный отец?"'
        answers = [
            '1962',
            '1969',
            '1972',
            '1979',
            '1982'
        ]
        await bot.send_poll(
            chat_id=call.message.chat.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,
            explanation='Криминальная сага была выпущена в 1972 году',
            open_period=15
        )





@dp.message_handler(commands=["mem"])
async def command_start(message: types.Message):
    photo = open('media/013e78fb-7c3f-4ad3-9387-8a69ee9695de.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo)



@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
