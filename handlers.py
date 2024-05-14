from aiogram.filters import CommandStart
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery


import keyboards as kb
import faculty as fc


router = Router()
counter_answer = 0
passed = False


# стартовое сообщение
@router.message(CommandStart())
async def main(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!",
                        reply_markup=kb.main) # в случае затруднений вызови команду help


# инлайн-кнопка "Тех. поддержка"
@router.callback_query(F.data == "help")
async def university(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Если в процессе использования бота вы нашли опечатку, ошибку или баг, сообщите, пожалуйста, нам", reply_markup=kb.back)


# инлайн-кнопка "Что за птица?"
@router.callback_query(F.data == "birdy")
async def birdy(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Я кеклик. Мои сородичи обитают в районе Средней Азии, Алтая, Кавказских гор, Гималаев, а также на Балканах и на севере Китая. '
                                     '\nО себе скажу так: люблю принимать грязевые ванны. Но это не потому, что у меня нет денег на мыло. '
                                     'Я же птица, в первую очередь. Как многие подростки, я обожаю кекать и вести сидячий образ жизни. '
                                     'Как большинство студентов, питаюсь тем, что попадет под ноги. '
                                     'Мой рацион обычно состоит из зерен, почек кустарников и невысоких деревьев, а еще ягод, травки, паучков и жучков.'
                                     '\nСовет для будущего студента: принимай ванны от паразитов, кушай больше белков, выбирай жилище недалеко от университета '
                                     'и не забывай, что кек продлевает жизнь.',
                                     reply_markup=kb.back)


# инлайн-кнопка "кнопка назад"
@router.callback_query(F.data == "main")
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Добро пожаловать в главное меню", reply_markup=kb.main)


# инлайн-кнопка "О разработчиках"
@router.callback_query(F.data == "authors")
async def creators(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Бот создан командой студенток 2-го курса Интеллектуальных систем в гуманитарной сфере. \nАлександра Острая - руководитель проекта, разработчик \nСофья Петрова - разработчик\nАлёна Чеснокова - работа со студентами, дизайнер \nАнна Зайцева - работа со студентами, тестировщик", reply_markup=kb.back)


# инлайн-кнопка "О боте"
@router.callback_query(F.data == "bot_info")
async def about(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Бот PolyHumGuide поможет абитуриентам Гуманитарного института СПбПУ найти направление подготовки по сферам личных и научных интересов с помощью анкетирования и получить всю актуальную информацию, необходимую для поступления.", reply_markup=kb.back)


# анкета
@router.callback_query(F.data == "test")
async def survey(callback: CallbackQuery):
    fc.score = {"law": 0, "region": 0,
             "advert": 0, "books": 0,
             "psyteach": 0, "ling": 0,
             "compling": 0, "forensic": 0}
    await callback.answer()  # Устанавливаем начальные значения для всех специальностей. При выборе того или иного ответа значение меняется
    await callback.message.edit_text(text="Данная анкета сделана на основе тестов на профориентацию и отзывах нынешних студентов об их направлении подготовки. Ее прохождение поможет подобрать направление по сферам личных и научных интересов и оценить свои шансы на поступление.", reply_markup=kb.ready)


@router.callback_query(F.data == "ready")
async def q1(callback: CallbackQuery):
    fc.score = {"law": 0, "region": 0,
                "advert": 0, "books": 0,
                "psyteach": 0, "ling": 0,
                "compling": 0, "forensic": 0}
    await callback.answer()
    await callback.message.answer(text="1. Какой тип профессии ты предпочтешь? \n\n"
                                       "a) «Человек – человек» – это работа с людьми во всех ее видах и проявления.\n"
                                       "б) «Человек – знаковая система» – любая деятельность, связанная с "
                                       "необходимостью систематизации и обозначения чего-либо.\n"
                                       "в) «Человек – художественный образ» – это все профессии творческого спектра "
                                       "и все специальности, требующие творческого подхода и креатива.", reply_markup=kb.first_q)


@router.message(F.text == "a) «Человек – человек»")
async def q2_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["region"] += 1
    fc.score["advert"] += 1
    fc.score["psyteach"] += 1
    fc.score["ling"] += 1
    await message.answer(text="2. На любом направлении в ГИ изучается английский язык в качестве первого иностранного языка. "
                              "Хочешь овладеть вторым иностранным языком?", reply_markup=kb.second_q)


@router.message(F.text == "б) «Человек – знаковая система»")
async def q2_2(message: types.Message):
    fc.score["forensic"] += 1
    fc.score["books"] += 1
    fc.score["ling"] += 1
    fc.score["compling"] += 1
    await message.answer(text="2. На любом направлении в ГИ изучается английский язык в качестве первого иностранного языка. "
                              "Хочешь овладеть вторым иностранным языком?", reply_markup=kb.second_q)


@router.message(F.text == "в) «Человек – художественный образ»")
async def q2_3(message: types.Message):
    fc.score["advert"] += 1
    fc.score["books"] += 1
    await message.answer(text="2. На любом направлении в ГИ изучается английский язык в качестве первого иностранного языка. "
                              "Хочешь овладеть вторым иностранным языком?", reply_markup=kb.second_q)


@router.message(F.text == 'Да, хочу')
async def q3_1(message: types.Message):
    fc.score["region"] += 1
    fc.score["ling"] += 1
    fc.score["compling"] += 1
    await message.answer(text="3. Какую предметную область тебе интереснее изучать?\n\n"
                              "а) Технические науки (математика, информатика)\n"
                              "б) Гуманитарные науки (история, филология, психология, лингвистика, литература)\n"
                              "в) Социальные науки (экономика, социология, политология, обществознание)\n"
                              "г) Естественные науки (физика, химия, биология)\n"
                              "д) Искусство и дизайн", reply_markup=kb.third_q)


@router.message(F.text == 'Нет, не хочу')
async def q3_2(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    fc.score["advert"] += 1
    fc.score["books"] += 1
    fc.score["psyteach"] += 1
    await message.answer(text="3. Какую предметную область тебе интереснее изучать?\n\n"
                              "а) Технические науки (математика, информатика)\n"
                              "б) Гуманитарные науки (история, филология, психология, лингвистика, литература)\n"
                              "в) Социальные науки (экономика, социология, политология, обществознание)\n"
                              "г) Естественные науки (физика, химия, биология)\n"
                              "д) Искусство и дизайн", reply_markup=kb.third_q)


@router.message(F.text == 'а) Технические науки')
async def q4_1(message: types.Message):
    fc.score["compling"] += 1
    await message.answer(text="4. Какое качество тебе ближе?", reply_markup=kb.fourth_q)


@router.message(F.text == 'б) Гуманитарные науки')
async def q4_2(message: types.Message):
    fc.score["law"] += 1
    fc.score["region"] += 1
    fc.score["advert"] += 1
    fc.score["books"] += 1
    fc.score["ling"] += 1
    fc.score["compling"] += 1
    fc.score["psyteach"] += 1
    await message.answer(text="4. Какое качество тебе ближе?", reply_markup=kb.fourth_q)


@router.message(F.text == 'в) Социальные науки')
async def q4_3(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    fc.score["psyteach"] += 1
    await message.answer(text="4. Какое качество тебе ближе?", reply_markup=kb.fourth_q)


@router.message(F.text == 'г) Естественные науки')
async def q4_4(message: types.Message):
    fc.score["psyteach"] += 1
    fc.score["forensic"] += 1
    await message.answer(text="4. Какое качество тебе ближе?", reply_markup=kb.fourth_q)


@router.message(F.text == 'д) Искусство и дизайн')
async def q4_5(message: types.Message):
    fc.score["advert"] += 1
    fc.score["books"] += 1
    await message.answer(text="4. Какое качество тебе ближе?", reply_markup=kb.fourth_q)


@router.message(F.text == 'а) Внимательность')
async def q5_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    fc.score["compling"] += 1
    fc.score["ling"] += 1
    await message.answer(text="5. Какой ведущий навык ты можешь у себя выделить?", reply_markup=kb.fifth_q)


@router.message(F.text =='б) Многозадачность')
async def q5_2(message: types.Message):
    fc.score["law"] += 1
    fc.score["advert"] += 1
    await message.answer(text="5. Какой ведущий навык ты можешь у себя выделить?", reply_markup=kb.fifth_q)


@router.message(F.text == 'в) Усидчивость')
async def q5_3(message: types.Message):
    fc.score["region"] += 1
    fc.score["books"] += 1
    fc.score["ling"] += 1
    fc.score["compling"] += 1
    await message.answer(text="5. Какой ведущий навык ты можешь у себя выделить?", reply_markup=kb.fifth_q)


@router.message(F.text == 'г) Стрессоустойчивость')
async def q5_4(message: types.Message):
    fc.score["forensic"] += 1
    fc.score["psyteach"] += 1
    await message.answer(text="5. Какой ведущий навык ты можешь у себя выделить?", reply_markup=kb.fifth_q)


@router.message(F.text == 'д) Коммуникабельность')
async def q5_5(message: types.Message):
    fc.score["region"] += 1
    fc.score["advert"] += 1
    fc.score["psyteach"] += 1
    fc.score["ling"] += 1
    await message.answer(text="5. Какой ведущий навык ты можешь у себя выделить?", reply_markup=kb.fifth_q)


@router.message(F.text == 'а) Ораторское искусство')
async def q6_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    fc.score["advert"] += 1
    await message.answer(text="6. Что ты любишь делать в свободное время?\n\n"
                              "а) Читать книги, журналы\n"
                              "б) Писать и редактировать произведения, посты в социальных сетях\n"
                              "в) Изучать языки", reply_markup=kb.sixth_q)


@router.message(F.text == 'б) Логическое мышление')
async def q6_2(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    fc.score["compling"] += 1
    await message.answer(text="6. Что ты любишь делать в свободное время?\n\n"
                              "а) Читать книги, журналы\n"
                              "б) Писать и редактировать произведения, посты в социальных сетях\n"
                              "в) Изучать языки", reply_markup=kb.sixth_q)


@router.message(F.text == 'в) Креативное мышление')
async def q6_3(message: types.Message):
    fc.score["advert"] += 1
    fc.score["books"] += 1
    fc.score["psyteach"] += 1
    await message.answer(text="6. Что ты любишь делать в свободное время?\n\n"
                              "а) Читать книги, журналы\n"
                              "б) Писать и редактировать произведения, посты в социальных сетях\n"
                              "в) Изучать языки", reply_markup=kb.sixth_q)


@router.message(F.text == 'г) Эрудированность')
async def q6_4(message: types.Message):
    fc.score["region"] += 1
    fc.score["books"] += 1
    fc.score["law"] += 1
    fc.score["ling"] += 1
    await message.answer(text="6. Что ты любишь делать в свободное время?\n\n"
                              "а) Читать книги, журналы\n"
                              "б) Писать и редактировать произведения, посты в социальных сетях\n"
                              "в) Изучать языки", reply_markup=kb.sixth_q)


@router.message(F.text == 'а) Читать книги, журналы')
async def q7_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["books"] += 1
    await message.answer(text="7. Что выберешь смотреть на выходных?\n\n"
                              "а) Тру-крайм сериал\n"
                              "б) Туториал по разработке компьютерной игры\n"
                              "в) Тревел-блог\n", reply_markup=kb.seventh_q)


@router.message(F.text == 'б) Посты в соц. сетях')
async def q7_2(message: types.Message):
    fc.score["advert"] += 1
    fc.score["books"] += 1
    fc.score["forensic"] += 1
    await message.answer(text="7. Что выберешь смотреть на выходных?\n\n"
                              "а) Тру-крайм сериал\n"
                              "б) Туториал по разработке компьютерной игры\n"
                              "в) Тревел-блог\n", reply_markup=kb.seventh_q)


@router.message(F.text == 'в) Изучать языки')
async def q7_3(message: types.Message):
    fc.score["region"] += 1
    fc.score["ling"] += 1
    fc.score["compling"] += 1
    await message.answer(text="7. Что выберешь смотреть на выходных?\n\n"
                              "а) Тру-крайм сериал\n"
                              "б) Туториал по разработке компьютерной игры\n"
                              "в) Тревел-блог\n", reply_markup=kb.seventh_q)


@router.message(F.text == 'а) Тру-крайм')
async def q8_1(message: types.Message):
    fc.score["forensic"] += 1
    fc.score["law"] += 1
    fc.score["psyteach"] += 1
    await message.answer(text="8. Какую рабочую задачу тебе хотелось бы выполнить?\n\n"
                              "а) Поучаствовать в следственном мероприятии\n"
                              "б) Обсудить с автором твоей любимой книги условия её публикации\n"
                              "в) Ничего из этого", reply_markup=kb.eight_q)


@router.message(F.text == 'б) Туториал')
async def q8_2(message: types.Message):
    fc.score["compling"] += 1
    await message.answer(text="8. Какую рабочую задачу тебе хотелось бы выполнить?\n\n"
                              "а) Поучаствовать в следственном мероприятии\n"
                              "б) Обсудить с автором твоей любимой книги условия её публикации\n"
                              "в) Ничего из этого", reply_markup=kb.eight_q)


@router.message(F.text == 'в) Тревел-блог')
async def q8_3(message: types.Message):
    fc.score["region"] += 1
    await message.answer(text="8. Какую рабочую задачу тебе хотелось бы выполнить?\n\n"
                              "а) Поучаствовать в следственном мероприятии\n"
                              "б) Обсудить с автором твоей любимой книги условия её публикации\n"
                              "в) Ничего из этого", reply_markup=kb.eight_q)


@router.message(F.text == 'а) Следственные мероприятия')
async def q9_1(message: types.Message):
    fc.score["law"] += 1
    fc.score["forensic"] += 1
    await message.answer(text="9. Нужно проанализировать отзывы на товар. Как ты это сделаешь?\n\n"
                              "а) Включу автоматический фильтр на сайте и просмотрю вручную\n"
                              "б) Напишу программу, которая сделает это за меня\n"
                              "в) Не буду это делать", reply_markup=kb.ninth_q)


@router.message(F.text == 'б) Обсудить публикацию')
async def q9_2(message: types.Message):
    fc.score["books"] += 1
    await message.answer(text="9. Нужно проанализировать отзывы на товар. Как ты это сделаешь?\n\n"
                              "а) Включу автоматический фильтр на сайте и просмотрю вручную\n"
                              "б) Напишу программу, которая сделает это за меня\n"
                              "в) Не буду это делать", reply_markup=kb.ninth_q)


@router.message(F.text == 'в) Никакую из этих')
async def q9_3(message: types.Message):
    # Никуда балл не ставим
    await message.answer(text="9. Нужно проанализировать отзывы на товар. Как ты это сделаешь?\n\n"
                              "а) Включу автоматический фильтр на сайте и просмотрю вручную\n"
                              "б) Напишу программу, которая сделает это за меня\n"
                              "в) Не буду это делать", reply_markup=kb.ninth_q)


@router.message(F.text == 'а) Включу фильтр')
async def q10_1(message: types.Message):
    fc.score["advert"] += 1
    await message.answer(text="10. Что выберешь сделать?\n\n"
                              "а) Провести химический опыт\n"
                              "б) Провести урок / мероприятие в школе\n"
                              "в) Ничего из этого", reply_markup=kb.tenth_q)


@router.message(F.text == 'б) Напишу программу')
async def q10_2(message: types.Message):
    fc.score["compling"] += 1
    await message.answer(text="10. Что выберешь сделать?\n\n"
                              "а) Провести химический опыт\n"
                              "б) Провести урок / мероприятие в школе\n"
                              "в) Ничего из этого", reply_markup=kb.tenth_q)


@router.message(F.text == 'в) Не буду это делать')
async def q10_3(message: types.Message):
    # Никуда балл не ставим
    await message.answer(text="10. Что выберешь сделать?\n\n"
                              "а) Провести химический опыт\n"
                              "б) Провести урок / мероприятие в школе\n"
                              "в) Ничего из этого", reply_markup=kb.tenth_q)


@router.message(F.text == 'а) Провести опыт')
async def q11_1(message: types.Message):
    fc.score["forensic"] += 1
    await message.answer(text="11. Что предпочтешь?\n\n"
                              "а) Помогать при подготовке и выпуске печатных изданий\n"
                              "б) Организовать выставку или форум\n"
                              "в) Быть вожатым(-ой) в лагере\n"
                              "г) Участвовать в общественной жизни школы, города\n"
                              "д) Ничего из этого", reply_markup=kb.eleventh_q)


@router.message(F.text == 'б) Провести урок')
async def q11_2(message: types.Message):
    fc.score["ling"] += 1
    fc.score["psyteach"] += 1
    await message.answer(text="11. Что предпочтешь?\n\n"
                              "а) Помогать при подготовке и выпуске печатных изданий\n"
                              "б) Организовать выставку или форум\n"
                              "в) Быть вожатым(-ой) в лагере\n"
                              "г) Участвовать в общественной жизни школы, города\n"
                              "д) Ничего из этого", reply_markup=kb.eleventh_q)


@router.message(F.text == 'в) Ничего не выберу')
async def q11_3(message: types.Message):
    # Никуда балл не ставим
    await message.answer(text="11. Что предпочтешь?\n\n"
                              "а) Помогать при подготовке и выпуске печатных изданий\n"
                              "б) Организовать выставку или форум\n"
                              "в) Быть вожатым(-ой) в лагере\n"
                              "г) Участвовать в общественной жизни школы, города\n"
                              "д) Ничего из этого", reply_markup=kb.eleventh_q)


@router.message(F.text == 'а) Помогать в издании')
async def q12_1(message: types.Message):
    fc.score["books"] += 1
    fc.score["ling"] += 1
    await message.answer(text="12. Что выберешь изучить?\n\n"
                              "а) Историю и культуру страны\n"
                              "б) Язык программирования\n"
                              "в) Ничего из этого", reply_markup=kb.twelth_q)


@router.message(F.text == 'б) Организовать выставку')
async def q12_2(message: types.Message):
    fc.score["region"] += 1
    await message.answer(text="12. Что выберешь изучить?\n\n"
                              "а) Историю и культуру страны\n"
                              "б) Язык программирования\n"
                              "в) Ничего из этого", reply_markup=kb.twelth_q)


@router.message(F.text == 'в) Быть вожатым(-ой)')
async def q12_3(message: types.Message):
    fc.score["psyteach"] += 1
    await message.answer(text="12. Что выберешь изучить?\n\n"
                              "а) Историю и культуру страны\n"
                              "б) Язык программирования\n"
                              "в) Ничего из этого", reply_markup=kb.twelth_q)


@router.message(F.text == 'г) Участвовать в жизни школы')
async def q12_4(message: types.Message):
    fc.score["law"] += 1
    fc.score["advert"] += 1
    await message.answer(text="12. Что выберешь изучить?\n\n"
                              "а) Историю и культуру страны\n"
                              "б) Язык программирования\n"
                              "в) Ничего из этого", reply_markup=kb.twelth_q)


@router.message(F.text == 'д) Ничего из этого')
async def q12_5(message: types.Message):
    # Никуда балл не ставим
    await message.answer(text="12. Что выберешь изучить?\n\n"
                              "а) Историю и культуру страны\n"
                              "б) Язык программирования\n"
                              "в) Ничего из этого", reply_markup=kb.twelth_q)

@router.message(F.text == 'а) Историю и культуру')
async def q13_1(message: types.Message):
    fc.score["region"] += 1
    await message.answer(text="13. Что выберешь?\n\n"
                              "а) Создавать контент для привлечения аудитории\n"
                              "б) Работать с детьми и подростками\n"
                              "в) Что-то другое", reply_markup=kb.thirteenth_q)


@router.message(F.text == 'б) Язык программирования')
async def q13_2(message: types.Message):
    fc.score["compling"] += 1
    await message.answer(text="13. Что выберешь?\n\n"
                              "а) Создавать контент для привлечения аудитории\n"
                              "б) Работать с детьми и подростками\n"
                              "в) Что-то другое", reply_markup=kb.thirteenth_q)


@router.message(F.text == 'в) Ничего')
async def q13_3(message: types.Message):
    # Никуда балл не ставим
    await message.answer(text="13. Что выберешь?\n\n"
                              "а) Создавать контент для привлечения аудитории\n"
                              "б) Работать с детьми и подростками\n"
                              "в) Что-то другое", reply_markup=kb.thirteenth_q)


@router.message(F.text == "а) Создавать контент")
async def handle_bye_1(message: types.Message):
    fc.score["advert"] += 1
    fc.score["books"] += 1

    for k, val in fc.score.items():
        if val >= 7:
            prog = k
            global counter_answer
            counter_answer += 1
            await message.answer(text=f"Тебе может подойти  *{fc.programms[prog]}* \n\n"
                                      f"*Ссылка на официальный сайт ГИ:* {fc.urls[prog]} \n\n"
                                      f"*Описание программы:* {fc.description[prog]} \n\n"
                                      f"*Профессии выпускников:* {fc.jobs[prog]} \n\n"
                                      f"*Минимальные баллы:*\n {fc.min_points[prog]}", parse_mode="Markdown")

            await message.answer(text="Кек-кек-кек! Благодарим за прохождение нашей анкеты, надеемся, "
                                  "что результаты помогли тебе хотя бы немного разобраться в своих мыслях. "
                                  "Результаты данного анкетирования не являются исчерпывающими. "
                                  "Они предоставляют лишь общую картину и могут быть полезным для понимания своих желаний в выборе будущего "
                                  "направления образования. Информацию, полученную из этой анкеты, следует рассматривать в контексте других факторов, "
                                  "она не должна быть единственным основанием для принятия решений. Удачи!", reply_markup=kb.cal_after_survey)
    if counter_answer == 0:
        await message.answer(text="К сожалению, в результате данного анкетирования я не смог найти направление, которое сможет тебя заинтересовать. Вероятно, тебе еще предстоит узнать свои личные и профессиональные интересы или тебя заинтересуют направления подготовки других институтов Политеха!",reply_markup=kb.back)


@router.message(F.text == "б) Работать с детьми")
async def handle_bye_2(message: types.Message):
    fc.score["psyteach"] += 1
    fc.score["ling"] += 1

    for k, val in fc.score.items():
        if val >= 7:
            prog = k
            global counter_answer
            counter_answer += 1
            await message.answer(text=f"Тебе может подойти  *{fc.programms[prog]}* \n\n"
                                      f"*Ссылка на официальный сайт ГИ:* {fc.urls[prog]} \n\n"
                                      f"*Описание программы:* {fc.description[prog]} \n\n"
                                      f"*Профессии выпускников:* {fc.jobs[prog]} \n\n"
                                      f"*Минимальные баллы:*\n {fc.min_points[prog]}", parse_mode="Markdown")

            await message.answer(text="Кек-кек-кек! Благодарим за прохождение нашей анкеты, надеемся, "
                                  "что результаты помогли тебе хотя бы немного разобраться в своих мыслях. "
                                  "Результаты данного анкетирования не являются исчерпывающими. "
                                  "Они предоставляют лишь общую картину и могут быть полезным для понимания своих желаний в выборе будущего "
                                  "направления образования. Информацию, полученную из этой анкеты, следует рассматривать в контексте других факторов, "
                                  "она не должна быть единственным основанием для принятия решений. Удачи!", reply_markup=kb.cal_after_survey)
    if counter_answer == 0:
        await message.answer(text="К сожалению, в результате данного анкетирования я не смог найти направление, которое сможет тебя заинтересовать. Вероятно, тебе еще предстоит узнать свои личные и профессиональные интересы или тебя заинтересуют направления подготовки других институтов Политеха!", reply_markup=kb.back)


@router.message(F.text == "в) Что-то другое")
async def handle_bye_3(message: types.Message):
    # Никуда балл не ставим

    for k, val in fc.score.items():
        if val >= 7:
            prog = k
            global counter_answer
            counter_answer += 1
            await message.answer(text=f"Тебе может подойти  *{fc.programms[prog]}* \n\n"
                                      f"*Ссылка на официальный сайт ГИ:* {fc.urls[prog]} \n\n"
                                      f"*Описание программы:* {fc.description[prog]} \n\n"
                                      f"*Профессии выпускников:* {fc.jobs[prog]} \n\n"
                                      f"*Минимальные баллы:*\n {fc.min_points[prog]}", parse_mode="Markdown")

            await message.answer(text="Кек-кек-кек! Благодарим за прохождение нашей анкеты, надеемся, "
                                  "что результаты помогли тебе хотя бы немного разобраться в своих мыслях. "
                                "Результаты данного анкетирования не являются исчерпывающими. "
                                "Они предоставляют лишь общую картину и могут быть полезным для понимания своих желаний в выборе будущего "
                                "направления образования. Информацию, полученную из этой анкеты, следует рассматривать в контексте других факторов, "
                                "она не должна быть единственным основанием для принятия решений. Удачи!", reply_markup=kb.cal_after_survey)
    if counter_answer == 0:
        await message.answer(text="К сожалению, в результате данного анкетирования я не смог найти направление, которое сможет тебя заинтересовать. Вероятно, тебе еще предстоит узнать свои личные и профессиональные интересы или тебя заинтересуют направления подготовки других институтов Политеха!", reply_markup=kb.back)


@router.callback_query(F.data == "calculator")
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="Ты уже сдал(-а) ЕГЭ или прошел(-ла) вступительные испытания?", reply_markup=kb.exam_passed)


@router.message(F.text == "Да")
async def yes(message: types.Message):
    global passed
    passed = True
    await message.answer(text="Введи свой суммарный балл, включая баллы за ИД\nБаллы за ИД можно посмотреть здесь: https://www.spbstu.ru/abit/bachelor/oznakomitsya-with-the-regulations/individual-achievements/")

@router.message(F.text == "Нет")
async def no(message: types.Message):

    for k, val in fc.score.items():
        if val >= 7:
            prog = k
            await message.answer(f"В таком случае ориентируйся на проходные баллы прошлых лет.\n"
                        f"На направление подготовки {fc.programms[prog]} в 2022 г. проходной балл был {fc.exam_points22[prog]}, "
                        f"а в 2023 г. - {fc.exam_points23[prog]}.\n\nНадеюсь, эта информация была для тебя полезной! Успехов!",reply_markup=kb.back)

@router.message()
async def check_points(message: types.Message):
    try:
        points = int(message.text)
    except ValueError:
        await message.answer("Что-то пошло не так :(\nВведи свой суммарный балл, включая баллы за ИД")

    for k, val in fc.score.items():
        if val >= 7:
            prog = k
            if points < fc.exam_points22[prog]:
                answ22 = f"На направление подготовки {fc.programms[prog]} в 2022г. ты бы не прошел(-ла)."
            else:
                answ22 = f"На направление подготовки {fc.programms[prog]} в 2022г. ты бы прошел(-ла)."

            if points < fc.exam_points23[prog]:
                answ23 = f"На направление подготовки {fc.programms[prog]} в 2023г. ты бы не прошел(-ла)."
            else:
                answ23 = f"На направление подготовки {fc.programms[prog]} в 2023г. ты бы прошел(-ла)."

            await message.answer(f"Если рассматривать проходные баллы прошлых лет, то\n\n{answ22}\n{answ23}\n\nНадеюсь, эта информация была для тебя полезной! Успехов!",reply_markup=kb.back)

