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
        ],
        [
            InlineKeyboardButton(text="Что за птица?", callback_data="birdy"),  # Кнопка про птичку
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
            InlineKeyboardButton(text="Назад", callback_data="main")
        ],
        [
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

#кнопки для 1 вопроса
first_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="a) «Человек – человек»")
        ],
        [
            KeyboardButton(text="б) «Человек – знаковая система»")
        ],
        [
            KeyboardButton(text="в) «Человек – художественный образ»"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 2 вопроса
second_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Да, хочу"),
            KeyboardButton(text="Нет, не хочу"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 3 вопроса
third_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Технические науки ")
        ],
        [
            KeyboardButton(text="б) Гуманитарные науки")
        ],
        [
            KeyboardButton(text="в) Социальные науки")
        ],
        [
            KeyboardButton(text="г) Естественные науки")
        ],
        [
            KeyboardButton(text="д) Искусство и дизайн")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 4 вопроса
fourth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Внимательность")
        ],
        [
            KeyboardButton(text="б) Многозадачность")
        ],
        [
            KeyboardButton(text="в) Усидчивость")
        ],
        [
            KeyboardButton(text="г) Стрессоустойчивость")
        ],
        [
            KeyboardButton(text="д) Коммуникабельность")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 5 вопроса
fifth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Ораторское искусство")
        ],
        [
            KeyboardButton(text="б) Логическое мышление")
        ],
        [
            KeyboardButton(text="в) Креативное мышление")
        ],
        [
            KeyboardButton(text="г) Эрудированность"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 6 вопроса
sixth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Читать книги, журналы")
        ],
        [
            KeyboardButton(text="б) Посты в соц. сетях")
        ],
        [
            KeyboardButton(text="в) Изучать языки")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 7 вопроса
seventh_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Тру-крайм")
        ],
        [
            KeyboardButton(text="б) Туториал")
        ],
        [
            KeyboardButton(text="в) Тревел-блог")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

#кнопки для 8 вопроса
eight_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Следственные мероприятия")
        ],
        [
            KeyboardButton(text="б) Обсудить публикацию")
        ],
        [
            KeyboardButton(text="в) Никакую из этих")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

ninth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Включу фильтр")
        ],
        [
            KeyboardButton(text="б) Напишу программу")
        ],
        [
            KeyboardButton(text="в) Не буду это делать")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

tenth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Провести опыт")
        ],
        [
            KeyboardButton(text="б) Провести урок")
        ],
        [
            KeyboardButton(text="в) Ничего не выберу")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

eleventh_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Помогать в издании")
        ],
        [
            KeyboardButton(text="б) Организовать выставку")
        ],
        [
            KeyboardButton(text="в) Быть вожатым(-ой)")
        ],
        [
            KeyboardButton(text="г) Участвовать в жизни школы")
        ],
        [
            KeyboardButton(text="д) Ничего из этого")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

twelth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Историю и культуру")
        ],
        [
            KeyboardButton(text="б) Язык программирования")
        ],
        [
            KeyboardButton(text="в) Ничего")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()

thirteenth_q = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="а) Создавать контент")
        ],
        [
            KeyboardButton(text="б) Работать с детьми")
        ],
        [
            KeyboardButton(text="в) Что-то другое")
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
ReplyKeyboardRemove()
