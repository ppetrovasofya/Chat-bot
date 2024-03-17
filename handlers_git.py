from aiogram.filters import CommandStart
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import keyboards as kb

router = Router()
programms = {}
answers = ["Ответ 1_1", "Ответ 1_2", "Ответ 2_1", "Ответ 2_2"]


# стартовое сообщение
@router.message(CommandStart())
async def main(message: types.Message):
    await message.answer(text=f"Приветствую, {message.from_user.first_name}",
                        reply_markup=kb.main)

#инлайн-кнопка "Об институте"
@router.callback_query(F.data == "uni_info")
async def university(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("[Инфа об институте]", reply_markup=kb.back)

#инлайн-кнопка "кнопка назад"
@router.callback_query(F.data == "main")
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Добро пожаловать в главное меню", reply_markup=kb.main)

#инлайн-кнопка "Разработчики"
@router.callback_query(F.data == "authors")
async def creators(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Бота разработали скуфы", reply_markup=kb.back)

#инлайн-кнопка "О боте"
@router.callback_query(F.data == "bot_info")
async def about(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("[Инфа о боте]", reply_markup=kb.back)

#анкета
@router.callback_query(F.data == "test")
async def anketa(callback: CallbackQuery):
    await callback.answer()
    global programms
    programms = {"p1": 0, "p2": 0}  # Устанавливаем начальные значения для всех специальностей. При выборе того или иного ответа значение меняется
    await callback.message.edit_text(text="[Об анкете]", reply_markup=kb.ready)

@router.callback_query(F.data == "ready")
async def q1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="Первый вопрос:", reply_markup=kb.first_q)

@router.message(F.text =='Ответ 1_1')
async def q2(message: types.Message):
    programms["p1"] += 1
    await message.answer(text="Второй вопрос:", reply_markup=kb.second_q)


@router.message(F.text =='Ответ 1_2')
async def q2(message: types.Message):
    programms["p2"] += 1
    await message.answer(text="Второй вопрос:", reply_markup=kb.second_q)

@router.message(F.text == "Ответ 2_1")
async def handle_bye(message: types.Message):
    programms["p1"] += 1
    appealing = ""
    for k, v in programms.items():
        if v == max(programms.values()):
            appealing += k + ", "
    await message.answer(text=f"{appealing} TEST = {programms}", reply_markup=kb.back)

@router.message(F.text == "Ответ 2_2")
async def handle_bye(message: types.Message):
    programms["p2"] += 1
    appealing = ""
    for k, v in programms.items():
        if v == max(programms.values()):
            appealing += k + ", "
    await message.answer(text=f"{message.from_user.first_name}, your result: {appealing} TEST = {programms}", reply_markup=kb.back)

"""Предполагается, что пользователь ничего не будет самостоятельно писать в чат - все будет реализовано с помощью кнопок. 
Поэтому при написании в чат чего то лишнего бот выдаст следующее сообщение"""
@router.message()
async def handle_text(message: Message):
    if message.text.lower() not in answers:
        await message.answer("Переформулируй свое сообщение")