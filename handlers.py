from aiogram.filters import CommandStart
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery


import keyboards as kb
import faculty as fc


router = Router()
answers = ["Ответ 1_1", "Ответ 1_2", "Ответ 2_1", "Ответ 2_2"]
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
    await callback.message.answer(text="Первый вопрос:", reply_markup=kb.first_q)

@router.message(F.text =='Ответ 1_1')
async def q2(message: types.Message):
    fc.score["law"] += 1
    await message.answer(text="Второй вопрос:", reply_markup=kb.second_q)


@router.message(F.text =='Ответ 1_2')
async def q2(message: types.Message):
    fc.score["ling"] += 1
    await message.answer(text="Второй вопрос:", reply_markup=kb.second_q)

@router.message(F.text == "Ответ 2_1")
async def handle_bye(message: types.Message):
    fc.score["law"] += 1
    for k, val in fc.score.items():
        if val >= 2:
            prog = k
            global counter_answer
            counter_answer += 1
            await message.answer(text=f"Тебе может подойти специальность {fc.programms[prog]} \nОфициальное описание программы: {fc.urls[prog]}", reply_markup=kb.back)
    if counter_answer == 0:
        await message.answer(text="Чел тебе не по адресу. Иди на завод", reply_markup=kb.back)

@router.message(F.text == "Ответ 2_2")
async def handle_bye(message: types.Message):
    fc.score["ling"] += 1
    for k, val in fc.score.items():
        if val >= 2:
            prog = k
            global counter_answer
            counter_answer += 1
            await message.answer(text=f"Тебе может подойти специальность {fc.programms[prog]} \nСсылка на официальный сайт ГИ: {fc.urls[prog]} \nОписание программы: {fc.description[prog]}", reply_markup=kb.back)
    if counter_answer == 0:
        await message.answer(text="Чел тебе не по адресу. Иди на завод", reply_markup=kb.back)

"""Предполагается, что пользователь ничего не будет самостоятельно писать в чат - все будет реализовано с помощью кнопок. 
Поэтому при написании в чат чего то лишнего бот выдаст следующее сообщение"""
@router.message()
async def handle_text(message: Message):
    if message.text.lower() not in answers:
        await message.answer("Переформулируй свое сообщение")