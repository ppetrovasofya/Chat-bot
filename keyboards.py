from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove


# Создаем стартовую клавиатуру с кнопками для ответа
main = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="О боте", callback_data="bot_info"),
            InlineKeyboardButton(text="Начать анкету", callback_data="test"),
        ],
        [
            InlineKeyboardButton(text="О разработчиках", callback_data="authors"),
            InlineKeyboardButton(text="Тех. поддержка", callback_data="help"),
        ]
    ])

ready = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="main"),
            InlineKeyboardButton(text="Начать", callback_data="ready")
        ]
    ])

#кнопка назад
back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="main")]])

#калькулятор баллов
cal_after_survey = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="main"),
            InlineKeyboardButton(text="Шансы на поступление", callback_data="calculator")
        ]
    ])

exam_passed = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для первого вопроса
first_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Вилкой в глаз"),
            KeyboardButton(text="В жопу раз"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 2 вопроса
second_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Экстраверт"),
            KeyboardButton(text="Интроверт"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 3 вопроса
third_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Пиво"),
            KeyboardButton(text="Водка"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 4 вопроса
fourth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Кринж"),
            KeyboardButton(text="Рофл"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 5 вопроса
fifth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Обычный"),
            KeyboardButton(text="Нудистский"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 6 вопроса
sixth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Год без любви"),
            KeyboardButton(text="Год без интернета"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 7 вопроса
seventh_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="100 рублей"),
            KeyboardButton(text="100 друзей"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 8 вопроса
eight_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Сяду на хуи, мать на пики"),
            KeyboardButton(text="Сяду на пики, мать на хуи"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()


