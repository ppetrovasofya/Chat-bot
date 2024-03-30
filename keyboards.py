from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Создаем стартовую клавиатуру с кнопками для ответа
main = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="О боте", callback_data="bot_info"),
            InlineKeyboardButton(text="Начать анкету", callback_data="test"),
        ],
        [
            InlineKeyboardButton(text="О разработчиках", callback_data="authors"),
            InlineKeyboardButton(text="Тех.поддержка", callback_data="help"),
        ]
    ])

ready = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Начать", callback_data="ready"),
            InlineKeyboardButton(text="Назад", callback_data="main")
        ]
    ])

#кнопка назад
back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="main")]])


#кнопки для первого вопроса
first_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Ответ 1_1"),
            KeyboardButton(text="Ответ 1_2"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)

#кнопки для 2 вопроса
second_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Ответ 2_1"),
            KeyboardButton(text="Ответ 2_2"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
