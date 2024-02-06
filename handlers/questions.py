import aiogram.utils.markdown as md
import aiogram.utils.formatting as f

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.for_questions import get_yes_no_kb

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    # await message.answer(
    #     # md.bold('Вы довольны своей работой?'),
    #     "Вы довольны <b>своей</b> работой?",
    #     reply_markup=get_yes_no_kb()
    # )
    # kb = ReplyKeyboardBuilder()
    # kb.button(text="show the app")
    # kb.adjust(1)
    # await message.answer(
    #    "show",
    #    reply_markup=kb.as_markup(resize_keyboard=True)
    # )
    await message.answer(
        "<b>Утверждение заявки руководителем</b>\n\nЗаявка на выдачу ДС №000032157 от 19.01.2024\nСумма: 3500.00 UAH\nНазначение: оплата рекламных услуг"
    )


@router.message(F.text.lower() == "да")
async def answer_yes(message: Message):
    await message.answer(
        "Это здорово!",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text.lower() == "нет")
async def answer_no(message: Message):
    await message.answer(
        "<i>Жаль</i>...",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text.lower() == "show the app")
async def answer_show(message: Message):
    await message.answer(
        "Let's go",
        reply_markup=ReplyKeyboardRemove()
    )