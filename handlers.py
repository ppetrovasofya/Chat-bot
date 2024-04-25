from aiogram.filters import CommandStart
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery


import keyboards as kb
import faculty as fc


router = Router()
counter_answer = 0

# стартовое сообщение
@router.message(CommandStart())
async def main(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!",
                        reply_markup=kb.main)

#инлайн-кнопка "Тех поддержка"
@router.callback_query(F.data == "help")
async def university(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Если в процессе использования бота вы нашли опечатку,"
                                     " ошибку или баг, сообщите, пожалуйста, нам **ссылка на аккаунт поддержки",
                                     reply_markup=kb.back)

#инлайн-кнопка "кнопка назад"
@router.callback_query(F.data == "main")
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Добро пожаловать в главное меню", reply_markup=kb.main)

#инлайн-кнопка "О разработчиках"
@router.callback_query(F.data == "authors")
async def creators(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Бот создан командой студенток 2-го курса Интеллектуальных систем в гуманитарной сфере. \nАлександра Острая - руководитель проекта, разработчик \nСофья Петрова - разработчик\nАлёна Чеснокова - работа со студентами, дизайнер \nАнна Зайцева - работа со студентами, тестировщик", reply_markup=kb.back)

#инлайн-кнопка "О боте"
@router.callback_query(F.data == "bot_info")
async def about(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Бот PolyHumGuide поможет абитуриентам Гуманитарного института СПбПУ найти специальность по сферам личных и научных интересов с помощью анкетирования и получить всю актуальную информацию, необходимую для поступления.", reply_markup=kb.back)

#анкета
@router.callback_query(F.data == "test")
async def survey(callback: CallbackQuery):
    fc.score = {"law": 0, "region": 0,
             "advert": 0, "books": 0,
             "psyteach": 0, "ling": 0,
             "compling": 0, "forensic": 0}
    await callback.answer()  # Устанавливаем начальные значения для всех специальностей. При выборе того или иного ответа значение меняется
    await callback.message.edit_text(text="Данная анкета сделана на основе тестов на проф. ориентацию и отзывах нынешних студентов об их специальности. Ее прохождение поможет подобрать направление по сферам личных и научных интересов и оценить свои шансы на поступление.", reply_markup=kb.ready)

@router.callback_query(F.data == "ready")
async def q1(callback: CallbackQuery):
    fc.score = {"law": 0, "region": 0,
                "advert": 0, "books": 0,
                "psyteach": 0, "ling": 0,
                "compling": 0, "forensic": 0}
    await callback.answer()
    await callback.message.answer(text="1. Вилкой в глаз или в жопу раз?", reply_markup=kb.first_q)

@router.message(F.text =='Вилкой в глаз')
async def q2_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    fc.score["psyteach"] += 1
    fc.score["region"] += 1
    await message.answer(text="2. Экстраверт или интроверт?", reply_markup=kb.second_q)


@router.message(F.text =='В жопу раз')
async def q2_2(message: types.Message):
    fc.score["ling"] += 1
    fc.score["advert"] += 1
    fc.score["compling"] += 1
    fc.score["books"] += 1
    await message.answer(text="2. Экстраверт или интроверт?", reply_markup=kb.second_q)

@router.message(F.text =='Экстраверт')
async def q3_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    fc.score["psyteach"] += 1
    fc.score["books"] += 1
    await message.answer(text="3. Пиво или водка?", reply_markup=kb.third_q)


@router.message(F.text =='Интроверт')
async def q3_2(message: types.Message):
    fc.score["ling"] += 1
    fc.score["compling"] += 1
    fc.score["advert"] += 1
    fc.score["region"] += 1
    await message.answer(text="3. Пиво или водка? ", reply_markup=kb.third_q)

@router.message(F.text =='Пиво')
async def q4_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["advert"] += 1
    fc.score["forensic"] += 1
    fc.score["ling"] += 1
    await message.answer(text="4. Кринж или рофл?", reply_markup=kb.fourth_q)


@router.message(F.text =='Водка')
async def q4_2(message: types.Message):
    fc.score["region"] += 1
    fc.score["psyteach"] += 1
    fc.score["compling"] += 1
    fc.score["books"] += 1
    await message.answer(text="4. Кринж или рофл?", reply_markup=kb.fourth_q)

@router.message(F.text =='Кринж')
async def q5_1(message: types.Message):
    fc.score["region"] += 1
    fc.score["ling"] += 1
    fc.score["psyteach"] += 1
    fc.score["compling"] += 1
    await message.answer(text="5.Обычный паляж или нудистский?", reply_markup=kb.fifth_q)


@router.message(F.text =='Рофл')
async def q5_2(message: types.Message):
    fc.score["books"] += 1
    fc.score["advert"] += 1
    fc.score["forensic"] += 1
    fc.score["law"] += 1
    await message.answer(text="5.Обычный пляж или нудистский?", reply_markup=kb.fifth_q)

@router.message(F.text =='Обычный')
async def q6_1(message: types.Message):
    fc.score["books"] += 1
    fc.score["compling"] += 1
    fc.score["forensic"] += 1
    fc.score["region"] += 1
    await message.answer(text="6.Год без интернета или год без любви?", reply_markup=kb.sixth_q)


@router.message(F.text =='Нудистский')
async def q6_2(message: types.Message):
    fc.score["ling"] += 1
    fc.score["psyteach"] += 1
    fc.score["advert"] += 1
    fc.score["law"] += 1
    await message.answer(text="6. Год без интернета или год без любви?", reply_markup=kb.sixth_q)

@router.message(F.text =='Год без любви')
async def q7_1(message: types.Message):
    fc.score["ling"] += 1
    fc.score["forensic"] += 1
    fc.score["compling"] += 1
    fc.score["law"] += 1
    await message.answer(text="7.Иметь 100 друзей или 100 рублей?", reply_markup=kb.seventh_q)


@router.message(F.text =='Год без интернета')
async def q7_2(message: types.Message):
    fc.score["books"] += 1
    fc.score["advert"] += 1
    fc.score["psyteach"] += 1
    fc.score["region"] += 1
    await message.answer(text="7.Иметь 100 друзей или 100 рублей?", reply_markup=kb.seventh_q)


@router.message(F.text =='100 рублей')
async def q8_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["advert"] += 1
    fc.score["forensic"] += 1
    fc.score["region"] += 1
    await message.answer(text="8. Есть 2 стула. На одном пики точенные, на втором хуи дроченные. На какой сам сядешь, на какой мать посадишь?", reply_markup=kb.eight_q)

@router.message(F.text =='100 друзей')
async def q8_2(message: types.Message):
    fc.score["ling"] += 1
    fc.score["psyteach"] += 1
    fc.score["compling"] += 1
    fc.score["books"] += 1
    await message.answer(text="8. Есть 2 стула. На одном пики точенные, на втором хуи дроченные. На какой сам сядешь, на какой мать посадишь?", reply_markup=kb.eight_q)

@router.message(F.text == "Сяду на пики, мать на хуи")
async def handle_bye(message: types.Message):
    fc.score["ling"] += 1
    fc.score["psyteach"] += 1
    fc.score["forensic"] += 1
    fc.score["law"] += 1
    for k, val in fc.score.items():
        if val >= 6:
            prog = k
            global counter_answer
            counter_answer += 1
            await message.answer(text=f"Тебе может подойти  *{fc.programms[prog]}* \n\n*Ссылка на официальный сайт ГИ:* {fc.urls[prog]} \n\n*Описание программы:* {fc.description[prog]} \n\n*Минимальные баллы:*\n {fc.min_points[prog]}", parse_mode="Markdown")
    await message.answer(text="Молодец чел", reply_markup=kb.cal_after_survey)
    if counter_answer == 0:
        await message.answer(text="Чел тебе не по адресу. Иди на завод", reply_markup=kb.back)

@router.message(F.text == "Сяду на хуи, мать на пики")
async def handle_bye(message: types.Message):
    fc.score["books"] += 1
    fc.score["advert"] += 1
    fc.score["compling"] += 1
    fc.score["region"] += 1
    for k, val in fc.score.items():
        if val >= 6:
            prog = k
            global counter_answer
            counter_answer += 1
            await message.answer(text=f"Тебе может подойти  *{fc.programms[prog]}* \n\n*Ссылка на официальный сайт ГИ:* {fc.urls[prog]} \n\n*Описание программы:* {fc.description[prog]} \n\n*Минимальные баллы:*\n {fc.min_points[prog]}", parse_mode="Markdown")
    await message.answer(text="Молодец чел", reply_markup=kb.cal_after_survey)
    if counter_answer == 0:
        await message.answer(text="Чел тебе не по адресу. Иди на завод", reply_markup=kb.back)

@router.callback_query(F.data == "calculator")
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="Ты уже сдал ЕГЭ или прошел вступительные испытания?", reply_markup=kb.exam_passed)

@router.message(F.text =='Да')
async def yes(message: types.Message):
    await message.answer(text="Введи свой суммарный балл, включая баллы за ИД\nБаллы за ИД можно посмотреть здесь: https://www.spbstu.ru/abit/bachelor/oznakomitsya-with-the-regulations/individual-achievements/")

@router.message()
async def check_points(message: types.Message):
    try:
        points = int(message.text)
    except ValueError:
        await message.answer("Что-то пошло не так :(\nВведи свой суммарный балл, включая баллы за ИД")
    for k, val in fc.score.items():
        if val >= 6:
            prog = k
            if points < fc.exam_points22[prog]:
                await message.answer(f"На {fc.programms[prog]} в 2022г. ты бы не прошел")
            else:
                await message.answer(f"На {fc.programms[prog]} в 2022г. ты бы прошел")

            if points < fc.exam_points23[prog]:
                await message.answer(f"На {fc.programms[prog]} в 2023г. ты бы не прошел")
            else:
                await message.answer(f"На {fc.programms[prog]} в 2023г. ты бы прошел")

